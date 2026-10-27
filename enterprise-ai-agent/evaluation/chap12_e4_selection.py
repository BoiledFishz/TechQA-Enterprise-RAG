"""E4: after retrieval, where does the gold document get lost? (2026-10-26; diagnosis, no LLM)

    python -m evaluation.chap12_e4_selection --index PATH/chap12_tune.sqlite

Replays, from the recorded trace of the current configuration on the TUNE split
(results/chap12/tune_real_r9_judged14), every decision between "the retriever returned the gold
document" and the published answer, and assigns each loss a drop reason:
  L3 (returned, not in the model's evidence)
    budget_cut       every document returned before the gold one is in the evidence and the
                     gold one is not: the evidence (max_context_tokens) filled up first
    other_context    the evidence also skipped documents returned before the gold one (passage
                     selection inside the budget, not a plain cut-off)
  L4 refused (gold in evidence, model abstained)
    selector_selected_nothing  the 7B selection (Project 1 ANSWERABILITY_SELECT) picked nothing
    selector_picked_other      it picked other sources only (+judge_rejected_it if the 14B
                               judge then rejected those)
    judge_<rule>     the selection picked it and the 14B judge rejected it (J1-J4)
    after_selection  picked and not rejected, but the RAG worker still did not answer
  L4 cited other (gold in evidence, answer cites another document)
    gold_not_selected / gold_selected_too, and whether a cited document looks like a near
    duplicate of the gold (title word Jaccard >= 0.5)
  Unanswerable questions that were answered: selection size, judge rejections, top score margin.
Also: the separation of the top rerank score (minus its threshold) between answerable questions
answered correctly and unanswerable questions (would a hard score gate help?), as AUC and the
best single cut on this split (descriptive; nothing is selected here).
Writes results/chap12/e4_selection/{cases.json,cases.md,summary.md}.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_judged14"
OUT = HERE / "results/chap12/e4_selection"
WORD = re.compile(r"[a-z0-9][a-z0-9_.\-]{2,}")
STOP = set("the and for with from that this when what how are was were not can does have has "
           "you your use using ibm united states".split())


def words(text: str) -> set[str]:
    return {w for w in WORD.findall(text.lower()) if w not in STOP}


def jaccard(a: str, b: str) -> float:
    x, y = words(a), words(b)
    return len(x & y) / max(len(x | y), 1)


def classify(layer: str, trace: dict[str, Any], gold: str | None,
             titles: dict[str, str]) -> dict[str, Any]:
    L = trace["layers"]
    returned = [x["doc"] for x in L["retrieval"]["returned"]]
    evidence = L["rag"].get("evidence", [])
    by_sid = {e["source_id"]: e["doc"] for e in evidence}
    sel = L.get("selector") or {}
    selected = [by_sid.get(s, s) for s in sel.get("selected", [])]
    judge = sel.get("judge") or {}
    rejected = {by_sid.get(r["source_id"], r["source_id"]): r.get("rule")
                for r in judge.get("rejected", [])}
    gold_sid = next((e["source_id"] for e in evidence if e["doc"] == gold), None)
    top = L["retrieval"]["returned"][0] if L["retrieval"]["returned"] else {}
    info: dict[str, Any] = {
        "returned_n": len(returned), "evidence_n": len(evidence),
        "context_tokens": L["rag"].get("context_tokens"),
        "gold_returned_pos": returned.index(gold) + 1 if gold in returned else None,
        "gold_source": gold_sid, "selected": selected,
        "selection_decision": sel.get("decision"), "judge_decision": judge.get("decision"),
        "judge_rejected": rejected, "cited": L["rag"].get("cited", []),
        "rag_status": L["rag"].get("status"),
        "top_score_margin": round(top["score"] - top["threshold"], 4) if top.get(
            "threshold") is not None else None,
    }
    reason = "-"
    if layer.startswith("L3"):
        # Evidence holds passages; several can come from one document.
        ev_docs = list(dict.fromkeys(e["doc"] for e in evidence))
        before = returned[:(info["gold_returned_pos"] or 1) - 1]
        reason = "budget_cut" if all(d in ev_docs for d in before) else "other_context"
        info["evidence_docs"] = len(ev_docs)
    elif layer.startswith("L4 generation: refused"):
        if not selected:
            reason = "selector_selected_nothing"
        elif gold not in selected:
            reason = "selector_picked_other" + ("+judge_rejected_it" if rejected else "")
        elif gold in rejected:
            reason = f"judge_{rejected[gold]}"
        else:
            reason = "after_selection"
    elif layer.startswith("L4 generation: cited"):
        near = max((jaccard(titles.get(c, ""), titles.get(gold or "", ""))
                    for c in info["cited"]), default=0.0)
        reason = ("gold_selected_too" if gold in selected else "gold_not_selected") + \
            ("+near_duplicate" if near >= 0.5 else "")
        info["cited_title_jaccard"] = round(near, 2)
    elif layer.startswith("L4 refusal"):
        reason = "answered_unanswerable"
    info["reason"] = reason
    return info


def auc(pos: list[float], neg: list[float]) -> float:
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    db = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    titles = dict(db.execute("SELECT doc_id, title FROM docs"))
    tasks = {t["task_id"]: t for t in map(json.loads, (HERE / "chap12/tune/mixed_tasks.jsonl")
                                          .read_text("utf-8").splitlines())}
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    traces = {r["task_id"]: r for r in map(json.loads, (RUN / "traces.jsonl")
                                           .read_text("utf-8-sig").splitlines()) if r}
    answers = {r["task_id"]: r for r in map(json.loads, (RUN / "runs.jsonl")
                                            .read_text("utf-8-sig").splitlines()) if r} \
        if (RUN / "runs.jsonl").is_file() else {}
    items = json.loads((RUN / "layer_attribution.json").read_text("utf-8-sig"))["items"]
    cases = []
    for item in items:
        if not item["layer"].startswith(("L3", "L4")):
            continue
        tid = item["task_id"]
        g = gold[tid].get("document") if gold[tid].get("answerable") == "Y" else None
        info = classify(item["layer"], traces[tid], g, titles)
        cases.append({"task_id": tid, "layer": item["layer"], **info,
                      "question": " ".join(tasks[tid]["query"].split())[:400],
                      "gold": g, "gold_title": titles.get(g or "", ""),
                      "selected_titles": [titles.get(d, d) for d in info["selected"]],
                      "cited_titles": [titles.get(d, d) for d in info["cited"]],
                      "answer": " ".join(str(answers.get(tid, {}).get("answer", ""))
                                         .split())[:300]})
    # Hard score gate: top score margin, answerable-correct vs unanswerable.
    pos, neg = [], []
    for item in items:
        t = traces[item["task_id"]]
        ret = t["layers"].get("retrieval", {}).get("returned") or []
        if not ret or ret[0].get("threshold") is None:
            continue
        m = ret[0]["score"] - ret[0]["threshold"]
        if item.get("answerable") and item["layer"] == "correct":
            pos.append(m)
        elif not item.get("answerable"):
            neg.append(m)
    best = max(((sum(p >= c for p in pos) - sum(n >= c for n in neg), c)
                for c in sorted(set(pos + neg))), default=(0, 0.0))
    gate = {"answerable_correct": len(pos), "unanswerable": len(neg),
            "auc": round(auc(pos, neg), 3), "best_cut_margin": round(best[1], 4),
            "kept_correct_at_best_cut": sum(p >= best[1] for p in pos),
            "kept_unanswerable_at_best_cut": sum(n >= best[1] for n in neg)}
    args.out.mkdir(parents=True, exist_ok=True)
    reasons = Counter((c["layer"], c["reason"]) for c in cases)
    (args.out / "cases.json").write_text(json.dumps({"cases": cases, "gate": gate}, indent=2,
                                                    ensure_ascii=False), encoding="utf-8")
    lines = ["# E4 汇总：答案文档检索到之后在哪一步丢失（调参集，当前配置 trace）", "",
             "| 层 | 原因 | 题数 |", "| --- | --- | --- |"]
    lines += [f"| {layer} | {reason} | {n} |" for (layer, reason), n in sorted(reasons.items())]
    lines += ["", "## 硬分数门槛能否区分（第 1 篇重排分数 − 门槛）", "",
              f"可回答且答对 {gate['answerable_correct']} 道 vs "
              f"不可回答 {gate['unanswerable']} 道："
              f"AUC {gate['auc']}；本集上最好的单一切点（margin ≥ {gate['best_cut_margin']}）"
              f"保留答对 {gate['kept_correct_at_best_cut']}、保留不可回答 "
              f"{gate['kept_unanswerable_at_best_cut']}（只是描述，在同一集上选切点会偏乐观）。"]
    (args.out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    md = ["# E4 逐题", ""]
    for c in cases:
        md += [f"## {c['task_id']} — {c['layer']} — {c['reason']}", "",
               f"- 问题：{c['question']}",
               f"- 答案文档：{c['gold']} {c['gold_title']}（返回第 {c['gold_returned_pos']} 篇，"
               f"证据 {c['gold_source']}；证据 {c['evidence_n']} 篇 / "
               f"{c['context_tokens']} tokens）",
               f"- 选证据（{c['selection_decision']}）：{c['selected_titles']}",
               f"- 判断（{c['judge_decision']}）否决：{c['judge_rejected']}",
               f"- 引用：{c['cited_titles']}；状态 {c['rag_status']}；第 1 篇分数−门槛 "
               f"{c['top_score_margin']}",
               f"- 回答开头：{c['answer'][:200]}", ""]
    (args.out / "cases.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
