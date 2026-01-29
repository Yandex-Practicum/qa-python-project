import allure
import pytest
from praktikum.ingredient import Ingredient


class TestIngredientsMethods:
    """
    ТЕСТЫ МЕТОДОВ КЛАССА Ingredient
    """
    @pytest.mark.parametrize('name, price, check_output_value', [
        ('Салат', 2.50, 2.50),
        ('Мясо', 7.20, 7.20)
    ])
    @allure.title('get_price() - получение цены ингредиента')
    @allure.description('Проверяем, что выводится цена ингредиента')
    def test_get_price(self, name, price, check_output_value):
        ingredient = Ingredient('Майонез', name, price)
        assert ingredient.get_price() == check_output_value

    @allure.title('get_name() - получение названия ингредиента')
    @allure.description('Проверяем, что выводится название ингредиента')
    def test_get_name(self):
        ingredient = Ingredient('Соус', 'Кетчуп', 0.50)
        assert ingredient.get_name() == 'Кетчуп'

    @allure.title('get_type() - получение названия ингредиента')
    @allure.description('Проверяем, что выводится название ингредиента')
    def test_get_type(self):
        ingredient = Ingredient('Овощи', 'Огурец', 0.20)
        assert ingredient.get_type() == 'Овощи'
