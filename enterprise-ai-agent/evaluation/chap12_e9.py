"""E9: the two changes that each helped, together (2026-11-06; TUNE split, report only).

    python -m evaluation.chap12_e9

    results/chap12/tune_real_e9_e5q72   CHAP12_RERANKER=e5_order (E6: e5 order, nomic acceptance)
                                        + selection and judge on
                                        openrouter:qwen/qwen-2.5-72b-instruct (E8 q72)
Everything else is the current configuration (judge prompt v1, 7B query rewrite, 2400 tokens,
Critic on); CHAP12_EXPLAIN_REFUSAL=1 and a 300 s deadline as in E8's hosted runs.
Compared, by the same paired numbers as every round, with
  tune_real_e8_base  (current configuration, Ollama 0.40.14)
  tune_real_e8_q72   (72B alone: does e5 order add anything on top of it?)
Rules, fixed and committed before the run:
  report only: the hosted model is outside the self-deployed system, so nothing is adopted.
  The usual rule (lost <= 3, net >= 5, failure rate not higher, token F1 drop <= 0.05) is
  evaluated against tune_real_e8_base and reported as "would pass" / "would not pass".
Writes `e9` in real_config.json (adopted values unchanged).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evaluation.chap12_paired import compare, load
from evaluation.chap12_round6 import lost_answerable
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent / "chap12/tune"
RUN = "tune_real_e9_e5q72"


def against(base: str) -> dict[str, Any]:
    pair = compare(base, RUN)
    lost = lost_answerable(load(base), {k: bool(r["score"].get("correct"))
                                        for k, r in load(RUN).items()})
    b, v = summary(base), summary(RUN)
    f1 = pair["y_token_f1_both_answered"]
    ok = (lost <= 3 and pair["net"] >= 5 and v["failure_rate"] <= b["failure_rate"]
          and f1["variant"] >= f1["base"] - 0.05)
    return {"base": base, "correct_answerable_lost": lost, "would_pass": ok,
            "paired": {x: pair[x] for x in ("base_correct", "variant_correct", "wins",
                                            "losses", "net", "mcnemar_p_one_sided",
                                            "y_token_f1_both_answered")}}


def main() -> None:
    result = {"run": RUN, "summary": summary(RUN),
              "vs_base": against("tune_real_e8_base"), "vs_q72": against("tune_real_e8_q72")}
    path = HERE / "real_config.json"
    config = json.loads(path.read_text("utf-8-sig"))
    config["e9"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Writes")[0].strip()}
    path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
