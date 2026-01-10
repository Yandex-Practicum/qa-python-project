import allure

from praktikum.bun import Bun
from data import Data


class TestBun:

    @allure.title('Проверка получения имени булочки')
    @allure.description('Проверяем, что возможно получить имя булочки методом get_name')
    def test_get_name_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME

    @allure.title('Проверка получения цены булочки')
    @allure.description('Проверяем, что возможно получить цену булочки методом get_price')
    def test_get_price_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE
