import pytest
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE,
                                        INGREDIENT_TYPE_FILLING)
from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:

    # Проверка конструктора класса
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
    ])
    def test_init(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    # Проверка метода get_price()
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
    ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Проверка метода get_name()
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
    ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Проверка метода get_type()
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
        (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
        (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type