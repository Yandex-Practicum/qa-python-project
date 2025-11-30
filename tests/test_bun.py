import allure

from praktikum import Bun
from helpers.helpers import *


class TestBun:
    @allure.title("Проверка получения названия булочки")
    def test_get_name(self):
        name = generate_random_string(10)
        price = float(random.randint(1, 1000))
        bun = Bun(name, price)
        assert bun.get_name() == name

    @allure.title("Проверка получения цены булочки")
    def test_get_price(self):
        name = generate_random_string(10)
        price = float(random.randint(1, 1000))
        bun = Bun(name, price)
        assert bun.get_price() == price


