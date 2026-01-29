from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_price_correct_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'TestIngredientName', 100)

        assert ingredient.get_price() == 100

    def test_get_name_correct_name_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'TestIngredientName', 100)

        assert ingredient.get_name() == 'TestIngredientName'

    def test_get_type_correct_type_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'TestIngredientName', 100)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
