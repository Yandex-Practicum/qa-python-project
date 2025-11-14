from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestBurger:

    @pytest.mark.parametrize('name, price', [
        ["black bun", 100],
        ["white bun", 200],
        ["red bun", 300]
                             ])
    def test_set_buns(self, name, price):
        mock_bun = Mock()
        mock_bun.bun = Bun(name, price)
        burger = Burger()
        burger.set_buns(mock_bun.bun)

        assert burger.bun == mock_bun.bun

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 88.25],
        [INGREDIENT_TYPE_FILLING, "dinosaur", -100.78]
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient( ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)

        assert burger.ingredients == [mock_ingredient.ingredients]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 88.25)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        mock_ingredient.ingredient1 = Ingredient('mayonnaise', INGREDIENT_TYPE_SAUCE, 0.5)
        mock_ingredient.ingredient2 = Ingredient('tomato', INGREDIENT_TYPE_FILLING, 0.7)
        mock_ingredient.ingredient3 = Ingredient('lettuce', INGREDIENT_TYPE_FILLING, 0.3)
        burger.add_ingredient(mock_ingredient.ingredient1)
        burger.add_ingredient(mock_ingredient.ingredient2)
        burger.add_ingredient(mock_ingredient.ingredient3)
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock_ingredient.ingredient2, mock_ingredient.ingredient3, mock_ingredient.ingredient1]

    def test_get_price(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        burger = Burger()
        mock_bun.bun = Bun('sesame', 2.0)
        mock_ingredient.ingredient1 = Ingredient('mayonnaise', INGREDIENT_TYPE_SAUCE, 0.5)
        mock_ingredient.ingredient2 = Ingredient('tomato', INGREDIENT_TYPE_FILLING, 0.7)
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredient1)
        burger.add_ingredient(mock_ingredient.ingredient2)

        assert burger.get_price() == 5.2

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.bun = Bun("Булка", 10.1)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient("FILLING", "chili", 1.8)
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)

        receipt = burger.get_receipt()

        expected_receipt = "(==== Булка ====)\n" \
                           "= filling chili =\n" \
                           "(==== Булка ====)\n"\
                           '\n'\
                           "Price: 22.0"
        assert receipt == expected_receipt

