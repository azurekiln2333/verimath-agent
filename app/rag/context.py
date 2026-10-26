"""Resolve short follow-ups for retrieval without changing the model's user turn."""
from __future__ import annotations

import re
from collections.abc import Sequence

from app.model_client import ModelMessage
from app.rag.store import build_query_terms, domain_query_terms


_REFERENCE = re.compile(r"这(?:里|个|些|一步|几步|样)|那(?:里|个|些|一步|样)|它|上述|刚才|上面|前面|继续|接着")
_NEW_TOPIC = re.compile(r"换.{0,3}话题|换.{0,3}问题|另外.{0,3}问题|改问|不谈|不讨论")


def retrieval_query(query: str, history: Sequence[ModelMessage] | None = None) -> str:
    """Only inherit a recent topic for a reference or a topic-free follow-up."""
    if not history or _NEW_TOPIC.search(query):
        return query
    if not _REFERENCE.search(query) and build_query_terms(query):
        return query
    inherited: list[str] = []
    recent_answer = ""
    for message in reversed(history[-8:]):
        if not isinstance(message.content, str):
            continue
        if message.role == "assistant" and not recent_answer:
            recent_answer = message.content[:1800]
        if message.role != "user":
            continue
        topic = domain_query_terms(message.content)
        if topic:
            inherited.extend(topic[:4])
            break
        if _NEW_TOPIC.search(message.content):
            break
        # Unknown but explicit subjects should also terminate the search rather
        # than borrowing an unrelated topic from earlier in the conversation.
        words = build_query_terms(message.content)
        if words and not _REFERENCE.search(message.content):
            inherited.extend(words[:3])
            break
    inherited.extend(domain_query_terms(recent_answer)[:4])
    terms = list(dict.fromkeys(inherited))[:6]
    return query + "\n" + " ".join(terms) if terms else query
