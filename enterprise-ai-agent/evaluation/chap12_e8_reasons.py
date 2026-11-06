"""E8: collect the reasons the models gave for refusing (2026-11-05; reads traces only).

    python -m evaluation.chap12_e8_reasons --index PATH/chap12_tune.sqlite RUN [RUN...]

For each run, every question where the 14B judge vetoed a source (with its v2 reason) or the
selection picked nothing (with the refusal-diagnostic reason), listed with the question, whether
it is answerable, the gold document, the vetoed source's document and title, and whether that
vetoed document IS the gold one. Writes results/chap12/<run>/reasons.md and reasons.json.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results/chap12"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--index", type=Path, required=True)
    p.add_argument("runs", nargs="+")
    args = p.parse_args()
    db = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    titles = dict(db.execute("SELECT doc_id, title FROM docs"))
    tasks = {t["task_id"]: t for t in map(json.loads, (HERE / "chap12/tune/mixed_tasks.jsonl")
                                          .read_text("utf-8").splitlines())}
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    for run in args.runs:
        rows = []
        for line in (RESULTS / run / "traces.jsonl").read_text("utf-8-sig").splitlines():
            if not line.strip():
                continue
            t = json.loads(line)
            layers, tid = t["layers"], t["task_id"]
            sel = layers.get("selector") or {}
            by_sid = {e["source_id"]: e["doc"] for e in layers["rag"].get("evidence", [])}
            g = gold[tid].get("document") if gold[tid].get("answerable") == "Y" else None
            base = {"task_id": tid, "answerable": g is not None, "correct": t["score"].get(
                "correct"), "question": " ".join(tasks[tid]["query"].split())[:300],
                "gold": g, "gold_title": titles.get(g or "", ""),
                "gold_in_evidence": g in by_sid.values()}
            for r in (sel.get("judge") or {}).get("rejected", []):
                d = by_sid.get(r["source_id"], "?")
                rows.append(base | {"kind": "judge_veto", "rule": r["rule"],
                                    "reason": r.get("reason", ""), "doc": d,
                                    "doc_title": titles.get(d, ""), "doc_is_gold": d == g})
            if not sel.get("selected") and sel.get("refusal_reason"):
                rows.append(base | {"kind": "selection_empty", "rule": "",
                                    "reason": sel["refusal_reason"], "doc": "",
                                    "doc_title": "", "doc_is_gold": False})
        out = RESULTS / run
        (out / "reasons.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False),
                                          encoding="utf-8")
        md = [f"# {run}: refusal reasons ({len(rows)})", ""]
        for r in rows:
            md += [f"## {r['task_id']} - {r['kind']} {r['rule']} - "
                   f"{'answerable' if r['answerable'] else 'unanswerable'}, "
                   f"{'correct' if r['correct'] else 'wrong'}", "",
                   f"- Q: {r['question']}",
                   f"- gold: {r['gold']} {r['gold_title']} (in evidence: {r['gold_in_evidence']})",
                   f"- vetoed: {r['doc']} {r['doc_title']} (is gold: {r['doc_is_gold']})",
                   f"- reason: {r['reason']}", ""]
        (out / "reasons.md").write_text("\n".join(md), encoding="utf-8")
        print(run, len(rows))


if __name__ == "__main__":
    main()
