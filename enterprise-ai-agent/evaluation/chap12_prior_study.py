"""Offline comparison of rerank-prior variants by gold-document rank (2026-10-24, diagnosis).

    python -m evaluation.chap12_prior_study --cache PATH/techqa_rerank_cache.sqlite

Round 10 showed that the fused-rank prior lifts gold documents into the top 8 (R@8 0.661 ->
0.714) but lowers R@1 (0.473 -> 0.375), and documents ranked 5-8 often fall outside the model's
context. This compares, on the same rebuilt candidates of tune_real_r9_base (rewritten queries,
candidate_k 30 and 50) and the cached nomic vectors, the gold document's rank under:
  bm25      Project 1: prior from the BM25 rank (dense-only hits = rank 1000)
  fused     prior from the fused rank (round 10)
  max       the larger of the two priors
  missing   BM25 prior when the document is in the BM25 list, fused-rank prior otherwise
Reports R@1/3/5/8 over the 112 answerable questions. Writes results/chap12/prior_study.json.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import replace
from pathlib import Path
from typing import Any

from rag.techqa.data import ROOT

from evaluation.chap12_recall_rerank_study import CachedOnlyReranker, doc_rank

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_base"
CUTS = (1, 3, 5, 8)


def prior(x: dict[str, float], fused_rank: int, variant: str) -> float:
    fused = 1 / (1 + fused_rank / 5)
    bm25 = x["bm25_prior"]
    return {"bm25": bm25, "fused": fused, "max": max(bm25, fused),
            "missing": fused if x["bm25_document_rank"] >= 1000 else bm25}[variant]


async def main_async(args: argparse.Namespace) -> None:
    from tools.sample_retriever import SampleRetrieverTool

    tool = SampleRetrieverTool(ROOT / ".rag_data/chap12_tune.sqlite", rerank="lexical")
    config = tool.pipeline.config
    reranker = CachedOnlyReranker(args.cache)
    gold = {g["task_id"]: g.get("document") for g in map(
        json.loads, (HERE / "chap12/tune/mixed_gold.jsonl").read_text("utf-8").splitlines())}
    rows = [json.loads(x) for x in (RUN / "traces.jsonl").read_text("utf-8-sig").splitlines()
            if x.strip()]
    rows = [r for r in rows if r["score"].get("answerable") and r["layers"].get("retrieval")]
    hits: dict[str, dict[int, int]] = {}
    missing = {30: 0, 50: 0}
    for r in rows:
        query, g = r["layers"]["retrieval"]["query"], gold[r["task_id"]]
        for k in (30, 50):
            tool.pipeline.config = replace(config, candidate_k=k)
            stages: dict[str, Any] = {}
            await tool.pipeline.retrieve(query, mode=tool.mode, filters=tool.secure_filters({}),
                                         trace=stages)
            cands = list(stages["fusion"])
            comps: dict[str, dict[str, float]] = {}
            try:
                await reranker.inner.rerank(query, cands, limit=len(cands), components=comps)
            except KeyError:
                missing[k] += 1
                continue
            for variant in ("bm25", "fused", "max", "missing"):
                order = doc_rank(sorted(cands, key=lambda c, v=variant: (
                    0.5 * comps[c.chunk_id]["semantic_score"]
                    + 0.3 * comps[c.chunk_id]["lexical_score"]
                    + 0.2 * prior(comps[c.chunk_id], cands.index(c) + 1, v)), reverse=True))
                bucket = hits.setdefault(f"{variant}@{k}", {n: 0 for n in CUTS})
                for n in CUTS:
                    bucket[n] += g in order[:n]
    tool.pipeline.config = config
    total = len(rows)
    out = {"tasks": total, "missing_vectors": missing,
           "recall": {name: {f"R@{n}": round(v / total, 3) for n, v in b.items()}
                      for name, b in hits.items()}}
    (HERE / "results/chap12/prior_study.json").write_text(json.dumps(out, indent=1) + "\n",
                                                          encoding="utf-8")
    print(json.dumps(out, indent=1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, required=True)
    asyncio.run(main_async(parser.parse_args()))


if __name__ == "__main__":
    main()
