"""E5 sampling: fixed strata sizes, deterministic, shuffled together."""

from __future__ import annotations

from evaluation.chap12_e5_review import SIZES, sample, strata


def test_strata_and_sample_are_deterministic() -> None:
    items = ([{"task_id": f"c{i}", "layer": "L4 generation: cited other"} for i in range(8)]
             + [{"task_id": f"u{i}", "layer": "L4 refusal: answered unanswerable"}
                for i in range(19)]
             + [{"task_id": f"k{i}", "layer": "correct", "answerable": True} for i in range(40)]
             + [{"task_id": "x", "layer": "correct", "answerable": True}])
    runs = {i["task_id"]: {"answer": "text"} for i in items if i["task_id"] != "x"}
    pools = strata(items, runs)
    assert "x" not in pools["control"]  # no published answer
    first, second = sample(pools), sample(pools)
    assert first == second and len(first) == sum(SIZES.values())
    assert sum(s == "unanswerable" for s, _ in first) == 16
    assert [s for s, _ in first[:8]] != ["cited_other"] * 8  # shuffled
