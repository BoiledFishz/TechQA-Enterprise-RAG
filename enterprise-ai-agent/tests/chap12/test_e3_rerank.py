"""E3 helpers: candidate reordering variants and the pre-registered pick rule."""

from __future__ import annotations

from evaluation.chap12_e3_rerank import order_docs, pick, variants


def cand(doc: str, fused: int, sem: float, lex: float, bm25: float) -> dict[str, float | str]:
    return {"doc": doc, "fused_rank": fused, "nomic": sem, "lexical": lex, "bm25_rank": bm25}


def test_order_docs_keeps_first_chunk_per_document() -> None:
    cands = [cand("a", 1, 0.2, 0, 1), cand("b", 2, 0.9, 0, 1), cand("a", 3, 0.95, 0, 1)]
    assert order_docs(cands, lambda c: c["nomic"]) == ["a", "b"]


def test_max_prior_rescues_dense_only_candidate() -> None:
    cands = [cand("bm25hit", 2, 0.50, 0.5, 1), cand("denseonly", 1, 0.55, 0.5, 1000)]
    out = variants(cands, ["nomic"])
    assert out["fusion"] == ["denseonly", "bm25hit"]
    assert out["nomic+bm25"][0] == "bm25hit"
    assert out["nomic+max"][0] == "denseonly"


def test_pick_needs_five_more_at_r5_and_no_r1_loss() -> None:
    base = {"variant": "nomic+bm25", "R@1": 50, "R@5": 70}
    rows = [{"variant": "ce_bge+max", "R@1": 49, "R@5": 80},
            {"variant": "bge_only", "R@1": 50, "R@5": 75},
            {"variant": "e5+bm25", "R@1": 52, "R@5": 75}]
    assert pick(rows, base)["variant"] == "e5+bm25"
    assert pick([{"variant": "e5_only", "R@1": 60, "R@5": 74}], base) is None
