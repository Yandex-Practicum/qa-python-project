import allure

from data import TestBunData
from praktikum.bun import Bun


class TestBun:
    @allure.title("Получение корректного названия булочки")
    def test_get_correct_bun_name(self):
        test_bun = Bun(TestBunData.name, TestBunData.price)
        assert test_bun.get_name() == TestBunData.name

    @allure.title("Получение корректной цены булочки")
    def test_get_correct_bun_price(self):
        test_bun = Bun(TestBunData.name, TestBunData.price)
        assert test_bun.get_price() == TestBunData.price