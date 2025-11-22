from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_type_sauce_name_price_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE and ingredient.name == 'hot sauce' and ingredient.price == 100

    def test_ingredient_type_filling_name_price_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 100)
        assert ingredient.type == INGREDIENT_TYPE_FILLING and ingredient.name == 'cutlet' and ingredient.price == 100

    def test_get_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert Ingredient.get_price(ingredient) == 100

    def test_get_name_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert Ingredient.get_name(ingredient) == 'hot sauce'

    def test_get_type_sauce_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert Ingredient.get_type(ingredient) == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'hot sauce', 100)
        assert Ingredient.get_type(ingredient) == INGREDIENT_TYPE_FILLING


