"""E8 (2026-11-05): selection / judge calls on a larger hosted model through OpenRouter.

Same interface as TokenMeteredOllamaModel (`generate(prompt, schema) -> str`), so it can stand in
for the 7B selection or the 14B judge without touching their prompts. Requests go to the
OpenAI-compatible endpoint https://openrouter.ai/api/v1/chat/completions with the JSON schema as
`response_format` and `provider.require_parameters = true`, so OpenRouter only routes to
providers that honour structured output. Temperature 0 except for OpenAI reasoning models
(openai/gpt-5*), which do not accept it. The API key is read from the OPENROUTER_API_KEY
environment variable and never written anywhere. Token usage is recorded like Ollama's.

A model is selected with an "openrouter:" prefix in CHAP12_SELECTOR_MODEL / CHAP12_JUDGE_MODEL /
CHAP12_SELECT_FALLBACK, e.g. "openrouter:qwen/qwen-2.5-72b-instruct".
"""

from __future__ import annotations

import os
from typing import Any

import httpx

from agents.chap12.budget import CURRENT
from models.errors import DependencyUnavailable

PREFIX = "openrouter:"
URL = "https://openrouter.ai/api/v1/chat/completions"


def is_openrouter(name: str) -> bool:
    return name.startswith(PREFIX)


class OpenRouterModel:
    def __init__(self, name: str, timeout: float = 180,
                 transport: httpx.AsyncBaseTransport | None = None,
                 api_key: str | None = None) -> None:
        self.model = name.removeprefix(PREFIX)
        self.timeout, self.transport = timeout, transport
        self.api_key = api_key if api_key is not None else os.getenv("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise DependencyUnavailable("OPENROUTER_API_KEY is not set")

    def body(self, prompt: str, schema: dict[str, Any]) -> dict[str, Any]:
        body: dict[str, Any] = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_schema", "json_schema": {
                "name": "answer", "strict": False, "schema": schema}},
            "provider": {"require_parameters": True},
        }
        if not self.model.startswith("openai/gpt-5"):
            body["temperature"] = 0
        return body

    async def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        try:
            async with httpx.AsyncClient(timeout=self.timeout, transport=self.transport) as client:
                response = await client.post(URL, json=self.body(prompt, schema), headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "X-Title": "TechQA-Enterprise-RAG E8"})
                response.raise_for_status()
                data = response.json()
                usage = data.get("usage") or {}
                active = CURRENT.get()
                if active is not None:
                    active[0].record_tokens(usage.get("prompt_tokens"),
                                            usage.get("completion_tokens"))
                choice = data["choices"][0]
                if choice.get("finish_reason") == "length":
                    raise ValueError("structured generation exceeded its token budget")
                content = choice["message"]["content"]
                if not isinstance(content, str):
                    raise ValueError("model content must be a string")
                return content.strip().removeprefix("```json").removesuffix("```").strip()
        except (httpx.HTTPError, KeyError, IndexError, ValueError, TypeError) as exc:
            raise DependencyUnavailable(f"OpenRouter generation failed ({self.model})") from exc
