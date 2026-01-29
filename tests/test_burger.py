import pytest
from praktikum.burger import Burger
from conftest import *

class TestBurger:

    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients == [mock_ingredient_filling]

    def test_burger_remove_ingredient(self, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient_sauce]

    def test_burger_move_ingredient(self, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_sauce, mock_ingredient_filling]

    def test_burger_get_price(self, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_price = 27
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_receipt = ('(==== Марсианская Булка ====)\n'
 '= filling Кеплерская Курочка =\n'
 '= sauce Юпитерский Соус =\n'
 '(==== Марсианская Булка ====)\n'
 '\n'
 'Price: 27')

        assert burger.get_receipt() == expected_receipt
