from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

from .config import API_PREFIX, BASE_URL


@dataclass(frozen=True)
class ApiResponse:
    status_code: int
    json: Dict[str, Any]


class StellarApiClient:
    """Thin wrapper over requests for Stellar Burgers API."""

    def __init__(self, base_url: str = BASE_URL) -> None:
        self._base_url = base_url.rstrip("/")
        self._session = requests.Session()

    def _url(self, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{self._base_url}{API_PREFIX}{path}"

    def get(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        r = self._session.get(self._url(path), headers=headers)
        return ApiResponse(status_code=r.status_code, json=_safe_json(r))

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ApiResponse:
        r = self._session.post(self._url(path), json=json, headers=headers)
        return ApiResponse(status_code=r.status_code, json=_safe_json(r))

    def patch(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ApiResponse:
        r = self._session.patch(self._url(path), json=json, headers=headers)
        return ApiResponse(status_code=r.status_code, json=_safe_json(r))

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        r = self._session.delete(self._url(path), headers=headers)
        return ApiResponse(status_code=r.status_code, json=_safe_json(r))


def _safe_json(response: requests.Response) -> Dict[str, Any]:
    try:
        return response.json()
    except Exception:
        return {}
