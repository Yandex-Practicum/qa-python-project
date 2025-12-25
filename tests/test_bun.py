import pytest
from praktikum.bun import Bun
from tests.test_data import BUNS_DATA

class TestBun:

    @pytest.mark.parametrize("name, price", BUNS_DATA)
    def test_get_name_and_price_valid(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price

