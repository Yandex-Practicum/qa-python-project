from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price_returns_correct_float_value(self):
        ingredient = Ingredient("SAUCE", "ketchup", 30.0)

        assert ingredient.get_price() == 30.0

    def test_get_name_returns_correct_string_value(self):
        ingredient = Ingredient("SAUCE", "ketchup", 30.0)

        assert ingredient.get_name() == "ketchup"

    def test_get_type_returns_correct_type_string(self):
        ingredient = Ingredient("SAUCE", "ketchup", 30.0)

        assert ingredient.get_type() == "SAUCE"
        