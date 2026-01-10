from praktikum.bun import Bun
import pytest


class TestBun:

    # Проверка получения названия
    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 99),
        ("Краторная булка N-200i", 999),])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Проверка получения цены
    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 99),
        ("Краторная булка N-200i", 999),])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
