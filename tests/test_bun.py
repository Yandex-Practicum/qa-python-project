import allure
from conftest import *
from data import DataOne

class TestBun:
    @allure.title('Проверка метода get_name')
    def test_get_name_bun_works_correctly(self, mock_bun_one):
        assert mock_bun_one.get_name() == DataOne.BUN_NAME

    @allure.title('Проверка метода get_price')
    def test_get_price_bun_works_correctly(self, mock_bun_one):
        assert mock_bun_one.get_price() == DataOne.BUN_PRICE
