"""E10 (2026-11-16): oracle retrieval - hand the model the gold document, skip retrieval.

The teacher's question: if retrieval were perfect, how well do the models answer? With
CHAP12_ORACLE=1 the evaluation sets ORACLE_DOC to the task's gold document before each task, and
this retriever returns exactly that document (full parent text, as the live retriever does), with
score 1.0 and acceptance threshold 0, so it always reaches the evidence step. Evidence passage
choice, selection, judge and Critic run unchanged - the system's answer is quoted from the
evidence it selects, so "answering" is selecting and judging. Unanswerable tasks have no gold
document: the retriever returns nothing and the agent abstains; oracle runs are read on the 112
answerable tasks only. Evaluation only; never enabled in the live system.
"""

from __future__ import annotations

from contextvars import ContextVar
from typing import Any

from agents.chap12.rag_worker import doc_id
from models.schemas import Document, RetrieverInput
from tools.sample_retriever import SampleRetrieverTool

ORACLE_DOC: ContextVar[str | None] = ContextVar("chap12_oracle_doc", default=None)


class OracleRetrieverTool(SampleRetrieverTool):
    async def invoke(self, request: RetrieverInput) -> list[Document]:
        from agents.chap12 import tracing

        gold = ORACLE_DOC.get()
        output: list[Document] = []
        if gold:
            for p in await self.parents.retrieve_by_chunk_ids([f"techqa:{gold}:parent"]):
                output.append(Document(
                    chunk_id=p.chunk_id, text=p.text, source_file=p.source_file,
                    page_number=p.page_number, score=1.0,
                    metadata={**p.metadata, "_full_parent": True,
                              "_acceptance_threshold": 0.0, "_retrieved_excerpt": ""}))
        if tracing.active() is not None:
            stage: list[dict[str, Any]] = [
                {"doc": doc_id(d.source_file), "rank": 1, "score": 1.0} for d in output]
            tracing.record("retrieval", {
                "query": request.query, "top_k": request.top_k, "choice": "oracle",
                "reranker_fallback": False, "refusal_gate_refused": False,
                "stages": {"rerank": stage, "final": stage},
                "returned": [{"doc": doc_id(d.source_file), "score": 1.0, "threshold": 0.0}
                             for d in output]})
        return output
