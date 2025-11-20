import allure

import data
from praktikum.bun import Bun


class TestBun:
    @allure.title('Проверка получения названия булки')
    def test_get_name_expected_name_ok(self):
        bun = Bun(data.bun[0], data.bun[1])
        assert bun.get_name() == data.bun[0]

    @allure.title('Проверка получения цены булки')
    def test_get_price_expected_price_ok(self):
        bun = Bun(data.bun[0], data.bun[1])
        assert bun.get_price() == data.bun[1]
