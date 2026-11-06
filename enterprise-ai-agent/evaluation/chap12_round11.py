"""Round 11: rerank prior = max(BM25-rank prior, fused-rank prior), candidate_k 30 (TUNE split).

    python -m evaluation.chap12_round11

Current configuration (round 9): nomic rerank, top_k 8, Critic on, 7B selector + 14B judge.
Round 10's fused-rank prior lifted R@8 but lowered R@1 (0.473 -> 0.375), and gold documents
landing at ranks 5-8 were cut from the model's context; not adopted. Offline on the same tune
candidates (results/chap12/prior_study.json, diagnosis) the max prior was at least as good as
the current prior at every cut (R@1 0.473 -> 0.482, R@3 0.589 -> 0.607, R@8 0.661 -> 0.696).
Variant (changes only the reranker's prior):
    results/chap12/tune_real_r11_max30   CHAP12_RERANK_PRIOR=max, CHAP12_CANDIDATE_K=30
Base: tune_real_r9_judged14 (Ollama 0.40.9), or results/chap12/tune_real_r11_base when the
runner had to re-run the current configuration on a newer Ollama.
Rules, fixed and committed before the run:
  adopt  only if, against the base: correct answerable answers lost <= 3, net paired wins >= 5,
         failure rate not higher, and mean token F1 on answerable tasks answered by both runs
         not lower by more than 0.05. Latency is reported, not gated.
Updates `adopted.rerank_prior` / `adopted.candidate_k` and adds `round11` in real_config.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import RESULTS, compare, load
from evaluation.chap12_round6 import lost_answerable

HERE = Path(__file__).resolve().parent / "chap12/tune"
BASE = "tune_real_r11_base" if (RESULTS / "tune_real_r11_base/summary.json").is_file() \
    else "tune_real_r9_judged14"
VARIANTS = {"max30": 30}


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
    for name, k in VARIANTS.items():
        run = f"tune_real_r11_{name}"
        pair = compare(BASE, run)
        lost = lost_answerable(base_rows, {key: bool(r["score"].get("correct"))
                                           for key, r in load(run).items()})
        v = summary(run)
        f1 = pair["y_token_f1_both_answered"]
        ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
              and f1["variant"] >= f1["base"] - 0.05)
        result["variants"][name] = {"candidate_k": k, "summary": v,
                                    "correct_answerable_lost": lost, "eligible": ok,
                                    "paired": {x: pair[x] for x in (
                                        "base_correct", "variant_correct", "wins", "losses",
                                        "net", "mcnemar_p_one_sided",
                                        "y_token_f1_both_answered")}}
        if ok:
            eligible[name] = (pair["net"], -k)
    chosen = max(eligible, key=lambda n: eligible[n]) if eligible else None
    config_path = HERE / "real_config.json"
    config = json.loads(config_path.read_text("utf-8-sig"))
    config["adopted"]["rerank_prior"] = "max" if chosen else "bm25"
    config["adopted"]["candidate_k"] = VARIANTS[chosen] if chosen else 30
    result["adopted"] = chosen
    config["round11"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Updates")[0]
                                  .strip()}
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
