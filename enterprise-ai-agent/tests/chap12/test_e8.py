"""E8: OpenRouter adapter, judge prompt v2 (answerable examples, reasons), refusal reasons."""

from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

from agents.chap12 import factory, tracing
from agents.chap12.judged_selector import PROMPT_V2, JudgedSelector, schema_for
from agents.chap12.openrouter import OpenRouterModel
from models.errors import DependencyUnavailable
from tests.chap12.test_judged_selector import EVIDENCE, Model


def transport(seen: list[dict[str, Any]], content: str) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append({"body": json.loads(request.content), "auth": request.headers["authorization"]})
        return httpx.Response(200, json={"choices": [{"message": {"content": content},
                                                      "finish_reason": "stop"}],
                                         "usage": {"prompt_tokens": 10, "completion_tokens": 3}})
    return httpx.MockTransport(handler)


def test_openrouter_request_shape() -> None:
    seen: list[dict[str, Any]] = []
    m = OpenRouterModel("openrouter:qwen/qwen-2.5-72b-instruct", api_key="k",
                        transport=transport(seen, '```json\n{"a": 1}\n```'))
    assert asyncio.run(m.generate("p", {"type": "object"})) == '{"a": 1}'
    body = seen[0]["body"]
    assert body["model"] == "qwen/qwen-2.5-72b-instruct" and body["temperature"] == 0
    assert body["provider"] == {"require_parameters": True}
    assert body["response_format"]["type"] == "json_schema"
    assert seen[0]["auth"] == "Bearer k"
    gpt = OpenRouterModel("openrouter:openai/gpt-5.6-luna", api_key="k")
    assert "temperature" not in gpt.body("p", {})


def test_openrouter_needs_a_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(DependencyUnavailable):
        OpenRouterModel("openrouter:x/y")


def test_chat_model_routes_by_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    settings = factory.Settings.from_env()
    assert isinstance(factory.chat_model(settings, "openrouter:x/y"), OpenRouterModel)
    assert not isinstance(factory.chat_model(settings, "qwen2.5:14b"), OpenRouterModel)


def test_judge_v2_keeps_reasons_in_the_trace() -> None:
    assert "ANSWERABLE cases" in PROMPT_V2 and "{query!r}" in PROMPT_V2
    assert "reason" in json.dumps(schema_for(["S1"], "v2"))
    verdict = {"asked": "a fix for X", "decision": "ABSTAIN",
               "rejected": [{"source_id": "S1", "rule": "J2", "reason": "error Y, not X"}]}
    model = Model(["S1"], verdict)
    with tracing.recording() as data:
        draft = asyncio.run(JudgedSelector(model, prompt_version="v2").select("Fix X?", EVIDENCE))
    assert draft.quotes == []
    assert data["selector"]["judge"]["rejected"][0]["reason"] == "error Y, not X"
    assert data["selector"]["judge_prompt"] == "v2"


class Explaining(Model):
    async def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        if prompt.startswith("KIND: REFUSAL_REASON\n"):
            self.kinds.append("explain")
            return json.dumps({"reason": "sources cover product B, not A"})
        return await super().generate(prompt, schema)


def test_refusal_reason_is_recorded_and_changes_nothing() -> None:
    model = Explaining([], {"asked": "", "decision": "ANSWER", "rejected": []})
    with tracing.recording() as data:
        draft = asyncio.run(JudgedSelector(model, explain_refusal=True).select("Q?", EVIDENCE))
    assert draft.quotes == [] and "explain" in model.kinds
    assert data["selector"]["refusal_reason"] == "sources cover product B, not A"


def test_openrouter_retries_transient_errors_only(monkeypatch: pytest.MonkeyPatch) -> None:
    import agents.chap12.openrouter as orm

    async def no_sleep(_: float) -> None:
        return None

    monkeypatch.setattr(orm.asyncio, "sleep", no_sleep)
    calls: list[int] = []

    def flaky(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) < 3:
            return httpx.Response(503, json={"error": "busy"})
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"},
                                                      "finish_reason": "stop"}]})

    m = OpenRouterModel("openrouter:x/y", api_key="k", retries=2,
                        transport=httpx.MockTransport(flaky))
    assert asyncio.run(m.generate("p", {})) == "{}" and len(calls) == 3

    calls.clear()

    def bad_request(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(400, json={"error": "bad"})

    m = OpenRouterModel("openrouter:x/y", api_key="k", retries=2,
                        transport=httpx.MockTransport(bad_request))
    with pytest.raises(DependencyUnavailable):
        asyncio.run(m.generate("p", {}))
    assert len(calls) == 1
