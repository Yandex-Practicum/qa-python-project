import unittest
from praktikum.ingredient import Ingredient
from data import Burger1
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient(unittest.TestCase):
    def test_init_ingredient_type(self):
        ingredient = Ingredient(Burger1().filling_type, Burger1().filling_name, Burger1().filling_price)
        assert ingredient.type == INGREDIENT_TYPE_FILLING and type(ingredient.type) == str

    def test_init_name(self):
        ingredient = Ingredient(Burger1().filling_type, Burger1().filling_name, Burger1().filling_price)
        assert ingredient.name == 'Биокотлета из марсианской Магнолии' and type(ingredient.name) == str

    def test_init_price(self):
        ingredient = Ingredient(Burger1().filling_type, Burger1().filling_name, Burger1().filling_price)
        assert ingredient.price == 424.0 and type(ingredient.price) == float

    def test_get_price(self):
        ingredient = Ingredient(Burger1().sauce_type, Burger1().sauce_name, Burger1().sauce_price)
        ingredient.get_price()
        assert ingredient.get_price() == 80.0 and type(ingredient.get_price()) == float

    def test_get_name(self):
        ingredient = Ingredient(Burger1().sauce_type, Burger1().sauce_name, Burger1().sauce_price)
        ingredient.get_name()
        assert ingredient.get_name() == 'Соус фирменный Space Sauce' and type(ingredient.get_name()) == str

    def test_get_type(self):
        ingredient = Ingredient(Burger1().sauce_type, Burger1().sauce_name, Burger1().sauce_price)
        ingredient.get_type()
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE and type(ingredient.get_type()) == str