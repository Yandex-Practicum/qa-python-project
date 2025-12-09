import pytest
from praktikum.bun import Bun
import data


class TestBun:

    @pytest.mark.parametrize('the_bun, the_price', data.available_buns)
    def test_get_name_true(self, the_bun, the_price):
        bun = Bun(the_bun, the_price)
        actual_result = bun.get_name()

        assert actual_result == bun.name

    @pytest.mark.parametrize('the_bun, the_price', data.available_buns)
    def test_get_price_true(self, the_bun, the_price):
        bun = Bun(the_bun, the_price)
        actual_result = bun.get_price()

        assert actual_result == bun.price