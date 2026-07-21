from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun

from data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:


    def test_set_buns(self):

        burger = Burger()

        bun = Bun(
            Data.BLACK_BUN,
            Data.BLACK_BUN_PRICE
        )

        burger.set_buns(bun)

        assert burger.bun == bun


    def test_add_ingredient(self):

        burger = Burger()

        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient


    def test_remove_ingredient(self):

        burger = Burger()

        ingredient = Mock()

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0


    def test_move_ingredient(self):

        burger = Burger()

        first = Mock()
        second = Mock()

        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second
        assert burger.ingredients[1] == first


    def test_get_price(self):

        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = 100

        ingredient = Mock()
        ingredient.get_price.return_value = 50

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 250


    def test_get_receipt(self):

        burger = Burger()

        bun = Bun(
            Data.RED_BUN,
            Data.RED_BUN_PRICE
        )

        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient.get_name.return_value = Data.CUTLET
        ingredient.get_price.return_value = Data.CUTLET_PRICE

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected_result = (
            "(==== red bun ====)\n"
            "= filling cutlet =\n"
            "(==== red bun ====)\n\n"
            "Price: 700"
        )

        assert burger.get_receipt() == expected_result