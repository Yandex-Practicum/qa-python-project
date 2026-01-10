from conftest import mock_sauce, mock_filling
from data import TestBurgerData
import allure


@allure.suite('Тестирование класса - Ingredients')
class TestIngredients:

    @allure.title('Проверка получения названия соуса - get_name')
    def test_get_name_sauce_is_success(self, mock_sauce):
        assert mock_sauce.get_name() == TestBurgerData.sauce_name

    @allure.title('Проверка получения стоимости соуса - get_price')
    def test_get_price_sauce_is_success(self, mock_sauce):
        assert mock_sauce.get_price() == TestBurgerData.sauce_price

    @allure.title('Проверка получения типа начинки соуса - get_type')
    def test_get_type_sauce_is_success(self, mock_sauce):
        assert mock_sauce.get_type() == TestBurgerData.sauce_type

    @allure.title('Проверка получения названия начинки - get_name')
    def test_get_name_filling_is_success(self, mock_filling):
        assert mock_filling.get_name() == TestBurgerData.filling_name

    @allure.title('Проверка получения стоимости начинки - get_price')
    def test_get_price_filling_is_success(self, mock_filling):
        assert mock_filling.get_price() == TestBurgerData.filling_price

    @allure.title('Проверка получения типа начинки - get_type')
    def test_get_type_filling_is_success(self, mock_filling):
        assert mock_filling.get_type() == TestBurgerData.filling_type