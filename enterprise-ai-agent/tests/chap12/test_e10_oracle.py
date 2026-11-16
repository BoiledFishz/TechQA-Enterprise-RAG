"""E10: oracle retrieval returns exactly the gold document, or nothing."""

from __future__ import annotations

import asyncio
from pathlib import Path

from agents.chap12 import tracing
from agents.chap12.oracle import ORACLE_DOC, OracleRetrieverTool
from models.schemas import RetrieverInput
from tests.chap12.conftest import fixture_docs


def test_oracle_returns_the_gold_document_only(sample_index: Path) -> None:
    gold = str(fixture_docs()[0]["id"])
    tool = OracleRetrieverTool(sample_index, rerank="lexical", use_dense=False)
    token = ORACLE_DOC.set(gold)
    try:
        with tracing.recording() as data:
            docs = asyncio.run(tool.invoke(RetrieverInput(query="anything at all", top_k=8)))
    finally:
        ORACLE_DOC.reset(token)
    assert [d.source_file for d in docs] == [f"techqa://{gold}"]
    assert docs[0].metadata["_full_parent"] is True and docs[0].score == 1.0
    assert data["retrieval"]["choice"] == "oracle"


def test_oracle_without_gold_returns_nothing(sample_index: Path) -> None:
    tool = OracleRetrieverTool(sample_index, rerank="lexical", use_dense=False)
    assert asyncio.run(tool.invoke(RetrieverInput(query="q", top_k=8))) == []
