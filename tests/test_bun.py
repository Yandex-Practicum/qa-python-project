import pytest
from praktikum.bun import Bun
from data.bun_data import get_bun_test_data


class TestBun:

    def test_bun_creation_name_and_price(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"
        assert bun.price == 100

    def test_get_name_returns_correct_name(self):
        bun = Bun("white bun", 200)
        assert bun.get_name() == "white bun"

    def test_get_price_returns_correct_price(self):
        bun = Bun("red bun", 300)
        assert bun.get_price() == 300

    @pytest.mark.parametrize("name,price", get_bun_test_data())
    def test_bun_creation_with_different_parameters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price