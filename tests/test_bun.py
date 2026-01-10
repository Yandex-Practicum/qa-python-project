import allure
from data import *


class TestBun:

    @allure.title('Проверка метода получения названия булки get_name')
    def test_get_bun_name(self, mock_bun):
        assert mock_bun.get_name() == Data1.bun_name

    @allure.title('Проверка метода получения стоимости булки get_price')
    def test_get_bun_price(self, mock_bun_2):
        assert mock_bun_2.get_price() == Data2.bun_price