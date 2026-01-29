import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000)

        assert ingredient.get_name() == 'Говяжий метеорит (отбивная)'

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)

        assert ingredient.get_price() == 90

    @pytest.mark.parametrize(
        'ingredient_type,name,price',
        [
            (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000),
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90)
        ]
    )
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
