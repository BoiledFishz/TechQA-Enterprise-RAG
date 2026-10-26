"""E2: does another embedding model or chunk size raise first-stage recall? (2026-10-26)

    python -m evaluation.chap12_e2_recall --index PATH/chap12_tune.sqlite --download
    python -m evaluation.chap12_e2_recall --index PATH/chap12_tune.sqlite

Diagnosis only, TUNE split, no LLM calls. Questions: the 112 answerable tune questions; the
query is the rewritten query recorded in results/chap12/tune_real_r9_judged14/traces.jsonl
(the current configuration), and the raw question as a second query source. For every
(embedder, chunking) pair it encodes the 6,500 sample documents, ranks documents by their best
chunk (cosine), and reports document-level recall@k of the single gold document, the smallest
k that reaches 85% / 90%, a hybrid proxy (RRF, k=60, of that dense ranking and the BM25 ranking)
and hits in the E1 manual categories A-D.

Embedders (local files only; `--download` fetches them once into .rag_data/models/e2_*/ and
records the resolved Hugging Face commit in e2_manifest.json):
  minilm   sentence-transformers/all-MiniLM-L6-v2, Project 1's pinned encoder (window 256 /
           stride 16 / mean); for chunking c1200 the stored Project 1 vectors are used as is
  bge      BAAI/bge-base-en-v1.5, CLS pooling, query instruction prefix
  e5       intfloat/e5-base-v2, mean pooling, "query: " / "passage: " prefixes
  nomic    nomic-embed-text through Ollama /api/embed, "search_query: " / "search_document: "
For bge and e5, inputs longer than 512 tokens are split into 512-token windows (stride 64) and
the window vectors averaged, so no text is silently cut off (as Project 1 does for MiniLM).
Chunkings (Project 1's legacy splitter, title + body, parameterised):
  c600  max 600 chars, overlap 80      c1200 max 1200, overlap 160 (current)
  c2400 max 2400, overlap 320          head  one chunk per document: title + first 1000 chars
BM25: Project 1's query construction (24 highest-idf terms, title-line boost) with FTS5 column
weights title:body = 1:1, 3:1 (current) and 6:1. The 3:1 ranking is checked against Project 1's
TechQAIndex.search.

Vectors are cached in .rag_data/e2/ (outside Project 1's files). Writes
results/chap12/e2_recall/{summary.json,summary.md,per_task.jsonl}.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sqlite3
import time
from collections import Counter
from collections.abc import Callable, Iterable, Sequence
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_judged14"
OUT = HERE / "results/chap12/e2_recall"
KS = (1, 3, 5, 8, 10, 20, 30, 50, 100)
DEPTH = 100
RRF_K = 60
CHUNKINGS = {"c600": (600, 80), "c1200": (1200, 160), "c2400": (2400, 320), "head": None}
HF = {
    "bge": {"repo": "BAAI/bge-base-en-v1.5", "pool": "cls",
            "query": "Represent this sentence for searching relevant passages: ", "doc": ""},
    "e5": {"repo": "intfloat/e5-base-v2", "pool": "mean", "query": "query: ", "doc": "passage: "},
}
NOMIC = {"query": "search_query: ", "doc": "search_document: "}
BM25_WEIGHTS = {"bm25_1to1": (1, 1), "bm25_3to1": (3, 1), "bm25_6to1": (6, 1)}
# E1 manual first read (results/chap12/e1_gap_analysis/summary.md), tune task numbers.
E1_CATEGORIES = {
    "A": (17, 25, 49, 56, 76, 85, 99, 119, 135),
    "B": (7, 21, 25, 34, 38, 87, 101, 121, 125),
    "C": (45, 66, 105, 106, 127, 142),
    "D": (7, 22, 25, 45, 70, 87, 111, 139),
}


# ---------------------------------------------------------------- chunking
def split(title: str, body: str, size: int, overlap: int) -> list[str]:
    """Project 1 legacy_chunks with the size and overlap as parameters (break >= size/2)."""
    text = f"{title}\n\n{body}" if title else body
    out: list[str] = []
    cursor = 0
    while cursor < len(text):
        remaining = text[cursor:]
        end = min(len(remaining), size)
        if len(remaining) > size:
            for pattern in (r"\n\n+", r"\n", r"(?<=[.!?])\s+", r"\s+"):
                matches = list(re.finditer(pattern, remaining[:size]))
                if matches and matches[-1].start() >= size // 2:
                    end = matches[-1].start()
                    break
        chunk = remaining[:end].strip()
        if chunk:
            out.append(chunk)
        if cursor + end >= len(text):
            break
        cursor += max(1, end - overlap)
    return out


def chunk_corpus(docs: dict[str, tuple[str, str]], chunking: str) -> tuple[list[str], list[str]]:
    owners: list[str] = []
    texts: list[str] = []
    for doc_id in sorted(docs):
        title, body = docs[doc_id]
        params = CHUNKINGS[chunking]
        parts = ([f"{title}\n\n{body[:1000]}".strip()] if params is None
                 else split(title, body, *params))
        owners += [doc_id] * len(parts)
        texts += parts
    return owners, texts


# ---------------------------------------------------------------- encoders
class HFEncoder:
    """Bi-encoder with windowed pooling (512-token windows, stride 64, mean of windows)."""

    def __init__(self, path: Path, pool: str, device: str, batch: int = 64) -> None:
        import torch
        from transformers import AutoModel, AutoTokenizer

        self.torch, self.pool, self.batch = torch, pool, batch
        self.tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
        self.model = AutoModel.from_pretrained(path, local_files_only=True).to(device).eval()
        if device == "cuda":
            self.model = self.model.half()
        self.device = device

    def encode(self, texts: Sequence[str]) -> Any:
        import numpy as np

        enc = self.tokenizer(list(texts), truncation=True, max_length=512, stride=64,
                             return_overflowing_tokens=True, padding=False)
        owners = enc.pop("overflow_to_sample_mapping")
        sums = np.zeros((len(texts), self.model.config.hidden_size), dtype="float32")
        counts = np.zeros(len(texts), dtype="float32")
        order = sorted(range(len(owners)), key=lambda i: len(enc["input_ids"][i]))
        for start in range(0, len(order), self.batch):
            idx = order[start:start + self.batch]
            rows = [{k: v[i] for k, v in enc.items()} for i in idx]
            batch = self.tokenizer.pad(rows, padding=True, return_tensors="pt")
            batch = {k: v.to(self.device) for k, v in batch.items()}
            with self.torch.inference_mode():
                states = self.model(**batch).last_hidden_state.float()
            if self.pool == "cls":
                pooled = states[:, 0]
            else:
                mask = batch["attention_mask"].unsqueeze(-1).float()
                pooled = (states * mask).sum(1) / mask.sum(1).clamp(min=1)
            pooled = self.torch.nn.functional.normalize(pooled, p=2, dim=1).cpu().numpy()
            for row, i in zip(pooled, idx, strict=True):
                sums[owners[i]] += row
                counts[owners[i]] += 1
        sums /= np.maximum(counts, 1)[:, None]
        return sums / np.maximum(np.linalg.norm(sums, axis=1, keepdims=True), 1e-12)


class OllamaEncoder:
    def __init__(self, url: str, model: str = "nomic-embed-text", batch: int = 32) -> None:
        self.url, self.model, self.batch = url.rstrip("/"), model, batch

    def encode(self, texts: Sequence[str]) -> Any:
        import urllib.request

        import numpy as np

        out = []
        for start in range(0, len(texts), self.batch):
            body = json.dumps({"model": self.model, "input": list(texts[start:start + self.batch]),
                               "truncate": True}).encode()
            req = urllib.request.Request(self.url + "/api/embed", body,
                                         {"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=600) as resp:
                out += json.loads(resp.read())["embeddings"]
        arr = np.asarray(out, dtype="float32")
        return arr / np.maximum(np.linalg.norm(arr, axis=1, keepdims=True), 1e-12)


def model_dir(root: Path, name: str) -> Path:
    return root / ".rag_data/models" / f"e2_{name}"


def download(root: Path) -> list[dict[str, str]]:
    from huggingface_hub import HfApi, snapshot_download

    done = []
    for name, spec in HF.items():
        path = model_dir(root, name)
        info_hf = HfApi().model_info(spec["repo"], files_metadata=False)
        commit = info_hf.sha
        files = [f.rfilename for f in info_hf.siblings or []]
        weights = "model.safetensors" if "model.safetensors" in files else "pytorch_model.bin"
        snapshot_download(spec["repo"], revision=commit, local_dir=path,
                          allow_patterns=["*.json", "*.txt", weights])
        info = {"repo": spec["repo"], "revision": str(commit), "downloaded": time.strftime("%F")}
        (path / "e2_manifest.json").write_text(json.dumps(info, indent=2), encoding="utf-8")
        done.append(info)
    return done


# ---------------------------------------------------------------- ranking
def rank_docs(query_vec: Any, vectors: Any, owners: Sequence[str], depth: int = DEPTH) -> list[str]:
    """Documents ordered by their best chunk's cosine with the query."""
    import numpy as np

    scores = vectors @ query_vec
    order = np.argsort(-scores, kind="stable")
    seen: list[str] = []
    found: set[str] = set()
    for i in order:
        doc = owners[int(i)]
        if doc not in found:
            found.add(doc)
            seen.append(doc)
            if len(seen) == depth:
                break
    return seen


