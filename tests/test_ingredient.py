from praktikum_app.data import Data
from praktikum_app.ingredient_types import INGREDIENT_TYPE_SAUCE
from src.ingredient import Ingredient


class TestIngredient:

    def test_get_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_price() == Data.SAUCE_PRICE

    def test_get_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_name() == Data.SAUCE_NAME

    def test_get_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
