"""E1: how the retrieved documents differ from the gold document (2026-10-26; diagnosis only).

    python -m evaluation.chap12_gap_analysis --index PATH/chap12_tune.sqlite

Current configuration, TUNE split (results/chap12/tune_real_r9_judged14 traces). Cases: every
answerable question whose gold document is not in the reranked top 8 (layers L1 and L2), plus 15
controls whose gold document is ranked first (seed 20261026). For each case it lists the
question, the rewritten query, the gold document and the top 3 reranked documents (title, product,
opening text) and the gold document's rank in each stage, and tags candidate causes with simple
rules (several may apply; they are a first grouping for a human to check, not ground truth):
  wrong_product      the top-ranked document has no product in common with the gold document
  same_product       top-ranked document shares a product but is a different document
  near_duplicate     a top-3 title shares >= 60% of its words with the gold title, or both cite
                     the same APAR / fix id
  vocab_gap          the question shares fewer words with the gold document's title+opening than
                     with the top-ranked document's
  rewrite_dropped    an identifier in the question (error code, APAR, version, file name) is
                     missing from the rewritten query
  dense_only / sparse_only / neither   which first-stage branch found the gold document
Writes results/chap12/e1_gap_analysis/{cases.json,cases.md,summary.md}.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sqlite3
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE / "results/chap12/tune_real_r9_judged14"
OUT = HERE / "results/chap12/e1_gap_analysis"
WORD = re.compile(r"[a-z0-9][a-z0-9_.\-]{2,}")
IDENT = re.compile(r"\b(?:[A-Z]{2,}\d{2,}[A-Z0-9]*|[A-Z]{3,}-\d+|\d+\.\d+(?:\.\d+)*|"
                   r"[\w\-]+\.(?:xml|log|jar|properties|sh|bat|cfg|conf|ini|exe|dll))\b")
STOP = set("the and for with from that this when what how are was were not can does have has "
           "you your our use using get got after before into ibm united states".split())


def words(text: str) -> set[str]:
    return {w for w in WORD.findall(text.lower()) if w not in STOP}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=Path, required=True)
    args = parser.parse_args()
    db = sqlite3.connect(f"file:{args.index}?mode=ro", uri=True)
    docs = {d: (t or "", x or "") for d, t, x in db.execute("SELECT doc_id, title, text FROM docs")}
    products: dict[str, set[str]] = {}
    for d, p in db.execute("SELECT doc_id, product_id FROM document_products"):
        products.setdefault(d, set()).add(p)
    names = {p: n for p, n in db.execute("SELECT DISTINCT product_id, product_name FROM technotes")}
    tasks = {t["task_id"]: t for t in map(json.loads, (HERE / "chap12/tune/mixed_tasks.jsonl")
                                          .read_text("utf-8").splitlines())}
    gold = {g["task_id"]: g for g in map(json.loads, (HERE / "chap12/tune/mixed_gold.jsonl")
                                         .read_text("utf-8").splitlines())}
    traces = {r["task_id"]: r for r in map(json.loads, (RUN / "traces.jsonl")
                                           .read_text("utf-8-sig").splitlines()) if r}
    items = json.loads((RUN / "layer_attribution.json").read_text("utf-8-sig"))["items"]
    misses = [i for i in items if i["layer"].startswith(("L1", "L2"))]
    firsts = [i for i in items if i.get("answerable") and i["layer"] == "correct"
              and traces[i["task_id"]]["layers"]["retrieval"]["stages"]["rerank"]
              and traces[i["task_id"]]["layers"]["retrieval"]["stages"]["rerank"][0]["doc"]
              == gold[i["task_id"]]["document"]]
    controls = sorted(random.Random(20261026).sample(firsts, min(15, len(firsts))),
                      key=lambda i: i["task_id"])

    def opening(d: str, n: int = 300) -> str:
        return " ".join(docs.get(d, ("", ""))[1].split())[:n]

    def product_names(d: str) -> str:
        return ", ".join(sorted(names.get(p, p) for p in products.get(d, set()))) or "?"

    cases = []
    for group, chosen in (("miss", misses), ("control", controls)):
        for item in chosen:
            tid = item["task_id"]
            r = traces[tid]["layers"]["retrieval"]
            stages = r["stages"]
            g = gold[tid]["document"]
            top3 = [x["doc"] for x in stages["rerank"][:3]]
            rank = {s: next((x["rank"] for x in stages[s] if x["doc"] == g), None)
                    for s in ("dense", "sparse", "fusion", "rerank")}
            q = tasks[tid]["query"]
            tags = []
            if rank["dense"] and not rank["sparse"]:
                tags.append("dense_only")
            elif rank["sparse"] and not rank["dense"]:
                tags.append("sparse_only")
            elif not rank["dense"] and not rank["sparse"]:
                tags.append("neither")
            if group == "miss" and top3:
                t1 = top3[0]
                if not products.get(t1, set()) & products.get(g, set()):
                    tags.append("wrong_product")
                else:
                    tags.append("same_product")
                gt = words(docs.get(g, ("", ""))[0])
                ids_gold = set(IDENT.findall(docs.get(g, ("", ""))[0]))
                for d in top3:
                    dt = words(docs.get(d, ("", ""))[0])
                    jac = len(gt & dt) / max(len(gt | dt), 1)
                    if jac >= 0.6 or ids_gold & set(IDENT.findall(docs.get(d, ("", ""))[0])):
                        tags.append("near_duplicate")
                        break
                qw = words(q)
                gold_overlap = len(qw & words(docs[g][0] + " " + opening(g, 1500)))
                top_overlap = len(qw & words(docs[t1][0] + " " + opening(t1, 1500)))
                if gold_overlap < top_overlap:
                    tags.append("vocab_gap")
            missing = [i for i in set(IDENT.findall(q)) if i.lower() not in r["query"].lower()]
            if missing:
                tags.append("rewrite_dropped")
            cases.append({"group": group, "task_id": tid, "layer": item["layer"], "tags": tags,
                          "question": " ".join(q.split())[:500],
                          "rewritten_query": " ".join(r["query"].split())[:300],
                          "rewrite_missing_ids": missing, "gold_rank": rank,
                          "gold": {"doc": g, "title": docs.get(g, ("?", ""))[0],
                                   "products": product_names(g), "opening": opening(g)},
                          "top3": [{"doc": d, "title": docs.get(d, ("?", ""))[0],
                                    "products": product_names(d), "opening": opening(d, 200)}
                                   for d in top3]})
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cases.json").write_text(json.dumps(cases, ensure_ascii=False, indent=1) + "\n",
                                    encoding="utf-8")
    lines = ["# E1 案例表（调参集，当前配置）", ""]
    for c in cases:
        lines += [f"## {c['group']} · {c['task_id']} · {c['layer']} · {', '.join(c['tags'])}", "",
                  f"- 问题：{c['question']}", f"- 改写后：{c['rewritten_query']}"
                  + (f"（丢失：{', '.join(c['rewrite_missing_ids'])}）"
                     if c["rewrite_missing_ids"] else ""),
                  f"- 答案文档在各阶段名次：{c['gold_rank']}",
                  f"- **答案文档** {c['gold']['doc']}｜{c['gold']['products']}｜"
                  f"{c['gold']['title']}", f"  - {c['gold']['opening']}"]
        for i, t in enumerate(c["top3"], 1):
            lines += [f"- 重排第 {i}：{t['doc']}｜{t['products']}｜{t['title']}",
                      f"  - {t['opening']}"]
        lines.append("")
    (OUT / "cases.md").write_text("\n".join(lines), encoding="utf-8")
    miss = [c for c in cases if c["group"] == "miss"]
    ctrl = [c for c in cases if c["group"] == "control"]
    count = Counter(t for c in miss for t in c["tags"])
    ccount = Counter(t for c in ctrl for t in c["tags"])
    order = ["neither", "dense_only", "sparse_only", "wrong_product", "same_product",
             "near_duplicate", "vocab_gap", "rewrite_dropped"]
    summary = ["# E1 汇总", "", f"未进前 8 的可回答题 {len(miss)} 道（L1 召回 "
               f"{sum(c['layer'].startswith('L1') for c in miss)}、L2 重排 "
               f"{sum(c['layer'].startswith('L2') for c in miss)}），对照组（答案文档排第一）"
               f"{len(ctrl)} 道。标签可多选，规则见脚本说明，供人工核对。", "",
               "| 标签 | 未进前 8 | 对照组 |", "| --- | --- | --- |"]
    summary += [f"| {t} | {count.get(t, 0)} | {ccount.get(t, 0)} |" for t in order]
    (OUT / "summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
