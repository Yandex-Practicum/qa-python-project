import pytest

from praktikum.bun import Bun

from data.burger_data import BurgerData


class TestBun:

    @pytest.mark.parametrize(("name", "price"), [BurgerData.BUN_1, BurgerData.BUN_2, BurgerData.BUN_3])
    def test_bun_attributes(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(("name", "price"), [BurgerData.BUN_1, BurgerData.BUN_2, BurgerData.BUN_3])
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(("name", "price"), [BurgerData.BUN_1, BurgerData.BUN_2, BurgerData.BUN_3])
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
