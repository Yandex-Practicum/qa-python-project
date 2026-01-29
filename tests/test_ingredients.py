from .. data import Helpers
from .. praktikum.ingredient import Ingredient

class TestIngredients:

    def test_get_ingredient_type(self):
        ingredients = Ingredient(Helpers.INGREDIENT_TYPE, Helpers.INGREDIENT_NAME, Helpers.INGREDIENT_PRICE)
        assert ingredients.get_type() == Helpers.INGREDIENT_TYPE

    def test_get_ingredient_price_(self):
        ingredients = Ingredient(Helpers.INGREDIENT_TYPE, Helpers.INGREDIENT_NAME, Helpers.INGREDIENT_PRICE)
        assert ingredients.get_price() == Helpers.INGREDIENT_PRICE

    def test_get_ingredient_name(self):
        ingredients = Ingredient(Helpers.INGREDIENT_TYPE, Helpers.INGREDIENT_NAME, Helpers.INGREDIENT_PRICE)
        assert ingredients.get_name() == Helpers.INGREDIENT_NAME