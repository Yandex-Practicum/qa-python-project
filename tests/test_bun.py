from conftest import *
import allure


class TestBun:

    @allure.title('Проверка работы метода get_name, который получает название булки')
    def test_get_name_bun_success(self, mock_bun):
        assert mock_bun.get_name() == Data1.bun_name

    @allure.title('Проверка работы метода get_price, который получает стоимость булки')
    def test_get_price_bun_success(self, mock_bun_2):
        assert mock_bun_2.get_price() == Data2.bun_price