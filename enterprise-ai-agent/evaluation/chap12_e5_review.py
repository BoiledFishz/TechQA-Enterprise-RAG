"""E5: blind human review of 30 published answers (2026-10-26).

    python -m evaluation.chap12_e5_review build --index PATH/chap12_tune.sqlite \
        --items OUT/items.json --key KEY.json
    python -m evaluation.chap12_e5_review analyze --key KEY.json --reviews REVIEWS.json

Answers come from the current configuration on the TUNE split
(results/chap12/tune_real_r9_judged14). Seed 20261026. Strata (the reviewer never sees them):
  cited_other   all 8 answerable questions whose answer cites a document other than the gold one
  unanswerable  16 of the 19 unanswerable questions that were answered (random)
  control       6 answerable questions graded correct (random)
Items are shuffled together. Each item shows the question, the published answer and the full text
of the documents it cites; no gold answer, gold document, score or stratum. The key (item -> task,
stratum, gold) is written separately and kept out of git until the review is done; its SHA-256 is
recorded in tasks.md beforehand.

Per item the reviewer answers: answers the question (yes / partial / no); supported by the cited
documents (yes / partial / no); product and version match the question (match / mismatch /
unclear); overall acceptable as a support reply (acceptable / not acceptable) - the primary
judgement. `analyze` reports acceptable counts per stratum (and agreement if several reviewers).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_judged14"
SEED = 20261026
SIZES = {"cited_other": 8, "unanswerable": 16, "control": 6}
DOC_CHARS = 6000


def strata(items: list[dict[str, Any]], runs: dict[str, dict[str, Any]]
           ) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {k: [] for k in SIZES}
    for i in items:
        tid = i["task_id"]
        if not runs.get(tid, {}).get("answer"):
            continue
        if i["layer"] == "L4 generation: cited other":
            out["cited_other"].append(tid)
        elif i["layer"].startswith("L4 refusal: answered"):
            out["unanswerable"].append(tid)
        elif i["layer"] == "correct" and i.get("answerable"):
            out["control"].append(tid)
    return out


def sample(pools: dict[str, list[str]], seed: int = SEED) -> list[tuple[str, str]]:
    rng = random.Random(seed)
    chosen = []
    for name, size in SIZES.items():
        pool = sorted(pools[name])
        picked = pool if len(pool) <= size else sorted(rng.sample(pool, size))
        chosen += [(name, t) for t in picked]
    rng.shuffle(chosen)
    return chosen


def build(args: argparse.Namespace) -> None:
    db = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    docs = {d: (t, x) for d, t, x in db.execute("SELECT doc_id, title, text FROM docs")}
    tasks = {t["task_id"]: t for t in map(json.loads, (HERE / "chap12/tune/mixed_tasks.jsonl")
                                          .read_text("utf-8").splitlines())}
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    runs = {r["task_id"]: r for r in map(json.loads, (RUN / "runs.jsonl")
                                         .read_text("utf-8-sig").splitlines()) if r}
    attribution = json.loads((RUN / "layer_attribution.json").read_text("utf-8-sig"))["items"]
    chosen = sample(strata(attribution, runs))
    items, key = [], []
    for n, (stratum, tid) in enumerate(chosen, 1):
        item_id = f"R{n:02d}"
        cited = list(dict.fromkeys(runs[tid].get("cited") or []))
        items.append({"id": item_id, "question": tasks[tid]["query"].strip(),
                      "answer": runs[tid]["answer"].strip(),
                      "documents": [{"doc": d, "title": docs.get(d, ("?", ""))[0],
                                     "text": docs.get(d, ("", ""))[1][:DOC_CHARS],
                                     "truncated": len(docs.get(d, ("", ""))[1]) > DOC_CHARS}
                                    for d in cited]})
        key.append({"id": item_id, "task_id": tid, "stratum": stratum,
                    "gold": gold[tid].get("document"), "cited": cited})
    args.items.parent.mkdir(parents=True, exist_ok=True)
    args.items.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    raw = json.dumps(key, indent=1).encode("utf-8")
    args.key.write_bytes(raw)
    print(json.dumps({"items": len(items), "strata": Counter(k["stratum"] for k in key),
                      "key_sha256": hashlib.sha256(raw).hexdigest()}, indent=1))


def analyze(args: argparse.Namespace) -> None:
    key = {k["id"]: k for k in json.loads(args.key.read_text("utf-8"))}
    reviews = json.loads(args.reviews.read_text("utf-8"))  # {reviewer: {item: {...}}}
    out: dict[str, Any] = {"reviewers": len(reviews), "per_reviewer": {}}
    for reviewer, marks in reviews.items():
        table: dict[str, Counter[str]] = defaultdict(Counter)
        for item, m in marks.items():
            table[key[item]["stratum"]][m.get("overall", "missing")] += 1
        out["per_reviewer"][reviewer] = {s: dict(c) for s, c in table.items()}
    if len(reviews) >= 2:
        names = sorted(reviews)
        a, b = reviews[names[0]], reviews[names[1]]
        both = [i for i in a if i in b and a[i].get("overall") and b[i].get("overall")]
        out["agreement_overall"] = f"{sum(a[i]['overall'] == b[i]['overall'] for i in both)}" \
                                   f"/{len(both)}"
    print(json.dumps(out, indent=1, ensure_ascii=False))
    if args.out:
        args.out.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--index", type=Path, required=True)
    b.add_argument("--items", type=Path, required=True)
    b.add_argument("--key", type=Path, required=True)
    a = sub.add_parser("analyze")
    a.add_argument("--key", type=Path, required=True)
    a.add_argument("--reviews", type=Path, required=True)
    a.add_argument("--out", type=Path)
    args = parser.parse_args()
    build(args) if args.cmd == "build" else analyze(args)


if __name__ == "__main__":
    main()
