"""E7: breadth-first evidence keeps Project 1's rules and changes only the taking order."""

from __future__ import annotations

from typing import Any

import pytest
from rag.techqa import evidence as p1_evidence
from rag.techqa.evidence import Passage

from agents.chap12 import factory
from agents.chap12.compression import BreadthFirstCompressor
from agents.rag_agent.compression import ContextCompressor
from models.schemas import Document


def docs(n: int) -> list[Document]:
    return [Document(chunk_id=f"c{i}", text=f"document {i} body", source_file=f"techqa://d{i}",
                     score=0.9, metadata={"_full_parent": True, "title": f"Title {i}"})
            for i in range(1, n + 1)]


@pytest.fixture
def two_passages(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake(query: str, text: str, **kwargs: Any) -> list[Passage]:
        d = text.split()[1]
        return [Passage(f"doc {d} passage one " + "x " * 40, 1.0),
                Passage(f"doc {d} passage two " + "y " * 40, 0.9)]
    monkeypatch.setattr(p1_evidence, "aspect_passages", fake)


def test_cap_reached_depth_first_drops_later_documents(two_passages: None) -> None:
    depth = ContextCompressor(100000, 8, model_selects_evidence=True).compress("q", docs(6))
    breadth = BreadthFirstCompressor(100000, 8, model_selects_evidence=True).compress("q", docs(6))
    assert {e.source_file for e in depth.evidence} == {f"techqa://d{i}" for i in range(1, 5)}
    assert {e.source_file for e in breadth.evidence} == {f"techqa://d{i}" for i in range(1, 7)}
    assert len(breadth.evidence) == 8
    # back in document order and renumbered
    assert [e.source_id for e in breadth.evidence] == [f"S{i}" for i in range(1, 9)]
    files = [e.source_file for e in breadth.evidence]
    assert files == sorted(files, key=lambda f: int(f[-1]))


def test_same_evidence_when_nothing_is_dropped(two_passages: None) -> None:
    depth = ContextCompressor(100000, 8, model_selects_evidence=True).compress("q", docs(3))
    breadth = BreadthFirstCompressor(100000, 8, model_selects_evidence=True).compress("q", docs(3))
    assert [e.model_dump() for e in depth.evidence] == [e.model_dump() for e in breadth.evidence]


def test_order_is_selected_by_env_or_tuned_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CHAP12_EVIDENCE_ORDER", "breadth")
    assert factory.evidence_order(True) == "breadth"
    monkeypatch.delenv("CHAP12_EVIDENCE_ORDER")
    monkeypatch.setattr(factory, "tuned_config", lambda: {})
    assert factory.evidence_order(True) == "depth"
