import allure
from praktikum.bun import Bun
from data import Data


class TestBun:

    @allure.title('Проверка получения имени булки')
    @allure.description('Проверяем, что можно получить имя булки методом get_name')
    def test_get_name_bun(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_name() == Data.BUN_NAME

    @allure.title('Проверка получения цены булочки')
    @allure.description('Проверяем, что можно получить цену булочки методом get_price')
    def test_get_price_bun(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_price() == Data.BUN_PRICE
