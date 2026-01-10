import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [('Бургер', 0.1), ('burger', 100), ('123456', '100000000000000')])
    def test_get_name_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [('Бургер', 0.1), ('burger', 100), ('123456', '100000000000000')])
    def test_get_price_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() ==  price
