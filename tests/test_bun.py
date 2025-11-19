import pytest
import allure
from praktikum.bun import Bun
from data import buns_name_price
from helpers import *

class TestBun:

    @pytest.mark.parametrize("mock_bun", buns_name_price, indirect=True)
    @allure.title("Тест получения названия булочки")
    def test_bun_get_name(self, mock_bun):
        bun = Bun(name=mock_bun.name, price=mock_bun.price)
        TestTools.check_unit_test_result(expected_value=mock_bun.name, actually_value=bun.get_name())

    @pytest.mark.parametrize("mock_bun", buns_name_price, indirect=True)
    @allure.title("Тест получения цены булочки")
    def test_bun_get_price(self, mock_bun):
        bun = Bun(name=mock_bun.name, price=mock_bun.price)
        TestTools.check_unit_test_result(expected_value=mock_bun.price, actually_value=bun.get_price())



