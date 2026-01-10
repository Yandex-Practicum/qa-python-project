import pytest
import data
from praktikum.bun import Bun


class TestBun:

    # Проверка работы метода get_name объекта класса Bun
    @pytest.mark.parametrize('name, price', data.buns_list())
    def test_get_name_all_types(self, name, price):
        bun_test = Bun(name, price)
        expected_name = name
        assert bun_test.get_name() == expected_name, f'bun_test_name = {expected_name}'

    # Проверка работы метода get_price объекта класса Bun
    @pytest.mark.parametrize('name, price', data.buns_list())
    def test_get_price_all_types(self, name, price):
        bun_test = Bun(name, price)
        expected_price = price
        assert bun_test.get_price() == expected_price, f'bun_test_price = {expected_price}'
