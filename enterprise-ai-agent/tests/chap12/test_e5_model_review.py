"""E5 model review: reply parsing keeps only well-formed judgements."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from evaluation.chap12_e5_model_review import ingest, render, valid


def test_valid_and_ingest(tmp_path: Path) -> None:
    good = {"id": "R01", "answers": "yes", "supported": "partial", "product": "match",
            "overall": "acceptable", "reason": "ok"}
    bad = {**good, "id": "R02", "overall": "maybe"}
    assert valid(good) and not valid(bad)
    pasted = tmp_path / "p.txt"
    pasted.write_text("Here you go:\n```json\n" + json.dumps([good, bad]) + "\n```", "utf-8")
    out = tmp_path / "o.json"
    ingest(argparse.Namespace(pasted=pasted, out=out, name="chatgpt"))
    assert list(json.loads(out.read_text("utf-8"))["chatgpt"]) == ["R01"]


def test_render_hides_nothing_but_shows_no_key() -> None:
    text = render({"id": "R05", "question": "Q?", "answer": "A.",
                   "documents": [{"doc": "swg1", "title": "T", "text": "body"}]})
    assert "Q?" in text and "A." in text and "swg1" in text and "gold" not in text.lower()
