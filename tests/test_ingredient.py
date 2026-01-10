from data import *
import allure


class TestIngredient:
    @allure.title('Проверка метода получения стоимости соуса get_price')
    def test_get_sauce_price(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == Data2.sauce_price

    @allure.title('Проверка метода получения стоимости начинки get_price')
    def test_get_filling_price(self, mock_filling_2):
        assert mock_filling_2.get_price() == Data2.filling_price

    @allure.title('Проверка метода получения названия соуса get_name')
    def test_get_sauce_name(self, mock_sauce):
        assert mock_sauce.get_name() == Data1.sauce_name

    @allure.title('Проверка метода получения названия начинки get_name')
    def test_get_filling_name(self, mock_filling):
        assert mock_filling.get_name() == Data1.filling_name

    @allure.title('Проверка метода получения типа ингредиента для соуса get_type')
    def test_get_type_sauce(self, mock_sauce):
        assert mock_sauce.get_type() == Data1.sauce_type

    @allure.title('Проверка метода получения типа ингредиента для начинки get_type')
    def test_get_type_filling(self, mock_filling):
        assert mock_filling.get_type() == Data1.filling_type