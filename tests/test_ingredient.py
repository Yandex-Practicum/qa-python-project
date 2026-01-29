import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    # Тест на получение цены на ингридиент
    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_price() == 90

    # Тест на получение наименования ингридиента
    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    # Тест на получение типа ингридиента
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
