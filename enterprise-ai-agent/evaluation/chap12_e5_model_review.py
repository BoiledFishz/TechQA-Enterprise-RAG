"""E5 by two model reviewers instead of people (amendment of 2026-10-28).

    python -m evaluation.chap12_e5_model_review local    --items ITEMS --out REVIEWS_QWEN.json
    python -m evaluation.chap12_e5_model_review packets  --items ITEMS --out-dir DIR
    python -m evaluation.chap12_e5_model_review ingest   --pasted PASTED.txt --out REVIEWS_GPT.json
    python -m evaluation.chap12_e5_model_review disagree --reviews A.json B.json --items ITEMS

The same blind items and the same four questions as the human sheet. PROMPT below is the only
instruction; the reviewer sees the question, the published answer and the cited documents, never
the gold document, the automatic score or the stratum.
  local    qwen2.5:14b through Ollama /api/chat, temperature 0, JSON schema output, num_ctx 16384
  packets  ChatGPT packets (10 items each) for the user to paste; ingest parses the replies
  disagree lists items whose overall judgement differs, for the user to decide
Reviews are written as {reviewer: {item: {answers, supported, product, overall, reason}}}, the
format chap12_e5_review analyze reads.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.request
from pathlib import Path
from typing import Any

PROMPT = """You are reviewing a technical support answer, blind. You see a customer's question,
the answer a system published, and the full text of the documents the answer cites. Judge only
from what is shown; do not use outside knowledge to fill gaps.

Answer four questions:
1. answers: does the answer address what the customer asked? yes / partial / no
2. supported: is the answer's content supported by the cited documents (nothing invented)?
   yes / partial / no
3. product: do the cited documents' product and version match the question?
   match / mismatch / unclear
4. overall: would this be an acceptable reply from a support engineer? acceptable / unacceptable
   (acceptable = it addresses the question, is supported by the documents, and is for the right
   product; a reply about a different product, a different error, or that does not answer the
   question is unacceptable)
