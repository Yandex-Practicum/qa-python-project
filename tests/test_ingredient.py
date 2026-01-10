from data import BurgerSample
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_sauce_success(self):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerSample.SAUCE_NAME, BurgerSample.SAUCE_PRICE)
        assert ingredient_sauce.get_price() == BurgerSample.SAUCE_PRICE

    def test_get_name_sauce_success(self):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerSample.SAUCE_NAME, BurgerSample.SAUCE_PRICE)
        assert ingredient_sauce.get_name() == BurgerSample.SAUCE_NAME

    def test_get_type_sauce_success(self):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, BurgerSample.SAUCE_NAME, BurgerSample.SAUCE_PRICE)
        assert ingredient_sauce.get_type() == 'SAUCE'

    def test_get_price_filling_success(self):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, BurgerSample.FILLING_NAME, BurgerSample.FILLING_PRICE)
        assert ingredient_filling.get_price() == BurgerSample.FILLING_PRICE

    def test_get_name_filling_success(self):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, BurgerSample.FILLING_NAME, BurgerSample.FILLING_PRICE)
        assert ingredient_filling.get_name() == BurgerSample.FILLING_NAME

    def test_get_type_filling_success(self):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, BurgerSample.FILLING_NAME, BurgerSample.FILLING_PRICE)
        assert ingredient_filling.get_type() == 'FILLING'
