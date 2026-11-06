"""E8: the teacher's suggestions (2026-11-05), on the TUNE split.

    python -m evaluation.chap12_e8

Current configuration (round 9): nomic rerank (BM25 prior), top_k 8, 2400 tokens, Critic on,
7B rewrite + 7B selection + 14B judge (prompt v1). All variants also set
CHAP12_EXPLAIN_REFUSAL=1: when the selection picks nothing, the same model is asked why (trace
only, unmetered; it never changes an outcome).
    results/chap12/tune_real_e8_v2    CHAP12_JUDGE_PROMPT=v2 (answerable examples A1-A5 and a
                                      one-sentence reason per veto), local models as now
    results/chap12/tune_real_e8_q72   selection + judge on openrouter:qwen/qwen-2.5-72b-instruct
    results/chap12/tune_real_e8_l70   selection + judge on
                                      openrouter:meta-llama/llama-3.3-70b-instruct
    results/chap12/tune_real_e8_gpt   selection + judge on openrouter:openai/gpt-5.6-luna
    (the three hosted runs keep judge prompt v1 and the local 7B query rewrite, so only the
    model size / family changes)
Base: results/chap12/tune_real_e6_base (Ollama 0.40.13), or tune_real_e8_base when the runner had
to re-run the current configuration on another Ollama version.
Rules, fixed and committed before the runs:
  adopt  only v2 can be adopted (the hosted models are outside the self-deployed system and are
         run to measure the effect of model size): eligible if, against the base, correct
         answerable answers lost <= 3, net paired wins >= 5, failure rate not higher, and mean
         token F1 on answerable tasks answered by both runs not lower by more than 0.05.
  report the same paired numbers for every hosted variant ("would pass" is reported, not
         adopted); and the reasons the judge and the refusal diagnostic gave.
Updates `adopted.judge_prompt` and adds `e8` in real_config.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import RESULTS, compare, load
from evaluation.chap12_round6 import lost_answerable
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent / "chap12/tune"
BASE = "tune_real_e8_base" if (RESULTS / "tune_real_e8_base/summary.json").is_file() \
    else "tune_real_e6_base"
VARIANTS = {"v2": "local qwen2.5:7b + 14b, judge v2",
            "q72": "openrouter:qwen/qwen-2.5-72b-instruct",
            "l70": "openrouter:meta-llama/llama-3.3-70b-instruct",
            "gpt": "openrouter:openai/gpt-5.6-luna"}


def main() -> None:
    base_rows, b = load(BASE), summary(BASE)
    result: dict[str, Any] = {"base_run": BASE, "base": b, "variants": {}}
    for name, model in VARIANTS.items():
        run = f"tune_real_e8_{name}"
        if not (RESULTS / run / "summary.json").is_file():
            result["variants"][name] = {"model": model, "not_run": True}
            continue
        pair = compare(BASE, run)
        lost = lost_answerable(base_rows, {key: bool(r["score"].get("correct"))
                                           for key, r in load(run).items()})
        v = summary(run)
        f1 = pair["y_token_f1_both_answered"]
        ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
              and f1["variant"] >= f1["base"] - 0.05)
        result["variants"][name] = {"model": model, "summary": v,
                                    "correct_answerable_lost": lost, "passes_rule": ok,
                                    "paired": {x: pair[x] for x in (
                                        "base_correct", "variant_correct", "wins", "losses",
                                        "net", "mcnemar_p_one_sided",
                                        "y_token_f1_both_answered")}}
    adopted = "v2" if result["variants"].get("v2", {}).get("passes_rule") else None
    config_path = HERE / "real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    if adopted:
        config["adopted"]["judge_prompt"] = "v2"
    result["adopted"] = adopted
    config["e8"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Updates")[0].strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
