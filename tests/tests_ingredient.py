from data import DataIngredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


# class for tests Ingredient methods
class TestsIngredient:

    def test_get_price(self, new_ingredient):
        assert new_ingredient.get_price() == DataIngredient.INGREDIENT_PRICE

    def test_get_name(self,new_ingredient):
        assert new_ingredient.get_name() == DataIngredient.INGREDIENT_NAME

    def test_get_type(self,new_ingredient):
        assert new_ingredient.get_type() == INGREDIENT_TYPE_FILLING
