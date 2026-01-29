import allure
from conftest import *

class TestBun:

    @allure.title('Проверка метода get_name для получения имени булочки')
    def test_verify_get_name_success(self, mock_bun):
        assert mock_bun.get_name() == BunData1.bun_name

    @allure.title('Проверка метода get_price для получения цены булочки')
    def test_verify_get_price_success(self, mock_bun_2):
        assert mock_bun_2.get_price() == BunData2.bun_price