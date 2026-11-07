"""E9b: E9 again, with retries for transient OpenRouter failures (2026-11-07; report only).

    python -m evaluation.chap12_e9b

E9 (2026-11-06) was not interpretable: 26 OpenRouter errors and 17 calls over the 300 s deadline
broke 31 answerable questions. Same variant as E9 - e5 order with nomic acceptance + selection
and judge on openrouter:qwen/qwen-2.5-72b-instruct, judge prompt v1, 7B rewrite,
CHAP12_EXPLAIN_REFUSAL=1 - with only the transport changed: each OpenRouter call is retried up to
2 more times on timeouts, connection errors, HTTP 429 and 5xx (CHAP12_OPENROUTER_RETRIES=2,
CHAP12_OPENROUTER_TIMEOUT=120 per attempt), and the request deadline is 600 s.
    results/chap12/tune_real_e9b_e5q72
Base: tune_real_e9_base (Ollama 0.40.15), or tune_real_e9b_base when the runner had to re-run
the current configuration on another Ollama version.
Rules, fixed and committed before the run:
  valid   the run is interpretable only if at most 8 of the 150 tasks (about 5%) carry any error
          (failed, timeout or partial with an error); otherwise it is reported as inconclusive.
  report  only (hosted model): paired numbers against the base, and against tune_real_e8_q72
          (72B alone, Ollama 0.40.14: across versions, labelled so); the usual rule (lost <= 3,
          net >= 5, failure rate not higher, token F1 drop <= 0.05) as "would pass".
Writes `e9b` in real_config.json (adopted values unchanged).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import evaluation.chap12_e9 as e9
from evaluation.chap12_e9 import against as _against
from evaluation.chap12_paired import RESULTS, load
from evaluation.chap12_round12 import summary

HERE = Path(__file__).resolve().parent / "chap12/tune"
RUN = "tune_real_e9b_e5q72"
BASE = "tune_real_e9b_base" if (RESULTS / "tune_real_e9b_base/summary.json").is_file() \
    else "tune_real_e9_base"


def against(base: str) -> dict[str, Any]:
    e9.RUN = RUN
    return _against(base)


def main() -> None:
    rows = load(RUN)
    errored = sum(1 for r in rows.values() if r.get("error"))
    result = {"run": RUN, "summary": summary(RUN), "tasks_with_error": errored,
              "valid": errored <= 8, "vs_base": against(BASE),
              "vs_q72_other_ollama_version": against("tune_real_e8_q72")}
    path = HERE / "real_config.json"
    config = json.loads(path.read_text("utf-8-sig"))
    config["e9b"] = result | {"rule": __doc__.split("Rules, fixed")[1].split("Writes")[0].strip()}
    path.write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
