"""Round 10 (2026-10-24): rerank prior from the fused (RRF) rank instead of the BM25 rank.

The Project 1 reranker scores 0.5 semantic + 0.3 lexical + 0.2 * 1 / (1 + BM25_rank / 5), and a
candidate that only the dense retriever found gets BM25 rank 1000 (prior about 0.005). The
offline study (results/chap12/recall_rerank_study.json) found 13 of the 22 gold documents pushed
out of the top 8 were such dense-only hits, usually with a higher semantic score than the 8th
document. This subclass hands the Project 1 reranker each candidate's position in the fused list
as its rank, so the prior rewards documents that either retriever ranked well. Semantic and
lexical scores, weights, caching and metering are unchanged; Project 1 is not modified.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

from rag.retrieval.contracts import SearchResult

from agents.chap12.metered import CountingReranker


class FusedPriorReranker(CountingReranker):
    # "fused" (round 10): rank = fused position. "max" (round 11): the better of the BM25 rank
    # and the fused position, i.e. the larger of the two priors (the prior falls with rank).
    mode = "fused"

    async def rerank(self, query: str, candidates: list[SearchResult], *, limit: int = 20,
                     components: dict[str, dict[str, float]] | None = None
                     ) -> list[SearchResult]:
        # Candidates arrive in fused (RRF) order from the pipeline; rank = position.
        ranked: list[Any] = [replace(c, metadata={**c.metadata, "bm25_document_rank": (
            i if self.mode == "fused"
            else min(i, int(c.metadata.get("bm25_document_rank", 1000))))})
            for i, c in enumerate(candidates, 1)]
        result: list[SearchResult] = await super().rerank(query, ranked, limit=limit,
                                                          components=components)
        return result


class MaxPriorReranker(FusedPriorReranker):
    """Round 11 (2026-10-24): prior = max(BM25-rank prior, fused-rank prior).

    Offline on the tune split (results/chap12/prior_study.json, candidate_k 30) it was at least
    as good as the Project 1 prior at every cut (R@1 0.473 -> 0.482, R@3 0.589 -> 0.607,
    R@8 0.661 -> 0.696), unlike the pure fused prior (R@1 0.393)."""

    mode = "max"
