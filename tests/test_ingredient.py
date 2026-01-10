from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_get_name_returns_name(self):
        expected_name = "Name"
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, expected_name, 1.0)
        assert ingredient.get_name() == expected_name

    def test_get_price_returns_price(self):
        expected_price = 1.0
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Name", expected_price)
        assert ingredient.get_price() == expected_price

    def test_get_type_returns_type(self):
        expected_type = INGREDIENT_TYPE_SAUCE
        ingredient = Ingredient(expected_type, "Name", 1.0)
        assert ingredient.get_type() == expected_type