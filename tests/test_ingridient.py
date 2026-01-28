import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngridient:
    @pytest.mark.parametrize('ingredient, name, price',
                             [
                                 (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 9.0),
                                 (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337.0)
                             ]
                             )
    def test_get_price(self, ingredient, name, price):
        ingredient = Ingredient(ingredient_type=type, name=name, price=price)
        expected_price = ingredient.get_price()
        assert expected_price == price

    @pytest.mark.parametrize('ingredient, name, price',
                             [
                                 (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 9.0),
                                 (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337.0)
                             ]
                             )
    def test_get_name(self, ingredient, name, price):
        ingredient = Ingredient(ingredient_type=type, name=name, price=price)
        expected_name = ingredient.get_name()
        assert expected_name == name

    @pytest.mark.parametrize('ingredient, name, price',
                             [
                                 (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 9.0),
                                 (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337.0)
                             ]
                             )
    def test_get_type(self, ingredient, name, price):
        ingredient = Ingredient(ingredient_type=type, name=name, price=price)
        expected_type = ingredient.get_type()
        assert expected_type == type





