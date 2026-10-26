"""E3: which reranker orders the same candidates best? (2026-10-26; diagnosis, no LLM calls)

    python -m evaluation.chap12_e3_rerank --root PATH --cache PATH/techqa_rerank_cache.sqlite

TUNE split, the 112 answerable questions, current configuration (results/chap12/
tune_real_r9_judged14 traces: rewritten query, candidate_k 30). For each question the fused
candidates (30 chunks) are rebuilt offline exactly as the live pipeline builds them (BM25 +
sample MiniLM vectors; the rebuilt document order is checked against the trace), and the same
candidates are reordered by every reranker below. Documents are ranked by their first chunk.
Metrics: R@1/3/5/8 and MRR of the single gold document, the ceiling (gold among the
candidates), and hits at 5 / 8 in the E1 manual categories A-D.

Semantic terms (one score per candidate chunk):
  nomic       Project 1's nomic cosine, read only from the rerank cache (a missing vector is an
              error; the current order is reproduced and checked against the trace)
  bge, e5     cosine from the E2 bi-encoders (.rag_data/models/e2_*)
  ce_minilm, ce_bge  cross-encoder probability (.rag_data/models/ce_*, as in rounds 3-4)
Variants:
  fusion                 the fused (RRF) order, no rerank
  <sem>_only             semantic term alone
  <sem>+bm25             Project 1 formula 0.5 sem + 0.3 lexical + 0.2 BM25-rank prior
                         (nomic+bm25 is the current reranker)
  <sem>+max              same, prior = max(BM25-rank prior, fused-rank prior) (round 11)
Writes results/chap12/e3_rerank/{summary.json,summary.md,per_task.jsonl}.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_judged14"
OUT = HERE / "results/chap12/e3_rerank"
SEMANTIC = ("nomic", "bge", "e5", "ce_minilm", "ce_bge")
COST = {"fusion": 0, "nomic": 1, "bge": 2, "e5": 2, "ce_minilm": 2, "ce_bge": 3}
WEIGHTS = (0.5, 0.3, 0.2)
E1_CATEGORIES = {
    "A": (17, 25, 49, 56, 76, 85, 99, 119, 135),
    "B": (7, 21, 25, 34, 38, 87, 101, 121, 125),
    "C": (45, 66, 105, 106, 127, 142),
    "D": (7, 22, 25, 45, 70, 87, 111, 139),
}


def prior(rank: float) -> float:
    return 1 / (1 + rank / 5)


def order_docs(cands: list[dict[str, Any]], key: Any) -> list[str]:
    """Stable sort of candidate chunks by key (desc), then documents by first chunk."""
    ranked = sorted(range(len(cands)), key=lambda i: (-key(cands[i]), i))
    out: list[str] = []
    for i in ranked:
        if cands[i]["doc"] not in out:
            out.append(cands[i]["doc"])
    return out


def variants(cands: list[dict[str, Any]], available: list[str]) -> dict[str, list[str]]:
    ws, wl, wp = WEIGHTS
    out = {"fusion": order_docs(cands, lambda c: -c["fused_rank"])}
    for s in available:
        out[f"{s}_only"] = order_docs(cands, lambda c, s=s: c[s])
        out[f"{s}+bm25"] = order_docs(cands, lambda c, s=s: ws * c[s] + wl * c["lexical"]
                                      + wp * prior(c["bm25_rank"]))
        out[f"{s}+max"] = order_docs(cands, lambda c, s=s: ws * c[s] + wl * c["lexical"]
                                     + wp * prior(min(c["bm25_rank"], c["fused_rank"])))
    return out


def summarize(name: str, ranks: dict[str, int | None], cats: dict[str, list[str]],
              n: int) -> dict[str, Any]:
    vals = list(ranks.values())
    row: dict[str, Any] = {"variant": name}
    for k in (1, 3, 5, 8):
        row[f"R@{k}"] = sum(1 for r in vals if r and r <= k)
    row["MRR"] = round(sum(1 / r for r in vals if r) / n, 3)
    for c, members in cats.items():
        for k in (5, 8):
            row[f"{c}@{k}"] = f"{sum(1 for t in members if ranks[t] and ranks[t] <= k)}/" \
                              f"{len(members)}"
    return row


def pick(rows: list[dict[str, Any]], base: dict[str, Any]) -> dict[str, Any] | None:
    """Pre-registered: R@5 >= current + 5 and R@1 >= current; best R@5, then R@1, then cost."""
    ok = [r for r in rows if r["R@5"] >= base["R@5"] + 5 and r["R@1"] >= base["R@1"]]
    ok.sort(key=lambda r: (-r["R@5"], -r["R@1"], COST[r["variant"].split("_only")[0]
                                                   .split("+")[0]]))
    return ok[0] if ok else None


async def build(args: argparse.Namespace) -> dict[str, Any] | None:
    from rag.techqa.semantic import MiniLMEncoder

    import agents.chap12.cross_encoder as ce
    from agents.chap12.dense import SampleDenseRetriever
    from agents.chap12.rag_worker import doc_id
    from evaluation.chap12_e2_recall import HF, HFEncoder, model_dir
    from evaluation.chap12_recall_rerank_study import CachedOnlyReranker
    from tools.sample_retriever import SampleRetrieverTool

    root = args.root
    if args.device == "auto":
        import torch

        args.device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"device={args.device}", flush=True)
    data = root / ".rag_data"
    ce.model_dir = lambda choice: data / "models" / ce.MODELS[choice]  # local folders under root
    dense = SampleDenseRetriever(data / "chap12_tune.dense.sqlite",
                                 encoder=MiniLMEncoder(data / "models/minilm", batch_size=32,
                                                       device="cpu"))
    tool = SampleRetrieverTool(data / "chap12_tune.sqlite", rerank="lexical", dense=dense)
    nomic = CachedOnlyReranker(args.cache)
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    traces = [json.loads(x) for x in (RUN / "traces.jsonl").read_text("utf-8-sig").splitlines()
              if x.strip()]
    traces = [t for t in traces if gold[t["task_id"]].get("answerable") == "Y"]
    encoders: dict[str, Any] = {}
    for name in ("bge", "e5"):
        try:
            encoders[name] = HFEncoder(model_dir(root, name), HF[name]["pool"], args.device)
        except Exception as exc:
            print(f"SKIP {name}: {exc}", flush=True)
    crosses = {}
    for name in ("ce_minilm", "ce_bge"):
        try:
            ce.manifest(name)
            crosses[name] = ce.CrossEncoderReranker(name)
        except Exception as exc:
            print(f"SKIP {name}: {exc}", flush=True)
    # Resumable: one line per finished question in <scores>.partial.jsonl.
    partial = args.scores.with_suffix(".partial.jsonl")
    partial.parent.mkdir(parents=True, exist_ok=True)
    done = {json.loads(x)["task_id"]: json.loads(x) for x in partial.read_text("utf-8")
            .splitlines() if x.strip()} if partial.is_file() else {}
    started = time.time()
    for t in traces:
        if t["task_id"] in done:
            continue
        if args.max_seconds and time.time() - started > args.max_seconds:
            print(f"stopping after {time.time() - started:.0f}s; {len(done)}/{len(traces)} done",
                  flush=True)
            return None
        r = t["layers"]["retrieval"]
        query = r["query"]
        stages: dict[str, Any] = {}
        await tool.pipeline.retrieve(query, mode=tool.mode, filters=tool.secure_filters({}),
                                     trace=stages)
        cands_sr = list(stages["fusion"])
        docs = [doc_id(str(c.metadata.get("parent_id", ""))) for c in cands_sr]
        firsts = list(dict.fromkeys(docs))
        fusion_ok = firsts == [x["doc"] for x in r["stages"]["fusion"]]
        comps: dict[str, dict[str, float]] = {}
        await nomic.inner.rerank(query, cands_sr, limit=len(cands_sr), components=comps)
        cands = [{"doc": d, "fused_rank": i, "nomic": comps[c.chunk_id]["semantic_score"],
                  "lexical": comps[c.chunk_id]["lexical_score"],
                  "bm25_rank": comps[c.chunk_id]["bm25_document_rank"]}
                 for i, (c, d) in enumerate(zip(cands_sr, docs, strict=True), 1)]
        passages = [(str(c.metadata.get("context_summary", "")) + " " + c.text).strip()
                    for c in cands_sr]
        for name, enc in encoders.items():
            q = enc.encode([HF[name]["query"] + query])[0]
            p = enc.encode([HF[name]["doc"] + x for x in passages])
            for c, v in zip(cands, p @ q, strict=True):
                c[name] = float(v)
        for name, cross in crosses.items():
            for c, v in zip(cands, cross.score(query[:2000], passages), strict=True):
                c[name] = float(v)
        current = order_docs(cands, lambda c: 0.5 * c["nomic"] + 0.3 * c["lexical"]
                             + 0.2 * prior(c["bm25_rank"]))
        traced = [x["doc"] for x in r["stages"]["rerank"]]
        row = {"task_id": t["task_id"], "gold": gold[t["task_id"]]["document"],
               "fusion_identical": fusion_ok, "rerank_identical": current[:len(traced)] == traced,
               "semantic": ["nomic", *encoders, *crosses], "candidates": cands}
        with partial.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row) + "\n")
        done[t["task_id"]] = row
        print(f"{len(done)}/{len(traces)} questions, {time.time() - started:.0f}s", flush=True)
    tasks = [done[t["task_id"]] for t in traces]
    semantic = tasks[0]["semantic"]
    if any(t["semantic"] != semantic for t in tasks):
        raise ValueError("semantic terms differ between resumed parts")
    checks = {k: sum(t[k] for t in tasks) for k in ("fusion_identical", "rerank_identical")}
    return {"checks": checks, "semantic": semantic, "tasks": tasks}


def report(data: dict[str, Any], out: Path) -> None:
    tasks = data["tasks"]
    n = len(tasks)
    cats = {c: [t["task_id"] for t in tasks if int(t["task_id"].rsplit("-", 1)[1]) in ids]
            for c, ids in E1_CATEGORIES.items()}
    orders = {t["task_id"]: variants(t["candidates"], data["semantic"]) for t in tasks}
    names = list(next(iter(orders.values())))
    rows = []
    per_task = {t["task_id"]: {"task_id": t["task_id"], "gold": t["gold"], "ranks": {}}
                for t in tasks}
    for name in names:
        ranks = {}
        for t in tasks:
            o = orders[t["task_id"]][name]
            ranks[t["task_id"]] = o.index(t["gold"]) + 1 if t["gold"] in o else None
            per_task[t["task_id"]]["ranks"][name] = ranks[t["task_id"]]
        rows.append(summarize(name, ranks, cats, n))
    ceiling = sum(1 for t in tasks if any(c["doc"] == t["gold"] for c in t["candidates"]))
    base = next(r for r in rows if r["variant"] == "nomic+bm25")
    chosen = pick([r for r in rows if r["variant"] != "nomic+bm25"], base)
    summary = {"date": time.strftime("%F"), "questions": n, "ceiling_gold_in_candidates": ceiling,
               "checks": {k: f"{v}/{n}" for k, v in data["checks"].items()},
               "semantic_terms": data["semantic"], "results": rows,
               "rule": "R@5 >= current + 5 and R@1 >= current (current = nomic+bm25)",
               "candidate_for_e6": chosen["variant"] if chosen else None}
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False),
                                      encoding="utf-8")
    with (out / "per_task.jsonl").open("w", encoding="utf-8") as f:
        for row in per_task.values():
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    cols = ["R@1", "R@3", "R@5", "R@8", "MRR", "A@5", "B@5", "C@5", "D@5", "D@8"]
    lines = [f"# E3 重排对比（调参集 {n} 道可回答题，同一批候选 30 块，答案文档名次）", "",
             f"候选里有答案文档 {ceiling}/{n}（上限）。融合候选与 trace 一致 "
             f"{summary['checks']['fusion_identical']}；当前重排复现 trace "
             f"{summary['checks']['rerank_identical']}。R@k 为题数。", "",
             "| 变体 | " + " | ".join(cols) + " |", "|" + " --- |" * (len(cols) + 1)]
    lines += ["| " + r["variant"] + (" （当前）" if r["variant"] == "nomic+bm25" else "") + " | "
              + " | ".join(str(r[c]) for c in cols) + " |" for r in rows]
    lines += ["", f"事先登记规则：{summary['rule']} → 候选："
              f"{summary['candidate_for_e6'] or '无'}"]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="folder holding .rag_data")
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--scores", type=Path, default=OUT / "scores.json",
                        help="per-candidate scores; reused if present")
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--max-seconds", type=float, default=0,
                        help="stop starting new questions after this long (resume later)")
    args = parser.parse_args()
    if args.scores.is_file():
        data = json.loads(args.scores.read_text("utf-8"))
    else:
        data = asyncio.run(build(args))
        if data is None:
            return
        args.scores.parent.mkdir(parents=True, exist_ok=True)
        args.scores.write_text(json.dumps(data), encoding="utf-8")
    report(data, args.out)


if __name__ == "__main__":
    main()
