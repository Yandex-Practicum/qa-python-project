import data
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(data.ingredient_type, data.ingredient_name, data.ingredient_price)
        assert ingredient.get_price() == data.ingredient_price

    def test_get_name(self):
        ingredient = Ingredient(data.ingredient_type, data.ingredient_name, data.ingredient_price)
        assert ingredient.get_name() == data.ingredient_name

    def test_get_type(self):
        ingredient = Ingredient(data.ingredient_type, data.ingredient_name, data.ingredient_price)
        assert ingredient.get_type() == data.ingredient_type
