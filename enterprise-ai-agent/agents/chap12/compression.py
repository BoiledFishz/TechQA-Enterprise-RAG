"""E7 (2026-10-31): breadth-first evidence, one passage per document before any second passage.

E6's trace showed answer documents that reached the top 8 but not the model's evidence (L3):
in the round 9 configuration all 5 such cases and in the e5 run 4 of 8 had the gold document at
returned position 6-8 while the evidence already held two passages of earlier documents and hit
the 2400-token budget or the 8-source cap. Project 1's ContextCompressor walks the documents in
order and takes up to two passages from each. This subclass keeps every Project 1 rule (the
score filter, the three conflict filters, `aspect_passages(limit=2)`, the token budget and the
source cap) and changes only the ORDER of taking: first passage of every document, then second
passages, each pass in document order. Selected evidence is then put back in document order
and renumbered S1..Sn. Project 1 code is not modified.
"""

from __future__ import annotations

from rag.techqa.query import component_conflict, operation_conflict, requirement_error_conflict

from agents.rag_agent.compression import ContextCompressor
from agents.rag_agent.text import serialize_evidence, token_count
from models.schemas import CompressionResult, Document, Evidence


class BreadthFirstCompressor(ContextCompressor):
    def compress(self, query: str, candidates: list[Document]) -> CompressionResult:
        if not any(d.metadata.get("_full_parent") for d in candidates):
            return super().compress(query, candidates)
        from rag.techqa import evidence as p1_evidence
        from rag.techqa.settings import evidence_candidate_threshold, relevance_threshold

        candidates = [d for d in candidates if d.score >= (
            min(evidence_candidate_threshold(), float(
                d.metadata.get("_acceptance_threshold", relevance_threshold())))
            if self.model_selects_evidence else
            float(d.metadata.get("_acceptance_threshold", relevance_threshold())))]
        per_doc: list[list[Evidence]] = []
        for document in candidates:
            title = str(document.metadata.get("title", ""))
            if (operation_conflict(query, title, document.text)
                    or component_conflict(query, title)
                    or requirement_error_conflict(query, document.text)):
                per_doc.append([])
                continue
            per_doc.append([Evidence(
                source_id="S0", chunk_id=document.chunk_id, source_file=document.source_file,
                page_number=document.page_number, excerpt=p.text, title=title,
                applicability=document.text[:500], relevance=min(1, max(0, document.score)),
                tokens=token_count(p.text), section=p.section, start_char=p.start_char,
                end_char=p.end_char, covers=list(p.covers), instruction_group=p.instruction_group,
            ) for p in p1_evidence.aspect_passages(
                query, document.text, limit=2,
                retrieved_excerpt=str(document.metadata.get("_retrieved_excerpt", "")))])
        chosen: list[tuple[int, int, Evidence]] = []
        seen: set[str] = set()
        for rank in range(2):
            for d, passages in enumerate(per_doc):
                if rank >= len(passages) or len(chosen) >= self.max_sources:
                    continue
                ev = passages[rank]
                if ev.excerpt in seen:
                    continue
                trial = [e for _, _, e in chosen] + [ev]
                if token_count(serialize_evidence(trial)) > self.max_tokens:
                    continue
                chosen.append((d, rank, ev))
                seen.add(ev.excerpt)
        chosen.sort(key=lambda x: (x[0], x[1]))
        resolved = [e.model_copy(update={"source_id": f"S{i}"})
                    for i, (_, _, e) in enumerate(chosen, 1)]
        return CompressionResult(
            evidence=resolved,
            original_tokens=sum(token_count(d.text) for d in candidates),
            context_tokens=token_count(serialize_evidence(resolved)) if resolved else 0)
