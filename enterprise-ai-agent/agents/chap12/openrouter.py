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

import asyncio
import logging
import os
from typing import Any

import httpx

from agents.chap12.budget import CURRENT
from models.errors import DependencyUnavailable

LOGGER = logging.getLogger(__name__)
PREFIX = "openrouter:"
URL = "https://openrouter.ai/api/v1/chat/completions"


def is_openrouter(name: str) -> bool:
    return name.startswith(PREFIX)


class OpenRouterModel:
    def __init__(self, name: str, timeout: float | None = None,
                 transport: httpx.AsyncBaseTransport | None = None,
                 api_key: str | None = None, retries: int | None = None) -> None:
        self.model = name.removeprefix(PREFIX)
        self.timeout = timeout if timeout is not None else float(
            os.getenv("CHAP12_OPENROUTER_TIMEOUT", "180"))
        self.retries = retries if retries is not None else int(
            os.getenv("CHAP12_OPENROUTER_RETRIES", "0"))
        self.transport = transport
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

    async def _post(self, prompt: str, schema: dict[str, Any]) -> dict[str, Any]:
        """E9b (2026-11-07): retry transient failures (timeouts, connection errors, HTTP 429 and
        5xx) up to `retries` more times with a short back-off; anything else fails at once.
        One budgeted LLM call covers its retries."""
        delay = 2.0
        for attempt in range(self.retries + 1):
            try:
                async with httpx.AsyncClient(timeout=self.timeout,
                                             transport=self.transport) as client:
                    response = await client.post(URL, json=self.body(prompt, schema), headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "X-Title": "TechQA-Enterprise-RAG"})
                    response.raise_for_status()
                    data: dict[str, Any] = response.json()
                    if attempt:
                        LOGGER.info("OpenRouter %s ok after %d retries", self.model, attempt)
                    LOGGER.info("OpenRouter provider=%s", data.get("provider"))
                    return data
            except (httpx.TimeoutException, httpx.TransportError, httpx.HTTPStatusError) as exc:
                status = getattr(getattr(exc, "response", None), "status_code", None)
                transient = status is None or status == 429 or status >= 500
                if not transient or attempt == self.retries:
                    raise
                LOGGER.warning("OpenRouter %s attempt %d failed (%s); retrying", self.model,
                               attempt + 1, status or type(exc).__name__)
                await asyncio.sleep(delay)
                delay *= 2.5
        raise RuntimeError("unreachable")

    async def generate(self, prompt: str, schema: dict[str, Any]) -> str:
        try:
            data = await self._post(prompt, schema)
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
