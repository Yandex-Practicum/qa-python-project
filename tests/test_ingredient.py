from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_type_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_price_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_get_type_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING