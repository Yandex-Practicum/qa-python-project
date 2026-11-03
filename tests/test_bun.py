import pytest

from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200.5),
            ("", 0),
            ("Очень длинное название булочки с пробелами", 999.99),
            ("bun 🥯", 1e3),
        ],
        ids=["standard", "float_price", "empty_zero", "long_name", "emoji_exp"],
    )
    def test_bun_stores_and_returns_data(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price