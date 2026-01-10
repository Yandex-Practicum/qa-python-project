from praktikum.ingredient import Ingredient
from data import Data


class TestIngredient:
    def test_get_price_correct_price(self):
        ingredient = Ingredient(Data.INGREDIENT_1_TYPE, Data.INGREDIENT_1_NAME, Data.INGREDIENT_1_PRICE)
        assert ingredient.get_price() == 100

    def test_get_name_correct_name(self):
        ingredient = Ingredient(Data.INGREDIENT_1_TYPE, Data.INGREDIENT_1_NAME, Data.INGREDIENT_1_PRICE)
        assert ingredient.get_name() == 'ingredient_1'

    def test_get_type_correct_type(self):
        ingredient = Ingredient(Data.INGREDIENT_1_TYPE, Data.INGREDIENT_1_NAME, Data.INGREDIENT_1_PRICE)
        assert ingredient.get_type() == 'SAUCE'
