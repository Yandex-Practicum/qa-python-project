import pytest
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as IngredientTypes


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price, expected_value', [[IngredientTypes.INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 100],
                                                                   [IngredientTypes.INGREDIENT_TYPE_FILLING,"dinosaur", 200, 200]])

    def test_ingredients_get_price(self, ingredient_type, name, price, expected_value):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_value

    @pytest.mark.parametrize('ingredient_type, name, price, expected_value',
                             [[IngredientTypes.INGREDIENT_TYPE_SAUCE, "hot sauce", 100, "hot sauce"],
                              [IngredientTypes.INGREDIENT_TYPE_FILLING, "dinosaur", 200, "dinosaur"]])
    def test_ingredients_get_name(self, ingredient_type, name, price, expected_value):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_value

    @pytest.mark.parametrize('ingredient_type, name, price, expected_value',
                             [[IngredientTypes.INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 'SAUCE'],
                              [IngredientTypes.INGREDIENT_TYPE_FILLING, "dinosaur", 200, 'FILLING']])
    def test_ingredients_get_type(self, ingredient_type, name, price, expected_value):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_value
