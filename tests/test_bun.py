import pytest
import allure
from praktikum.bun import Bun
from data import Data, Data_0

class TestBun:
    @allure.title('Проверка метода get_name')
    @allure.description('С помощью метода получаем название булки')
    def test_get_name(self, mock_bun):
        assert mock_bun.get_name() == Data.bun_name

    @allure.title('Проверка метода get_price')
    @allure.description('С помощью метода получаем стоимость булки')
    def test_get_price(self, mock_bun):
        assert mock_bun.get_price() == Data.bun_price