import pytest
import allure

from praktikum.bun import Bun
from data import TestData


@pytest.mark.parametrize("name, price", [TestData.buns[0], TestData.buns[1]])
class TestBun:

    @allure.title("Проверка получения названия булочки")
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @allure.title("Проверка получения цены булочки")
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
