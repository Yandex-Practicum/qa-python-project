from conftest import *
import allure


class TestIngredient:
    @allure.title('Проверка метода get_name, получающего название соуса')
    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == Data1.sauce_name

    @allure.title('Проверка метода get_name, получающего название начинки')
    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == Data1.filling_name

    @allure.title('Проверка метода get_price, получающего стоимость соуса')
    def test_get_price_sauce_success(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == Data2.sauce_price

    @allure.title('Проверка метода get_price, получающего стоимость начинки')
    def test_get_price_filling_success(self, mock_filling_2):
        assert mock_filling_2.get_price() == Data2.filling_price

    @allure.title('Проверка метода get_type, получающего тип ингредиента для соуса')
    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == Data1.sauce_type

    @allure.title('Проверка метода get_type, получающего тип ингредиента для начинки')
    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == Data1.filling_type
