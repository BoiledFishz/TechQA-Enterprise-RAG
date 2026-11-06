"""Answer document in the model's evidence, but the selection did not pick it (2026-11-06).

    python -m evaluation.chap12_selection_misses --index PATH/chap12_tune.sqlite RUN [RUN...]

Reads traces only (no model calls). For every answerable question whose gold document is among
the evidence the model saw but not among the sources the selection picked, lists the question,
the gold document (title, evidence position), what was picked instead (titles), the judge's
decision, the published answer's opening, and the refusal diagnostic if any. Also marks the
questions missed in every listed run. Writes results/chap12/selection_misses/{cases.md,cases.json}.
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
    cases: dict[str, dict[str, object]] = {}
    for run in args.runs:
        answers = {r["task_id"]: r for r in map(json.loads, (RESULTS / run / "runs.jsonl")
                                                .read_text("utf-8-sig").splitlines()) if r}
        for line in (RESULTS / run / "traces.jsonl").read_text("utf-8-sig").splitlines():
            if not line.strip():
                continue
            t = json.loads(line)
            tid, layers = t["task_id"], t["layers"]
            if gold[tid].get("answerable") != "Y" or not layers.get("rag"):
                continue
            g = gold[tid]["document"]
            ev = layers["rag"].get("evidence", [])
            by_sid = {e["source_id"]: e["doc"] for e in ev}
            if g not in by_sid.values():
                continue
            sel = layers.get("selector") or {}
            picked = [by_sid.get(s, s) for s in sel.get("selected", [])]
            if g in picked:
                continue
            pos = next(e["source_id"] for e in ev if e["doc"] == g)
            case = cases.setdefault(tid, {
                "task_id": tid, "question": " ".join(tasks[tid]["query"].split())[:400],
                "gold": g, "gold_title": titles.get(g, ""), "runs": {}})
            case["runs"][run] = {  # type: ignore[index]
                "gold_source": pos, "picked": [f"{d} {titles.get(d, '')}" for d in picked],
                "judge": (sel.get("judge") or {}).get("decision"),
                "refusal_reason": sel.get("refusal_reason"),
                "correct": t["score"].get("correct"),
                "answer": " ".join(str(answers.get(tid, {}).get("answer") or "").split())[:300]}
    out = RESULTS / "selection_misses"
    out.mkdir(parents=True, exist_ok=True)
    rows = sorted(cases.values(), key=lambda c: (-len(c["runs"]), c["task_id"]))  # type: ignore[arg-type]
    (out / "cases.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), "utf-8")
    md = [f"# 答案文档在证据里、选证据却没选中（{', '.join(args.runs)}）", "",
          f"共 {len(rows)} 道；在全部 {len(args.runs)} 个运行里都没选中："
          f"{sum(len(c['runs']) == len(args.runs) for c in rows)} 道。", ""]  # type: ignore[arg-type]
    for c in rows:
        md += [f"## {c['task_id']}（{len(c['runs'])}/{len(args.runs)} 个运行）", "",  # type: ignore[arg-type]
               f"- 问题：{c['question']}", f"- 答案文档：{c['gold']} {c['gold_title']}"]
        for run, r in c["runs"].items():  # type: ignore[union-attr]
            picked = r["picked"] or "（一篇不选）"
            md += [f"- **{run}**：答案文档在 {r['gold_source']}；选了 {picked}；"
                   f"判断 {r['judge']}；{'答对' if r['correct'] else '答错'}",
                   f"  - 回答开头：{r['answer'][:200] or '（无）'}"]
            if r["refusal_reason"]:
                md.append(f"  - 拒答理由：{r['refusal_reason'][:250]}")
        md.append("")
    (out / "cases.md").write_text("\n".join(md), "utf-8")
    print(len(rows))


if __name__ == "__main__":
    main()
