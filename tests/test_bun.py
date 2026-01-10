from bun import Bun
from data import Data
import allure


class TestBun:

    @allure.title('Получение имени булочки через метод get_name')
    def test_get_name_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_name() == Data.BUN_NAME

    @allure.title('Получения цены булочки через метод get_price')
    def test_get_price_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_price() == Data.BUN_PRICE
