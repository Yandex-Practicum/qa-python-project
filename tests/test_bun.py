from conftest import mock_bun
from data import TestBurgerData
import allure


@allure.suite('Тестирование класса - Buns')
class TestBun():

    @allure.title('Проверка получения названия булки - get_name')
    def test_get_bun_name(self, mock_bun):
        assert mock_bun.get_name() == TestBurgerData.bun_name

    @allure.title('Проверка получения стоимости булки - get_price')
    def test_get_bun_price(self, mock_bun):
        assert mock_bun.get_price() == TestBurgerData.bun_price

