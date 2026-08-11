import builtins
from unittest.mock import Mock

import pytest

import praktikum


def test_main_builds_burger_using_database_and_prints_receipt(monkeypatch):
    fake_bun = Mock(get_name=Mock(return_value="dummy bun"), get_price=Mock(return_value=10.0))
    fake_ingredient = Mock(
        get_type=Mock(return_value="FILLING"),
        get_name=Mock(return_value="dummy filling"),
        get_price=Mock(return_value=5.0),
    )
    fake_database = Mock(
        available_buns=Mock(return_value=[fake_bun]),
        available_ingredients=Mock(return_value=[fake_ingredient] * 6),
    )

    monkeypatch.setattr(praktikum, "Database", Mock(return_value=fake_database))

    printed_lines = []

    def fake_print(*args, **kwargs):
        printed_lines.append(" ".join(str(item) for item in args))

    monkeypatch.setattr(builtins, "print", fake_print)

    praktikum.main()

    assert any("dummy bun" in line for line in printed_lines)
    assert any("dummy filling" in line for line in printed_lines)
    assert any("Price:" in line for line in printed_lines)