def rrf(*rankings: Sequence[str], k: int = RRF_K, depth: int = DEPTH) -> list[str]:
    score: Counter[str] = Counter()
    for ranking in rankings:
        for rank, doc in enumerate(ranking, 1):
            score[doc] += 1 / (k + rank)
    return [d for d, _ in sorted(score.items(), key=lambda x: (-x[1], x[0]))][:depth]


def bm25_search(db: sqlite3.Connection, count: int, query: str, weights: tuple[int, int],
                tokens: Callable[[str], list[str]], depth: int = DEPTH) -> list[str]:
    """Project 1 TechQAIndex.search with the FTS5 column weights as a parameter."""
    terms = Counter(tokens(query))
    if not terms:
        return []
    title_terms = set(tokens(query.splitlines()[0]))
    idf = {}
    for term in terms:
        row = db.execute("SELECT doc FROM vocabulary WHERE term=?", (term,)).fetchone()
        df = row[0] if row else max(10, count // 100)
        idf[term] = math.log1p(count / (df + 1)) * (1.5 if term in title_terms else 1)
    chosen = sorted(terms, key=lambda t: idf[t], reverse=True)[:24]
    expression = " OR ".join('"' + t + '"' for t in chosen)
    rows = db.execute(
        "SELECT d.doc_id FROM (SELECT rowid,rank FROM search WHERE search MATCH ? AND rank MATCH "
        f"'bm25({weights[0]},{weights[1]})' ORDER BY rank LIMIT ?) r JOIN docs d "
        "ON d.rowid=r.rowid ORDER BY r.rank", (expression, depth)).fetchall()
    return [r[0] for r in rows]


def metrics(ranks: Iterable[int | None], n: int) -> dict[str, Any]:
    ranks = list(ranks)
    out: dict[str, Any] = {f"R@{k}": round(sum(1 for r in ranks if r and r <= k) / n, 3)
                           for k in KS}
    for target in (0.85, 0.90):
        need = math.ceil(target * n)
        hits = sorted(r for r in ranks if r)
        out[f"k{int(target * 100)}"] = hits[need - 1] if len(hits) >= need else f">{DEPTH}"
    return out


def gold_rank(ranking: Sequence[str], gold: str) -> int | None:
    return ranking.index(gold) + 1 if gold in ranking else None


# ---------------------------------------------------------------- main
def load_questions() -> list[dict[str, Any]]:
    tasks = {t["task_id"]: t for t in map(json.loads, (HERE / "chap12/tune/mixed_tasks.jsonl")
                                          .read_text("utf-8").splitlines())}
    traces = {r["task_id"]: r for r in map(json.loads, (RUN / "traces.jsonl")
                                           .read_text("utf-8-sig").splitlines()) if r}
    out = []
    for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl").read_text("utf-8")
                 .splitlines()):
        if g.get("answerable") != "Y":
            continue
        tid = g["task_id"]
        r = traces[tid]["layers"]["retrieval"]
        dense = {x["doc"]: x["rank"] for x in r["stages"]["dense"]}
        number = int(tid.rsplit("-", 1)[1])
        out.append({"task_id": tid, "gold": g["document"], "raw": tasks[tid]["query"],
                    "rewritten": r["query"], "trace_dense_rank": dense.get(g["document"]),
                    "trace_dense_docs": [x["doc"] for x in r["stages"]["dense"]],
                    "categories": [c for c, ids in E1_CATEGORIES.items() if number in ids]})
    return out


