import pytest
from praktikum.bun import Bun


class TestBun:
    list_data_name = ["black bun", "white bun", "", "1", "b"]
    list_data_price = [100.0, 0.0, 0.01, 999.99]

    @pytest.mark.parametrize("name", list_data_name)
    def test_bun_names(self, name):
        price = 99.0
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", list_data_price)
    def test_bun_price(self, price):
        name = "black bun"
        bun = Bun(name, price)

        assert bun.get_price() == price
