"""E6: e5 order with nomic acceptance, and the 14B fallback when the selection picks nothing."""

from __future__ import annotations

import asyncio
from typing import Any

from rag.retrieval.contracts import SearchResult

from agents.chap12 import tracing
from agents.chap12.bi_encoder import E5Reranker
from agents.chap12.budget import Budget, BudgetLimits, metered
from agents.chap12.cross_encoder import OrderOnlyReranker
from agents.chap12.judged_selector import JudgedSelector
from tests.chap12.test_judged_selector import EVIDENCE, Model, judge


def candidate(n: int, text: str) -> SearchResult:
    return SearchResult(text=text, metadata={"chunk_id": f"c{n}", "context_summary": f"T{n}"},
                        score=0.0, backend="hybrid")


def overlap(query: str, passages: Any) -> list[float]:
    words = set(query.lower().split())
    return [len(words & set(p.lower().split())) / 10 for p in passages]


class FixedNomic:
    async def rerank(self, query: str, candidates: list[SearchResult], *,
                     limit: int = 20) -> list[SearchResult]:
        from dataclasses import replace
        return [replace(c, score=0.5 + i / 100) for i, c in enumerate(candidates)][:limit]


def test_e5_orders_and_nomic_score_is_kept_for_acceptance() -> None:
    items = [candidate(1, "unrelated"), candidate(2, "jobs environment variables"),
             candidate(3, "environment")]
    reranker = OrderOnlyReranker(FixedNomic(), E5Reranker(scorer=overlap))
    budget = Budget(BudgetLimits())
    with metered(budget, "rag"):
        ranked = asyncio.run(reranker.rerank("jobs environment variables", items, limit=3))
    assert [r.metadata["chunk_id"] for r in ranked] == ["c2", "c3", "c1"]
    assert [r.score for r in ranked] == [0.51, 0.52, 0.5]  # nomic scores, e5 order


def run(selector: JudgedSelector) -> Any:
    with tracing.recording() as data:
        draft = asyncio.run(selector.select("Fix for X?", EVIDENCE))
    return draft, data


def test_fallback_runs_only_when_the_selection_is_empty() -> None:
    small, big = Model([], judge("ANSWER")), Model(["S2"], judge("ANSWER"))
    draft, data = run(JudgedSelector(small, judge_model=big, fallback_model=big,
                                     fallback_name="14b"))
    assert [q.source_id for q in draft.quotes] == ["S2"]
    assert data["selector"]["fallback"] is True and "judge" in big.kinds

    small, big = Model(["S1"], judge("ANSWER")), Model(["S3"], judge("ANSWER"))
    draft, data = run(JudgedSelector(small, judge_model=big, fallback_model=big))
    assert [q.source_id for q in draft.quotes] == ["S1"]
    assert data["selector"]["fallback"] is False and "select" not in big.kinds


def test_no_fallback_keeps_round9_behaviour() -> None:
    draft, data = run(JudgedSelector(Model([], judge("ANSWER"))))
    assert draft.quotes == [] and data["selector"]["fallback"] is False
