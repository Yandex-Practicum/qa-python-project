from conftest import *
import allure


class TestIngredient:
    @allure.title('Тестирование метода get_name для получения названия соуса')
    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == BunData1.sauce_name

    @allure.title('Тестирование метода get_name для получения имени заполнения')
    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == BunData1.filling_name

    @allure.title('Тестирование метода get_price для получения цены на соус')
    def test_get_price_sauce_success(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == BunData2.sauce_price

    @allure.title('Тестирование метода get_price для получения цены начинки')
    def test_get_price_filling_success(self, mock_filling_2):
        assert mock_filling_2.get_price() == BunData2.filling_price

    @allure.title('Тестирование метода get_type для получения типа ингредиента соуса')
    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == BunData1.sauce_type

    @allure.title('Тестирование метода get_type для получения типа ингредиента начинки')
    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == BunData1.filling_type