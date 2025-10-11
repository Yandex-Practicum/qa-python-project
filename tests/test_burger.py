from unittest.mock import Mock, patch

import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_default_bun_and_ingredients(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_bun(self):
        burger = Burger()
        bun = Bun(data.bun_name, data.bun_price)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[-1] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.ingredients = [ingredient]
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        my_ingredient = Mock()
        burger.ingredients = [Mock(), Mock(), my_ingredient]
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] is my_ingredient

    def test_get_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100

        ingredient = Mock()
        ingredient.get_price.return_value = 200

        burger.bun = bun
        burger.ingredients = [ingredient]

        assert burger.get_price() == 400

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, mock_get_price):
        burger = Burger()

        mock_get_price.return_value = 500

        bun = Mock()
        bun.get_name.return_value = 'white'
        burger.bun = bun

        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient.get_name.return_value = 'cutlet'
        burger.ingredients = [ingredient]

        assert burger.get_receipt() == '(==== white ====)\n= filling cutlet =\n(==== white ====)\n\nPrice: 500'
