import allure
from praktikum.bun import Bun
from data import BUN_NAME, BUN_PRICE

class TestBun:
    @allure.title('Получение названия булочки')
    def test_get_name(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_name() == BUN_NAME

    @allure.title('Получение цены булочки')
    def test_get_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_price() == BUN_PRICE
