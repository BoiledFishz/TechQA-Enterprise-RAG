"""E4 drop-reason rules on hand-made traces."""

from __future__ import annotations

from typing import Any

from evaluation.chap12_e4_selection import auc, classify


def trace(returned: list[str], evidence: list[str], selected: list[str],
          rejected: dict[str, str] | None = None) -> dict[str, Any]:
    sids = {d: f"S{i}" for i, d in enumerate(evidence, 1)}
    return {"layers": {
        "retrieval": {"returned": [{"doc": d, "score": 0.7, "threshold": 0.65} for d in returned]},
        "rag": {"evidence": [{"doc": d, "source_id": sids[d]} for d in evidence],
                "cited": [], "status": "abstained", "context_tokens": 2300},
        "selector": {"selected": [sids[d] for d in selected], "decision": "ABSTAIN",
                     "judge": {"rejected": [{"source_id": sids[d], "rule": r}
                                            for d, r in (rejected or {}).items()]}}}}


def test_l3_budget_cut_vs_other() -> None:
    assert classify("L3 context", trace(["a", "b", "g"], ["a", "b"], []), "g", {})["reason"] \
        == "budget_cut"
    assert classify("L3 context", trace(["a", "b", "g", "c"], ["a", "c"], []), "g",
                    {})["reason"] == "other_context"


def test_l4_refused_reasons() -> None:
    f = "L4 generation: refused"
    assert classify(f, trace(["g"], ["g"], []), "g", {})["reason"] == "selector_selected_nothing"
    assert classify(f, trace(["g", "x"], ["g", "x"], ["x"], {"x": "J2"}), "g", {})["reason"] \
        == "selector_picked_other+judge_rejected_it"
    assert classify(f, trace(["g"], ["g"], ["g"], {"g": "J4"}), "g", {})["reason"] == "judge_J4"


def test_auc() -> None:
    assert auc([0.3, 0.2], [0.1, 0.0]) == 1.0
