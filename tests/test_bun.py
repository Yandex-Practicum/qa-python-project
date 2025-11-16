import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name,price',[('Флюорисцентная булка', 988), ('Краторная булка', 1255)])
    def test_name_and_price_of_bun_true(self, name, price):
        bun = Bun(name,price)
        assert bun.name == name and bun.price == price

    @pytest.mark.parametrize('name,price', [('Флюорисцентная булка', 988), ('Краторная булка', 1255)])
    def test_get_name_true(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price

