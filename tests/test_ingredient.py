import pytest
import praktikum.ingredient_types

from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredients_name', ['tomato', 'P1neapple', '11', '',None])
    def test_get_name(self,ingredients_name):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, ingredients_name, 10.0)
        assert ingredient.get_name() == ingredients_name

    @pytest.mark.parametrize('prices', [10.0, 0.0, 1.7976931348623157e+308, 2.2250738585072014e-308])
    def test_gen_price(self, prices):
        ingredient = Ingredient(praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, 'chili', prices)
        assert ingredient.get_price() == prices

    @pytest.mark.parametrize('ingredient_type', [praktikum.ingredient_types.INGREDIENT_TYPE_FILLING,
                                                 praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'lime', 10.0)
        assert ingredient.get_type() == ingredient_type