Give a one-sentence reason."""
KEYS = {"answers": ["yes", "partial", "no"], "supported": ["yes", "partial", "no"],
        "product": ["match", "mismatch", "unclear"], "overall": ["acceptable", "unacceptable"]}
SCHEMA = {"type": "object", "required": [*KEYS, "reason"], "properties": {
    **{k: {"type": "string", "enum": v} for k, v in KEYS.items()}, "reason": {"type": "string"}}}


def render(item: dict[str, Any]) -> str:
    docs = "\n\n".join(f"--- Cited document {i}: {d['title']} ({d['doc']})\n{d['text']}"
                       + ("\n[document truncated]" if d.get("truncated") else "")
                       for i, d in enumerate(item["documents"], 1))
    return (f"=== Item {item['id']}\n--- Question\n{item['question']}\n\n--- Published answer\n"
            f"{item['answer']}\n\n{docs}")


def valid(r: Any) -> bool:
    return isinstance(r, dict) and all(r.get(k) in v for k, v in KEYS.items())


def local(args: argparse.Namespace) -> None:
    items = json.loads(args.items.read_text("utf-8"))
    out: dict[str, dict[str, Any]] = {}
    if args.out.is_file():
        out = json.loads(args.out.read_text("utf-8")).get(args.name, {})
    for item in items:
        if item["id"] in out:
            continue
        body = {"model": args.model, "stream": False, "format": SCHEMA,
                "options": {"temperature": 0, "num_ctx": 16384, "num_predict": 300},
                "messages": [{"role": "user", "content": PROMPT + "\n\nReply as JSON.\n\n"
                              + render(item)}]}
        started = time.time()
        req = urllib.request.Request(args.ollama.rstrip("/") + "/api/chat",
                                     json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=900) as resp:
            reply = json.loads(resp.read())
        try:
            parsed = json.loads(reply["message"]["content"])
        except (KeyError, json.JSONDecodeError):
            parsed = {}
        out[item["id"]] = parsed if valid(parsed) else {"invalid": reply.get("message", {})
                                                        .get("content", "")[:500]}
        out[item["id"]]["prompt_tokens"] = reply.get("prompt_eval_count")
        print(f"{item['id']} {out[item['id']].get('overall', 'INVALID')} "
              f"{time.time() - started:.0f}s", flush=True)
        args.out.write_text(json.dumps({args.name: out}, indent=1, ensure_ascii=False),
                            encoding="utf-8")


def packets(args: argparse.Namespace) -> None:
    items = json.loads(args.items.read_text("utf-8"))
    args.out_dir.mkdir(parents=True, exist_ok=True)
    fmt = ('Reply with ONE JSON array only, one object per item, in order: [{"id": "R01", '
           '"answers": "...", "supported": "...", "product": "...", "overall": "...", '
           '"reason": "..."}, ...]')
    for n in range(0, len(items), args.size):
        part = items[n:n + args.size]
        text = (f"{PROMPT}\n\nThere are {len(part)} items below; judge each one separately. "
                f"{fmt}\n\n" + "\n\n".join(render(i) for i in part))
        path = args.out_dir / f"packet_{n // args.size + 1}.txt"
        path.write_text(text, encoding="utf-8")
        print(path, len(text))


def ingest(args: argparse.Namespace) -> None:
    out: dict[str, Any] = {}
    for arr in re.findall(r"\[\s*\{.*?\}\s*\]", args.pasted.read_text("utf-8"), re.S):
        for r in json.loads(arr):
            if valid(r):
                out[r["id"]] = {k: r[k] for k in [*KEYS, "reason"] if k in r}
    args.out.write_text(json.dumps({args.name: out}, indent=1, ensure_ascii=False),
                        encoding="utf-8")
    print(f"{len(out)} valid items")


def disagree(args: argparse.Namespace) -> None:
    (na, a), = json.loads(args.reviews[0].read_text("utf-8")).items()
    (nb, b), = json.loads(args.reviews[1].read_text("utf-8")).items()
    items = {i["id"]: i for i in json.loads(args.items.read_text("utf-8"))}
    ids = sorted(set(a) & set(b))
    diff = [i for i in ids if a[i].get("overall") != b[i].get("overall")]
    print(f"overall agreement {len(ids) - len(diff)}/{len(ids)}; disagree: {diff}")
    lines = [f"# 两个模型意见不同的题（{len(diff)} 道）", ""]
    for i in diff:
        lines += [f"## {i}", "", f"- {na}: {a[i].get('overall')} — {a[i].get('reason', '')}",
                  f"- {nb}: {b[i].get('overall')} — {b[i].get('reason', '')}", "",
                  render(items[i]), ""]
    if args.out:
        args.out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("local")
    s.add_argument("--items", type=Path, required=True)
    s.add_argument("--out", type=Path, required=True)
    s.add_argument("--model", default="qwen2.5:14b")
    s.add_argument("--name", default="qwen2.5:14b")
    s.add_argument("--ollama", default="http://localhost:11434")
    s = sub.add_parser("packets")
    s.add_argument("--items", type=Path, required=True)
    s.add_argument("--out-dir", type=Path, required=True)
    s.add_argument("--size", type=int, default=10)
    s = sub.add_parser("ingest")
    s.add_argument("--pasted", type=Path, required=True)
    s.add_argument("--out", type=Path, required=True)
    s.add_argument("--name", default="chatgpt")
    s = sub.add_parser("disagree")
    s.add_argument("--reviews", type=Path, nargs=2, required=True)
    s.add_argument("--items", type=Path, required=True)
    s.add_argument("--out", type=Path)
    args = p.parse_args()
    {"local": local, "packets": packets, "ingest": ingest, "disagree": disagree}[args.cmd](args)


if __name__ == "__main__":
    main()
