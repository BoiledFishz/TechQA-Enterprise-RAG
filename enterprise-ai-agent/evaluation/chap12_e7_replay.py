"""E7 offline estimate: does breadth-first evidence or a larger budget put more gold documents
into the model's evidence? (2026-10-31; diagnosis, no model calls)

    python -m evaluation.chap12_e7_replay --index PATH/chap12_tune.sqlite --budget 2400 RUN...

Replays Project 1's ContextCompressor ("depth") and BreadthFirstCompressor ("breadth") on the
documents each traced question actually returned (full parent text from the sample index, the
traced rerank score and threshold). APPROXIMATE: the retrieved excerpt that steers passage
choice is not in the trace, so the replay is checked against the traced evidence and that
agreement is reported. Counts answerable questions whose gold document ends up in the evidence.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from agents.chap12.compression import BreadthFirstCompressor
from agents.rag_agent.compression import ContextCompressor
from models.schemas import Document

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results/chap12"


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--index", type=Path, required=True)
    p.add_argument("--budget", type=int, default=2400)
    p.add_argument("runs", nargs="+")
    args = p.parse_args()
    db = sqlite3.connect(args.index.resolve().as_uri() + "?mode=ro", uri=True)
    docs = {d: (t, x) for d, t, x in db.execute("SELECT doc_id, title, text FROM docs")}
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    for run in args.runs:
        traces = [json.loads(x) for x in (RESULTS / run / "traces.jsonl").read_text("utf-8-sig")
                  .splitlines() if x.strip()]
        out = {"run": run, "budget": args.budget, "replay_matches_trace": 0, "questions": 0,
               "gold_in_evidence_depth": 0, "gold_in_evidence_breadth": 0,
               "evidence_doc_set_changed": 0}
        for t in traces:
            layers = t["layers"]
            ret = layers["retrieval"]["returned"]
            if not ret:
                continue
            q = layers["rag"]["rewritten_query"]
            cands = [Document(chunk_id=f"c{i}", text=docs[r["doc"]][1] or docs[r["doc"]][0],
                              source_file="techqa://" + r["doc"], score=r["score"],
                              metadata={"_full_parent": True, "title": docs[r["doc"]][0],
                                        "_acceptance_threshold": r["threshold"]})
                     for i, r in enumerate(ret)]

            def chosen(c: type[ContextCompressor], cands: list[Document] = cands,
                       q: str = q) -> list[str]:
                res = c(args.budget, 8, model_selects_evidence=True).compress(q, cands)
                return list(dict.fromkeys(e.source_file[len("techqa://"):] for e in res.evidence))

            depth, breadth = chosen(ContextCompressor), chosen(BreadthFirstCompressor)
            actual = list(dict.fromkeys(e["doc"] for e in layers["rag"]["evidence"]))
            out["questions"] += 1
            out["replay_matches_trace"] += depth == actual
            out["evidence_doc_set_changed"] += set(depth) != set(breadth)
            g = gold[t["task_id"]]
            if g.get("answerable") == "Y":
                out["gold_in_evidence_depth"] += g["document"] in depth
                out["gold_in_evidence_breadth"] += g["document"] in breadth
        print(json.dumps(out))


if __name__ == "__main__":
    main()
