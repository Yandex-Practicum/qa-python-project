import pytest
import data
from praktikum.ingredient import Ingredient


class TestIngredient:

    # Проверка работы метода get_name объекта класса Ingredient
    @pytest.mark.parametrize('i_type, name, price', data.ingredients_list())
    def test_get_name_all_types(self, i_type, name, price):
        ingredient_test = Ingredient(i_type, name, price)
        expected_name = name
        assert ingredient_test.get_name() == expected_name, f'ingredient_test_name = {expected_name}'

    # Проверка работы метода get_price объекта класса Ingredient
    @pytest.mark.parametrize('i_type, name, price', data.ingredients_list())
    def test_get_price_all_types(self, i_type, name, price):
        ingredient_test = Ingredient(i_type, name, price)
        expected_price = price
        assert ingredient_test.get_price() == expected_price, f'bun_test_price = {expected_price}'

    # Проверка работы метода get_type объекта класса Ingredient
    @pytest.mark.parametrize('i_type, name, price', data.ingredients_list())
    def test_get_type_all_types(self, i_type, name, price):
        ingredient_test = Ingredient(i_type, name, price)
        expected_type = i_type
        assert ingredient_test.get_type() == expected_type, f'bun_test_type = {expected_type}'
