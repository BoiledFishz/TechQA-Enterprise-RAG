"""E2 recall helpers: chunking parity with Project 1, document ranking, RRF, k for coverage."""

from __future__ import annotations

import numpy as np
from rag.techqa.retrieval import legacy_chunks

from evaluation.chap12_e2_recall import chunk_corpus, metrics, rank_docs, rrf, split


def test_split_1200_matches_project1_legacy_chunks() -> None:
    body = ("Paragraph one about WebSphere.\n\n" + "word " * 400 + "\nline\n" + "x. " * 500) * 3
    ours = split("A title", body, 1200, 160)
    theirs = [c.text for c in legacy_chunks({"title": "A title", "text": body, "id": "d1"})]
    assert ours == theirs


def test_head_chunking_is_one_chunk_per_document() -> None:
    owners, texts = chunk_corpus({"b": ("T2", "y" * 5000), "a": ("T1", "short")}, "head")
    assert owners == ["a", "b"]
    assert texts[0] == "T1\n\nshort" and len(texts[1]) == len("T2\n\n") + 1000


def test_rank_docs_uses_best_chunk_and_dedupes() -> None:
    vectors = np.array([[1, 0], [0.9, 0.1], [0, 1], [0.95, 0]], dtype="float32")
    owners = ["d1", "d1", "d2", "d3"]
    assert rank_docs(np.array([1, 0], dtype="float32"), vectors, owners) == ["d1", "d3", "d2"]


def test_rrf_and_metrics() -> None:
    assert rrf(["a", "b"], ["b", "c"])[0] == "b"
    out = metrics([1, 2, None, 30], 4)
    assert out["R@1"] == 0.25 and out["R@30"] == 0.75
    assert out["k85"] == ">100"
    assert metrics([1, 3, 5, 7], 4)["k85"] == 7