def vectors_for(root: Path, embedder: str, chunking: str, docs: dict[str, tuple[str, str]],
                encoder: Any, cache: Path, log: Callable[[str], None]) -> tuple[Any, list[str]]:
    import numpy as np

    vec_path, own_path = cache / f"{embedder}_{chunking}.npy", cache / f"{embedder}_{chunking}.json"
    if vec_path.is_file() and own_path.is_file():
        return np.load(vec_path), json.loads(own_path.read_text("utf-8"))
    if embedder == "minilm" and chunking == "c1200":
        sidecar = root / ".rag_data/chap12_tune.dense.sqlite"
        db = sqlite3.connect(sidecar.resolve().as_uri() + "?mode=ro", uri=True)
        rows = db.execute("SELECT doc_id, vector FROM chunks ORDER BY rowid").fetchall()
        owners = [r[0] for r in rows]
        vectors = np.frombuffer(b"".join(r[1] for r in rows), dtype="float32").reshape(
            len(rows), -1)
    else:
        owners, texts = chunk_corpus(docs, chunking)
        prefix = HF[embedder]["doc"] if embedder in HF else NOMIC["doc"] if embedder == "nomic" \
            else ""
        started = time.time()
        parts = []
        for s in range(0, len(texts), 2048):
            parts.append(encoder.encode([prefix + t for t in texts[s:s + 2048]]))
            log(f"  {embedder}/{chunking}: {min(s + 2048, len(texts))}/{len(texts)} chunks, "
                f"{time.time() - started:.0f}s")
        vectors = np.vstack(parts).astype("float32")
    cache.mkdir(parents=True, exist_ok=True)
    np.save(vec_path, vectors)
    own_path.write_text(json.dumps(owners), encoding="utf-8")
    return vectors, owners


