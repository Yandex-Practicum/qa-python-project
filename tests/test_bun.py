import allure
from data import Data


class TestBun:

    @allure.title('Проверка получения имени булочки, через метод get_name')
    def test_get_name_bun(self, mock_bun):
        assert mock_bun.get_name() == Data.Bun_name

    @allure.title('Проверка получения стоимости булочки, через метод get_price')
    def test_get_price_bun(self, mock_bun):
        assert mock_bun.get_price() == Data.Bun_price


