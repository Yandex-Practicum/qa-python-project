import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_name() == 'Соус Spicy-X'

    def test_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        assert ingredient.get_price() == 90

    @pytest.mark.parametrize(
        'type, name, price, added_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424, 'FILLING']
        ]
    )
    def test_get_ingredient_type(self, type, name, price, added_ingredient):
        ingredient = Ingredient(type,name, price)
        assert ingredient.get_type() == added_ingredient