def make_encoder(root: Path, embedder: str, device: str, ollama: str) -> Any:
    if embedder == "minilm":
        from rag.techqa.semantic import MiniLMEncoder

        return MiniLMEncoder(root / ".rag_data/models/minilm", batch_size=64, device=device)
    if embedder == "nomic":
        return OllamaEncoder(ollama)
    path = model_dir(root, embedder)
    if not (path / "e2_manifest.json").is_file():
        raise FileNotFoundError(f"{path} missing; run with --download first")
    return HFEncoder(path, HF[embedder]["pool"], device)


def identity(root: Path, embedder: str) -> str:
    if embedder in HF:
        info = json.loads((model_dir(root, embedder) / "e2_manifest.json").read_text("utf-8"))
        return f"{info['repo']}@{info['revision']}"
    if embedder == "minilm":
        from rag.techqa.semantic import MODEL_ID, MODEL_REVISION

        return f"{MODEL_ID}@{MODEL_REVISION}"
    return "ollama:nomic-embed-text"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--embedders", default="minilm,bge,e5,nomic")
    parser.add_argument("--chunkings", default="c600,c1200,c2400,head")
    parser.add_argument("--nomic-chunkings", default="c1200,head",
                        help="nomic goes through Ollama and is slow; only these chunkings")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--ollama", default="http://localhost:11434")
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--root", type=Path, default=None,
                        help="folder holding .rag_data (default: Project 1 ROOT)")
    args = parser.parse_args()
    from rag.techqa import data

    ROOT = args.root or data.ROOT  # noqa: N806
    from rag.techqa.index import TechQAIndex, tokens

    if args.download:
        print(json.dumps(download(ROOT), indent=2))
        return
    import torch

    device = ("cuda" if torch.cuda.is_available() else "cpu") if args.device == "auto" \
        else args.device
    args.out.mkdir(parents=True, exist_ok=True)
    log_lines: list[str] = []

    def log(line: str) -> None:
        print(line, flush=True)
        log_lines.append(line)

    db = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    docs = {d: (t or "", x or "") for d, t, x in db.execute("SELECT doc_id, title, text FROM docs")}
    count = int(dict(db.execute("SELECT key, value FROM manifest"))["document_count"])
    questions = load_questions()
    n = len(questions)
    log(f"questions={n} docs={len(docs)} device={device}")

    # BM25 rankings and the check against Project 1's search (weights 3:1).
    project1 = TechQAIndex(args.index)
    bm25: dict[str, dict[str, dict[str, list[str]]]] = {}
    agree = 0
    for name, w in BM25_WEIGHTS.items():
        bm25[name] = {src: {q["task_id"]: bm25_search(db, count, q[src], w, tokens)
                            for q in questions} for src in ("rewritten", "raw")}
    for q in questions:
        ref = [d["id"] for d in project1.search(q["rewritten"], DEPTH)]
        agree += ref == bm25["bm25_3to1"]["rewritten"][q["task_id"]]
    log(f"bm25 3:1 identical to Project 1 search for {agree}/{n} queries")

    results: list[dict[str, Any]] = []
    per_task: dict[str, dict[str, Any]] = {q["task_id"]: {
        "task_id": q["task_id"], "gold": q["gold"], "categories": q["categories"],
        "ranks": {}} for q in questions}

    def record(config: str, source: str, rankings: dict[str, list[str]], extra: dict[str, Any]
               ) -> None:
        ranks = {q["task_id"]: gold_rank(rankings[q["task_id"]], q["gold"]) for q in questions}
        row = {"config": config, "query": source, **extra, **metrics(ranks.values(), n)}
        for cat in E1_CATEGORIES:
            members = [q["task_id"] for q in questions if cat in q["categories"]]
            row[f"{cat}@8"] = f"{sum(1 for t in members if ranks[t] and ranks[t] <= 8)}/" \
                              f"{len(members)}"
            row[f"{cat}@30"] = f"{sum(1 for t in members if ranks[t] and ranks[t] <= 30)}/" \
                               f"{len(members)}"
        results.append(row)
        for tid, rank in ranks.items():
            per_task[tid]["ranks"][f"{config}|{source}"] = rank

    for name in BM25_WEIGHTS:
        for src in ("rewritten", "raw"):
            record(name, src, bm25[name][src], {"kind": "bm25"})

    for embedder in [e for e in args.embedders.split(",") if e]:
        chunkings = [c for c in args.chunkings.split(",") if c]
        if embedder == "nomic":
            chunkings = [c for c in chunkings if c in args.nomic_chunkings.split(",")]
        try:
            encoder = make_encoder(ROOT, embedder, device, args.ollama)
            ident = identity(ROOT, embedder)
        except Exception as exc:  # recorded, not hidden
            log(f"SKIP {embedder}: {type(exc).__name__}: {exc}")
            results.append({"config": embedder, "skipped": f"{type(exc).__name__}: {exc}"})
            continue
        for chunking in chunkings:
            started = time.time()
            try:
                vectors, owners = vectors_for(ROOT, embedder, chunking, docs, encoder,
                                              ROOT / ".rag_data/e2", log)
            except Exception as exc:
                log(f"SKIP {embedder}/{chunking}: {type(exc).__name__}: {exc}")
                results.append({"config": f"{embedder}/{chunking}",
                                "skipped": f"{type(exc).__name__}: {exc}"})
                continue
            qprefix = HF[embedder]["query"] if embedder in HF else NOMIC["query"] \
                if embedder == "nomic" else ""
            for src in ("rewritten", "raw"):
                qv = encoder.encode([qprefix + q[src] for q in questions])
                dense = {q["task_id"]: rank_docs(qv[i], vectors, owners)
                         for i, q in enumerate(questions)}
                extra = {"kind": "dense", "embedder": ident, "chunks": len(owners),
                         "seconds": round(time.time() - started)}
                if embedder == "minilm" and chunking == "c1200" and src == "rewritten":
                    same = sum(dense[q["task_id"]][:len(q["trace_dense_docs"])]
                               == q["trace_dense_docs"] for q in questions)
                    extra["trace_dense_identical"] = f"{same}/{n}"
                    log(f"minilm/c1200 dense order identical to the r9 trace for {same}/{n}")
                record(f"{embedder}/{chunking}", src, dense, extra)
                hybrid = {t: rrf(dense[t], bm25["bm25_3to1"][src][t]) for t in dense}
                record(f"{embedder}/{chunking}+bm25", src, hybrid, {"kind": "hybrid_proxy"})
            log(f"done {embedder}/{chunking} in {time.time() - started:.0f}s")

    (args.out / "summary.json").write_text(json.dumps(
        {"date": time.strftime("%F"), "device": device, "questions": n,
         "bm25_identical_to_project1": f"{agree}/{n}", "results": results, "log": log_lines},
        indent=2, ensure_ascii=False), encoding="utf-8")
    with (args.out / "per_task.jsonl").open("w", encoding="utf-8") as f:
        for row in per_task.values():
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    cols = ["R@1", "R@5", "R@8", "R@10", "R@20", "R@30", "R@50", "k85", "k90",
            "A@8", "B@8", "C@8", "D@8", "B@30", "C@30"]
    lines = [f"# E2 召回（调参集 {n} 道可回答题，文档级，唯一标准文档）", "",
             f"设备 {device}；BM25 3:1 与 Project 1 检索一致 {agree}/{n}。"
             "hybrid_proxy = 该稠密排名与 BM25(3:1) 的 RRF(k=60)，是线上融合的近似。", ""]
    for src in ("rewritten", "raw"):
        lines += [f"## 查询：{'改写后' if src == 'rewritten' else '原问题'}", "",
                  "| 配置 | " + " | ".join(cols) + " |", "|" + " --- |" * (len(cols) + 1)]
        lines += ["| " + r["config"] + " | " + " | ".join(str(r.get(c, "")) for c in cols) + " |"
                  for r in results if r.get("query") == src]
        lines.append("")
    skipped = [r for r in results if "skipped" in r]
    if skipped:
        lines += ["## 未执行", ""] + [f"- {r['config']}: {r['skipped']}" for r in skipped]
    (args.out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
