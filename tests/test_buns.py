import pytest

from helpers import BUN_NAME_1, BUN_NAME_2, BUN_PRICE
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", [BUN_NAME_1, BUN_NAME_2])
    def test_bun_name(self, name):
        # Проверяет, правильно ли устанавливается название булочки
        bun = Bun(name, BUN_PRICE)
        assert bun.get_name() == name, f"Название булочки '{bun.get_name()}' не соответствует ожидаемому '{name}'"

    def test_bun_price(self):
        # Проверяет, правильно ли устанавливается цена булочки
        bun = Bun(BUN_NAME_1, BUN_PRICE)
        assert bun.get_price() == BUN_PRICE, f"Цена булочки {bun.get_price()} не соответствует ожидаемой {BUN_PRICE}"
