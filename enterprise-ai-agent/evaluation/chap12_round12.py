"""Round 12: 14B also for the selection call (two variants), on the TUNE split.

    python -m evaluation.chap12_round12

Current configuration (round 9): nomic rerank (BM25 prior), top_k 8, Critic on, 7B rewrite +
7B selection + 14B judge. In round 11's trace (diagnosis) the remaining losses with the gold
document in the evidence were: the 7B selector refusing 7 (gold often at evidence position 1),
the 14B judge vetoing 7, and citing another document 5; unanswerable questions answered 19.
Variants (query rewrite stays 7B in both):
    results/chap12/tune_real_r12_s14      CHAP12_SELECTOR_MODEL=qwen2.5:14b
    results/chap12/tune_real_r12_s14max   CHAP12_SELECTOR_MODEL=qwen2.5:14b, CHAP12_RERANK_PRIOR=max
Base: tune_real_r9_judged14 (Ollama 0.40.9), or results/chap12/tune_real_r12_base when the
runner had to re-run the current configuration on a newer Ollama.
Rules, fixed and committed before the runs:
  adopt  a variant is eligible only if, against the base: correct answerable answers lost <= 3,
         net paired wins >= 5, failure rate not higher, and mean token F1 on answerable tasks
         answered by both runs not lower by more than 0.05. Adopt the eligible variant with the
         larger net (ties: s14, the smaller change). Latency is reported, not gated.
Updates `adopted.selector_model` / `adopted.rerank_prior` and adds `round12` in real_config.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import RESULTS, compare, load
from evaluation.chap12_round6 import lost_answerable

HERE = Path(__file__).resolve().parent / "chap12/tune"
BASE = "tune_real_r12_base" if (RESULTS / "tune_real_r12_base/summary.json").is_file() \
    else "tune_real_r9_judged14"
VARIANTS = {"s14": "bm25", "s14max": "max"}


def summary(name: str) -> dict[str, Any]:
    b = json.loads((RESULTS / name / "summary.json").read_text("utf-8-sig"))["systems"]["multi"][
        "all"]
    out = {k: float(b[v]["mean"]) for k, v in (
        ("correct_all", "correct_completion"), ("failure_rate", "failure_rate (failed+timeout)"),
        ("y_accept", "y_accept"), ("n_refuse", "n_refuse"), ("y_gold_cited", "y_gold_cited"))}
    return out | {"latency_mean_ms": float(b["latency_ms"]["mean"]),
                  "retrieval_y": b.get("retrieval_y")}


def main() -> None:
    base_rows, b = load(BASE), summary(BASE)
    result: dict[str, Any] = {"base_run": BASE, "base": b, "variants": {}}
    if BASE != "tune_real_r9_judged14":
        r = compare("tune_real_r9_judged14", BASE)
        result["base_reproduces_r9"] = {x: r[x] for x in ("base_correct", "variant_correct",
                                                          "wins", "losses")}
    eligible = {}
    for name, prior in VARIANTS.items():
        run = f"tune_real_r12_{name}"
        pair = compare(BASE, run)
        lost = lost_answerable(base_rows, {key: bool(r["score"].get("correct"))
                                           for key, r in load(run).items()})
        v = summary(run)
        f1 = pair["y_token_f1_both_answered"]
        ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
              and f1["variant"] >= f1["base"] - 0.05)
        result["variants"][name] = {"rerank_prior": prior, "summary": v,
                                    "correct_answerable_lost": lost, "eligible": ok,
                                    "paired": {x: pair[x] for x in (
                                        "base_correct", "variant_correct", "wins", "losses",
                                        "net", "mcnemar_p_one_sided",
                                        "y_token_f1_both_answered")}}
        if ok:
            eligible[name] = (pair["net"], name == "s14")
    chosen = max(eligible, key=lambda n: eligible[n]) if eligible else None
    config_path = HERE / "real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    config["adopted"]["rerank_prior"] = VARIANTS[chosen] if chosen else "bm25"
    config["adopted"]["selector_model"] = "qwen2.5:14b" if chosen else None
    result["adopted"] = chosen
    config["round12"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Updates")[0]
                                  .strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
