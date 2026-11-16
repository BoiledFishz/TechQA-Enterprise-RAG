"""E10: the teacher's 2026-11-16 suggestions, on the TUNE split (report only).

    python -m evaluation.chap12_e10

Variants (all with CHAP12_EXPLAIN_REFUSAL=1, OpenRouter retries 2 / 120 s, deadline 600 s):
  tune_real_e10_online   every LLM call on openrouter:openai/gpt-5.6-luna (query rewrite,
                         selection, judge, Critic, product pick); retrieval as now (nomic rerank)
  tune_real_e10_gptsel   only selection + judge on gpt-5.6-luna, 7B rewrite (E8 "gpt" again,
                         now with retries)
  tune_real_e10_oracle_local  oracle retrieval (the gold document only), local 7B select + 14B judge
  tune_real_e10_oracle_gpt    oracle retrieval, selection + judge on gpt-5.6-luna (7B rewrite)
Base: tune_real_e9_base (current configuration, Ollama 0.40.15), or tune_real_e10_base when the
runner had to re-run it on another Ollama version.
Rules, fixed and committed before the runs:
  valid   a run is interpretable only if at most 8 of its 150 tasks carry an error.
  report  only (hosted models; oracle retrieval is not a system): for online and gptsel, paired
          numbers against the base and the usual rule as "would pass"; for every run, on the 112
          answerable tasks: answered correctly, gold document cited, mean token F1 of answered
          tasks, and gold-span coverage = the published answer contains at least half of the gold
          answer's tokens (a chunk-level check against the golden answer, in addition to the
          document-level score). Oracle runs are read on the answerable tasks only.
Writes results/chap12/e10_summary.{json,md} and `e10` in real_config.json (adopted unchanged).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_compare import tokens
from evaluation.chap12_paired import RESULTS, compare, load
from evaluation.chap12_round6 import lost_answerable
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent
BASE = "tune_real_e10_base" if (RESULTS / "tune_real_e10_base/summary.json").is_file() \
    else "tune_real_e9_base"
RUNS = ["tune_real_e10_online", "tune_real_e10_gptsel", "tune_real_e10_oracle_local",
        "tune_real_e10_oracle_gpt"]


def span_recall(answer: str, gold: str) -> float:
    a, g = tokens(answer or ""), tokens(gold or "")
    if not g:
        return 0.0
    return sum(min(a.count(t), g.count(t)) for t in set(g)) / len(g)


def answerable_view(run: str, gold: dict[str, Any]) -> dict[str, Any]:
    rows = [r for r in load(run).values()]
    y = [r for r in rows if gold[r["task_id"]].get("answerable") == "Y"]
    answered = [r for r in y if r.get("answer")]
    return {"answerable": len(y), "correct": sum(bool(r["score"].get("correct")) for r in y),
            "gold_cited": sum(bool(r["score"].get("gold_cited")) for r in y),
            "answered": len(answered),
            "token_f1_answered": round(sum(r["score"].get("token_f1") or 0 for r in answered)
                                       / max(len(answered), 1), 3),
            "gold_span_covered": sum(span_recall(r.get("answer", ""), gold[r["task_id"]].get(
                "answer", "")) >= 0.5 for r in y),
            "tasks_with_error": sum(1 for r in rows if r.get("error"))}


def paired(run: str) -> dict[str, Any]:
    pair = compare(BASE, run)
    lost = lost_answerable(load(BASE), {k: bool(r["score"].get("correct"))
                                        for k, r in load(run).items()})
    b, v = summary(BASE), summary(run)
    f1 = pair["y_token_f1_both_answered"]
    return {"correct_answerable_lost": lost,
            "would_pass": (lost <= 3 and pair["net"] >= 5
                           and v["failure_rate"] <= b["failure_rate"]
                           and f1["variant"] >= f1["base"] - 0.05),
            **{x: pair[x] for x in ("base_correct", "variant_correct", "wins", "losses", "net",
                                    "mcnemar_p_one_sided")}}


def main() -> None:
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    out: dict[str, Any] = {"base": BASE, "runs": {BASE: answerable_view(BASE, gold)}}
    for run in RUNS:
        if not (RESULTS / run / "summary.json").is_file():
            out["runs"][run] = {"not_run": True}
            continue
        view = answerable_view(run, gold)
        view["valid"] = view["tasks_with_error"] <= 8
        if "oracle" not in run:
            view["paired_vs_base"] = paired(run)
        out["runs"][run] = view
    (RESULTS / "e10_summary.json").write_text(json.dumps(out, indent=1), "utf-8")
    cols = ["correct", "gold_cited", "gold_span_covered", "answered", "token_f1_answered",
            "tasks_with_error"]
    md = ["# E10（调参集，112 道可回答题）", "", "| 运行 | " + " | ".join(cols) + " | 配对 |",
          "|" + " --- |" * (len(cols) + 2)]
    for run, v in out["runs"].items():
        if v.get("not_run"):
            md.append(f"| {run} | 未执行 |")
            continue
        p = v.get("paired_vs_base")
        pair = f"{p['variant_correct']} vs {p['base_correct']}，净 {p['net']}，丢失 " \
               f"{p['correct_answerable_lost']}" if p else ""
        md.append(f"| {run} | " + " | ".join(str(v[c]) for c in cols) + f" | {pair} |")
    (RESULTS / "e10_summary.md").write_text("\n".join(md) + "\n", "utf-8")
    config_path = HERE / "chap12/tune/real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    config["e10"] = out | {"rule": __doc__.split("Rules, fixed")[1].split("Writes")[0].strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n", "utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
