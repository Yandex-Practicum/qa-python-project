import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['SAUCE', 'Соус традиционный галактический', 15.5],
            ['FILLING', 'Мясо бессмертных моллюсков Protostomia', 250.6]
        ]
    )
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['SAUCE', 'Соус традиционный галактический', 15.5],
            ['FILLING', 'Мясо бессмертных моллюсков Protostomia', 250.6]
        ]
    )
    def test_get_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['SAUCE', 'Соус традиционный галактический', 15.5],
            ['FILLING', 'Мясо бессмертных моллюсков Protostomia', 250.6]
        ]
    )
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
