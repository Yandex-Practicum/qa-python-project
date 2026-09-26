import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            'SAUCE',
            'FILLING',
        ]
    )
    def test_get_type_returns_correct_type(
        self,
        ingredient_type
    ):
        ingredient = Ingredient(
            ingredient_type,
            'Hot sauce',
            50
        )

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        'name',
        [
            'Hot sauce',
            'Cutlet',
            'Cheese sauce',
        ]
    )
    def test_get_name_returns_correct_name(self, name):
        ingredient = Ingredient(
            'SAUCE',
            name,
            50
        )

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        'price',
        [
            50,
            100,
            75.5,
        ]
    )
    def test_get_price_returns_correct_price(self, price):
        ingredient = Ingredient(
            'SAUCE',
            'Hot sauce',
            price
        )

        assert ingredient.get_price() == price