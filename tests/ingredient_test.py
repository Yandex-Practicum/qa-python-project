import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Юнит-тесты для класса Ingredient."""

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_SAUCE, 'sour cream', 200.5),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 300),
        (INGREDIENT_TYPE_FILLING, 'dinosaur', 0),
    ])
    def test_ingredient_init(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize('price', [0, 100, 150.25, 999])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sauce', price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', ['hot sauce', 'cutlet', 'dinosaur'])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, 100)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'name', 100)

        assert ingredient.get_type() == ingredient_type
