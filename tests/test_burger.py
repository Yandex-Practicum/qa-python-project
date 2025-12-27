from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest
from unittest.mock import Mock


class TestBurger:

    def test_set_buns_true(self):
        burger = Burger()
        bun = Bun('test bun', 100)
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_add_ingredient_true(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = 'test sause'
        mock_ingredient.price = 20
        mock_ingredient.type = 'SAUSE'
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]


    def test_remove_ingredient_true(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_true(self):
        burger = Burger()
        mock_sauce = Mock()
        mock_filling = Mock()
        burger.ingredients = [mock_sauce, mock_filling]
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_filling, mock_sauce]\

    def test_get_price_true(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        assert burger.get_price() == 400.0

    def test_get_receipt_true(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n" \
                           "= sauce hot sauce =\n" \
                           "= filling cutlet =\n" \
                           "(==== black bun ====)\n\n" \
                           "Price: 400"
        assert expected_receipt == burger.get_receipt()










