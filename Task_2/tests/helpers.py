from __future__ import annotations

from typing import Dict, List
from uuid import uuid4

import allure

from stellar_burgers.api_client import StellarApiClient


def get_ingredient_ids(api: StellarApiClient, limit: int = 2) -> List[str]:
    with allure.step("Get ingredients list"):
        resp = api.get("/ingredients")
    assert resp.status_code == 200
    assert resp.json.get("success") is True
    data = resp.json.get("data") or []
    ids = [item["_id"] for item in data if isinstance(item, dict) and "_id" in item]
    assert len(ids) >= limit, "Not enough ingredients returned by API"
    return ids[:limit]


def auth_header(access_token: str) -> Dict[str, str]:
    return {"Authorization": access_token}


def random_email(prefix: str = "autotest") -> str:
    """Generate a unique email to avoid collisions on a shared test stand."""
    return f"{prefix}_{uuid4().hex}@yandex.ru"
