"""E6: one pre-registered end-to-end run of the E1-E5 findings, on the TUNE split (2026-10-30).

    python -m evaluation.chap12_e6

Current configuration (round 9): nomic rerank (BM25 prior), top_k 8, Critic on, 7B rewrite +
7B selection + 14B judge. Variants (everything else unchanged):
    results/chap12/tune_real_e6_e5     CHAP12_RERANKER=e5_order
        e5-base-v2 order with nomic acceptance (E3: e5_only R@5 69 -> 76, R@1 53 -> 54)
    results/chap12/tune_real_e6_e5fb   CHAP12_RERANKER=e5_order, CHAP12_SELECT_FALLBACK=qwen2.5:14b
        plus: when the 7B selection picks no source, the same selection runs once with 14B
        (E4: 5 answerable questions lost because the 7B selection picked nothing)
Base: tune_real_r9_judged14 (Ollama 0.40.9), or results/chap12/tune_real_e6_base when the
runner had to re-run the current configuration on another Ollama version.
Rules, fixed and committed before the runs:
  adopt  a variant is eligible only if, against the base: correct answerable answers lost <= 3,
         net paired wins >= 5, failure rate not higher, and mean token F1 on answerable tasks
         answered by both runs not lower by more than 0.05. Adopt the eligible variant with the
         larger net (ties: e5, the smaller change). Latency is reported, not gated.
Updates `adopted.reranker` / `adopted.select_fallback` and adds `e6` in real_config.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import RESULTS, compare, load
from evaluation.chap12_round6 import lost_answerable
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent / "chap12/tune"
BASE = "tune_real_e6_base" if (RESULTS / "tune_real_e6_base/summary.json").is_file() \
    else "tune_real_r9_judged14"
VARIANTS = {"e5": None, "e5fb": "qwen2.5:14b"}


def main() -> None:
    base_rows, b = load(BASE), summary(BASE)
    result: dict[str, Any] = {"base_run": BASE, "base": b, "variants": {}}
    if BASE != "tune_real_r9_judged14":
        r = compare("tune_real_r9_judged14", BASE)
        result["base_reproduces_r9"] = {x: r[x] for x in ("base_correct", "variant_correct",
                                                          "wins", "losses")}
    eligible = {}
    for name, fallback in VARIANTS.items():
        run = f"tune_real_e6_{name}"
        pair = compare(BASE, run)
        lost = lost_answerable(base_rows, {key: bool(r["score"].get("correct"))
                                           for key, r in load(run).items()})
        v = summary(run)
        f1 = pair["y_token_f1_both_answered"]
        ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
              and f1["variant"] >= f1["base"] - 0.05)
        result["variants"][name] = {"select_fallback": fallback, "summary": v,
                                    "correct_answerable_lost": lost, "eligible": ok,
                                    "paired": {x: pair[x] for x in (
                                        "base_correct", "variant_correct", "wins", "losses",
                                        "net", "mcnemar_p_one_sided",
                                        "y_token_f1_both_answered")}}
        if ok:
            eligible[name] = (pair["net"], name == "e5")
    chosen = max(eligible, key=lambda n: eligible[n]) if eligible else None
    config_path = HERE / "real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    if chosen:
        config["adopted"]["reranker"] = "e5_order"
        config["adopted"]["select_fallback"] = VARIANTS[chosen]
    result["adopted"] = chosen
    config["e6"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Updates")[0].strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
