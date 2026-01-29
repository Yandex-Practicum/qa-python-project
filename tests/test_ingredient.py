from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Первый", 3)
        assert ingredient.get_price() == 3

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "Второй", 2)
        assert ingredient.get_name() == "Второй"

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Третий", 1)
        assert ingredient.get_type() == "SAUCE"