"""E6 (2026-10-30): order candidates by e5-base-v2 cosine, accept by the nomic score.

E3 (results/chap12/e3_rerank) found that ordering the same 30 fused candidates by e5-base-v2
cosine alone ("e5_only") ranks the gold document higher than the current Project 1 formula
(R@5 69 -> 76, R@1 53 -> 54, tune split). E5Reranker reproduces that scoring for the live
pipeline: query "query: " + rewritten query, passage "passage: " + title + " " + chunk text,
512-token windows (stride 64) mean-pooled, cosine. It is used only for ORDER through the round 4
OrderOnlyReranker, so acceptance still uses the nomic score and its calibrated threshold.

The model is loaded only from `.rag_data/models/e2_e5/` (downloaded by E2, resolved commit in
e2_manifest.json); nothing is downloaded at runtime. Project 1 code is not modified.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Callable, Sequence
from dataclasses import replace
from pathlib import Path
from typing import Any

from rag.retrieval.contracts import SearchResult
from rag.techqa.data import ROOT

QUERY, PASSAGE = "query: ", "passage: "


def model_dir() -> Path:
    return ROOT / ".rag_data/models/e2_e5"


def manifest() -> dict[str, Any]:
    path = model_dir() / "e2_manifest.json"
    if not path.is_file():
        raise FileNotFoundError(f"{path} missing; run .chap12_run/run_e2.cmd (download) first")
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


class E5Reranker:
    def __init__(self, scorer: Callable[[str, Sequence[str]], list[float]] | None = None
                 ) -> None:
        self.identity = manifest() if scorer is None else {"repo": "test"}
        self._scorer = scorer  # injectable for tests
        self._encoder: Any = None

    def score(self, query: str, passages: Sequence[str]) -> list[float]:
        if self._scorer is not None:
            return list(self._scorer(query, passages))
        if self._encoder is None:
            import torch

            from evaluation.chap12_e2_recall import HFEncoder

            device = "cuda" if torch.cuda.is_available() else "cpu"
            self._encoder = HFEncoder(model_dir(), "mean", device)
        q = self._encoder.encode([QUERY + query])[0]
        p = self._encoder.encode([PASSAGE + x for x in passages])
        return [float(v) for v in p @ q]

    async def rerank(self, query: str, candidates: list[SearchResult], *,
                     limit: int = 20) -> list[SearchResult]:
        from agents.chap12.budget import charge

        if not candidates or limit <= 0:
            return []
        charge("local")
        passages = [(str(c.metadata.get("context_summary", "")) + " " + c.text).strip()
                    for c in candidates]
        scores = await asyncio.to_thread(self.score, query, passages)
        ranked = [replace(c, score=s, rerank_score=s, backend=c.backend + "+e5")
                  for c, s in zip(candidates, scores, strict=True)]
        ranked.sort(key=lambda r: r.score, reverse=True)
        return [replace(r, rerank_rank=rank) for rank, r in enumerate(ranked[:limit], 1)]
