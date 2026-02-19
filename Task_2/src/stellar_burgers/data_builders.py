from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class UserCredentials:
    email: str
    password: str
    name: str


def build_unique_user() -> UserCredentials:
    unique = uuid4().hex
    return UserCredentials(
        email=f"autotest_{unique}@yandex.ru",
        password=f"pass_{unique}",
        name=f"User_{unique[:8]}",
    )
