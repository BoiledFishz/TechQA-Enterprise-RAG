"""E7: breadth-first evidence (L3), on the TUNE split (2026-10-31).

    python -m evaluation.chap12_e7

Current configuration (round 9): nomic rerank (BM25 prior), top_k 8, max_context_tokens 2400,
Critic on, 7B rewrite + 7B selection + 14B judge. Variants (everything else unchanged):
    results/chap12/tune_real_e7_b2400   CHAP12_EVIDENCE_ORDER=breadth
    results/chap12/tune_real_e7_b3200   CHAP12_EVIDENCE_ORDER=breadth, AGENT_MAX_CONTEXT_TOKENS=3200
Base: results/chap12/tune_real_e6_base (current configuration, Ollama 0.40.13). The runner
stops unless Ollama is still 0.40.13, so base and variants share one version.
Rules, fixed and committed before the runs:
  adopt  a variant is eligible only if, against the base: correct answerable answers lost <= 3,
         net paired wins >= 5, failure rate not higher, and mean token F1 on answerable tasks
         answered by both runs not lower by more than 0.05. Adopt the eligible variant with the
         larger net (ties: b2400, the smaller change). Latency is reported, not gated.
Updates `adopted.evidence_order` / `adopted.max_context_tokens` and adds `e7` in
real_config.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import compare, load
from evaluation.chap12_round6 import lost_answerable
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent / "chap12/tune"
BASE = "tune_real_e6_base"
VARIANTS = {"b2400": 2400, "b3200": 3200}


def main() -> None:
    base_rows, b = load(BASE), summary(BASE)
    result: dict[str, Any] = {"base_run": BASE, "base": b, "variants": {}}
    eligible = {}
    for name, tokens in VARIANTS.items():
        run = f"tune_real_e7_{name}"
        pair = compare(BASE, run)
        lost = lost_answerable(base_rows, {key: bool(r["score"].get("correct"))
                                           for key, r in load(run).items()})
        v = summary(run)
        f1 = pair["y_token_f1_both_answered"]
        ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
              and f1["variant"] >= f1["base"] - 0.05)
        result["variants"][name] = {"max_context_tokens": tokens, "summary": v,
                                    "correct_answerable_lost": lost, "eligible": ok,
                                    "paired": {x: pair[x] for x in (
                                        "base_correct", "variant_correct", "wins", "losses",
                                        "net", "mcnemar_p_one_sided",
                                        "y_token_f1_both_answered")}}
        if ok:
            eligible[name] = (pair["net"], name == "b2400")
    chosen = max(eligible, key=lambda n: eligible[n]) if eligible else None
    config_path = HERE / "real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    if chosen:
        config["adopted"]["evidence_order"] = "breadth"
        config["adopted"]["max_context_tokens"] = VARIANTS[chosen]
    result["adopted"] = chosen
    config["e7"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Updates")[0].strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
