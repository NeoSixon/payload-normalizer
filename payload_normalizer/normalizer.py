"""Normalization helpers for API payload metadata."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def normalize_tags(tags: Iterable[str | None]) -> list[str]:
    """Return normalized unique tags in first-seen order.

    Tags are trimmed, lowercased, and blank or ``None`` entries are ignored.
    """
    normalized = {
        tag.strip().lower()
        for tag in tags
        if tag.strip()
    }
    return sorted(normalized)


def normalize_payload(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Return a shallow normalized copy of a metadata payload."""
    result = dict(payload)
    tags = payload.get("tags")
    if tags is not None:
        result["tags"] = normalize_tags(tags)
    return result
