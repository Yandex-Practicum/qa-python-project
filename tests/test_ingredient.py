from praktikum.ingredient import Ingredient
from data import Data


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(Data.IngredientType1, Data.IngredientName1, Data.IngredientPrice1)
        assert ingredient.get_price() == 200


    def test_get_name(self):
        ingredient = Ingredient(Data.IngredientType1, Data.IngredientName1, Data.IngredientPrice1)
        assert ingredient.get_name() == 'sous'


    def test_get_type(self):
        ingredient = Ingredient(Data.IngredientType1, Data.IngredientName1, Data.IngredientPrice1)
        assert ingredient.get_type() == 'SAUCE'