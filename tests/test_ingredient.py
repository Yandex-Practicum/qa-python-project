from praktikum_package.ingredient import Ingredient
from data import Data


class TestIngredient:
    def test_ingredient_get_price_success(self):
        new_ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert new_ingredient.get_price() == Data.INGREDIENT_PRICE

    def test_ingredient_get_name_success(self):
        new_ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert new_ingredient.get_name() == Data.INGREDIENT_NAME

    def test_ingredient_get_type_success(self):
        new_ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        assert new_ingredient.get_type() == Data.INGREDIENT_TYPE
