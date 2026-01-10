import unittest
from unittest.mock import Mock
import pytest
from data import Burger1
from praktikum.bun import Bun
from praktikum.burger import Burger


class TestBurger(unittest.TestCase):

    def test_init(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_bun(self):
        burger = Burger()
        bun = Bun(Burger1().bun_name, Burger1().bun_price)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('new_ingredients', [Burger1().sauce_name, Burger1().filling_name])
    def test_add_ingredient(new_ingredients):
        burger = Burger()
        burger.add_ingredient(new_ingredients)
        assert burger.ingredients == [new_ingredients] and len(burger.ingredients) == 1

    @pytest.mark.parametrize('removed_ingredients', [Burger1().sauce_name, Burger1().filling_name])
    def test_remove_ingredient(removed_ingredients):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = Burger1.sauce_name
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(removed_ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredients not in burger.ingredients and mock_ingredient in burger.ingredients


    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Burger1().filling_name)
        burger.add_ingredient(Burger1().sauce_name)
        old_index = 0
        new_index = 1
        burger.move_ingredient(old_index, new_index)
        assert burger.ingredients[0] == Burger1().sauce_name and burger.ingredients[1] == Burger1().filling_name

    def test_get_price(self):
        mock_bun = Mock()
        bun_price = 100.0
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        ingredient_price = 300.0
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = bun_price*2 + ingredient_price
        actual_price = burger.get_price()
        assert actual_price == expected_price and type(actual_price) == float

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = Burger1().bun_name
        mock_bun.get_price.return_value = Burger1().bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = Burger1().filling_type
        mock_ingredient.get_name.return_value = Burger1().filling_name
        mock_ingredient.get_price.return_value = Burger1().filling_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_receipt = ('(==== Краторная булка N-200i ====)\n'
                            '= filling Биокотлета из марсианской Магнолии =\n'
                            '(==== Краторная булка N-200i ====)\n'
                            '\n'
                            f'Price: {burger.get_price()}')
        actual_receipt = burger.get_receipt()
        assert expected_receipt == actual_receipt and type(actual_receipt) == str









