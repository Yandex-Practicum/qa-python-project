import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from input_data import Data


class TestIngredient:

    def test_get_price_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_DINOSAUR_NAME, Data.INGREDIENT_DINOSAUR_PRICE)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == Data.INGREDIENT_DINOSAUR_NAME
        assert ingredient.price == Data.INGREDIENT_DINOSAUR_PRICE

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_HOT_SAUCE_NAME, Data.INGREDIENT_HOT_SAUCE_PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_SOUR_CREAM_NAME,Data.INGREDIENT_SOUR_CREAM__PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_CILI_SAUCE_NAME, Data.INGREDIENT_CILI_SAUCE_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_CUTLET_NAME, Data.INGREDIENT_CUTLET_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_DINOSAUR_NAME, Data.INGREDIENT_DINOSAUR_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_SAUSAGE_NAME, Data.INGREDIENT_SAUSAGE_PRICE)])
    def test_get_price_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_HOT_SAUCE_NAME, Data.INGREDIENT_HOT_SAUCE_PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_SOUR_CREAM_NAME,Data.INGREDIENT_SOUR_CREAM__PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_CILI_SAUCE_NAME, Data.INGREDIENT_CILI_SAUCE_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_CUTLET_NAME, Data.INGREDIENT_CUTLET_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_DINOSAUR_NAME, Data.INGREDIENT_DINOSAUR_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_SAUSAGE_NAME, Data.INGREDIENT_SAUSAGE_PRICE)])
    def test_get_name_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                            [(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_HOT_SAUCE_NAME, Data.INGREDIENT_HOT_SAUCE_PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_SOUR_CREAM_NAME,Data.INGREDIENT_SOUR_CREAM__PRICE),
                            (INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_CILI_SAUCE_NAME, Data.INGREDIENT_CILI_SAUCE_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_CUTLET_NAME, Data.INGREDIENT_CUTLET_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_DINOSAUR_NAME, Data.INGREDIENT_DINOSAUR_PRICE),
                            (INGREDIENT_TYPE_FILLING, Data.INGREDIENT_SAUSAGE_NAME, Data.INGREDIENT_SAUSAGE_PRICE)])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

