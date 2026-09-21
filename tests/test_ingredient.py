import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200.5),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 0),
            (INGREDIENT_TYPE_FILLING, 'sausage', 300.99),
        ]
    )
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
        ]
    )
    def test_ingredient_get_type_returns_correct_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type=ingredient_type, name='test_ingredient', price=100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        'name',
        [
            'chili sauce',
            'cheese filling',
        ]
    )
    def test_ingredient_get_name_returns_correct_name(self, name):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=name, price=50)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        'price',
        [
            0,
            150.5,
            999,
        ]
    )
    def test_ingredient_get_price_returns_correct_price(self, price):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name='cutlet', price=price)
        assert ingredient.get_price() == price
