import pytest
from praktikum.bun import Bun


class TestBun:
    list_data_name = ["black bun", "white bun", "red bun" "", "1", "b"]
    list_data_price = [100.0, 0.0, 0.01, 999.99]

    @pytest.mark.parametrize("name", list_data_name)
    def test_names_bun(self, name):
        price = 369.0
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", list_data_price)
    def test_price_buns(self, price):
        name = "red bun"
        bun = Bun(name, price)

        assert bun.get_price() == price

    def test_making_buns(self):
        bun = Bun("red bun", 369.0)

        assert bun.get_name() == "red bun"
        assert bun.get_price() == 369.0