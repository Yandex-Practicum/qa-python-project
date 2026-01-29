from unittest.mock import Mock

import pytest

from praktikum_app.data import Data
from praktikum_app.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from src.bun import Bun
from src.burger import Burger
from src.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_to_the_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_from_the_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_in_the_list(self):
        burger = Burger()
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.FILLING_NAME, Data.FILLING_PRICE)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second_ingredient

    def test_get_burger_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        mock_first_ingredient = Mock()
        mock_first_ingredient.get_price.return_value = 60
        mock_second_ingredient = Mock()
        mock_second_ingredient.get_price.return_value = 40
        burger.add_ingredient(mock_first_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        assert burger.get_price() == 200

    @pytest.mark.parametrize(
        'bun_name, bun_price, sauce_type, sauce_name, sauce_price, filling_type, filling_name, filling_price', Data.DATA
    )
    def test_get_burger_receipt(self, bun_name, bun_price, sauce_type, sauce_name, sauce_price, filling_type,
                                filling_name, filling_price):
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        sauce = Ingredient(sauce_type, sauce_name, sauce_price)
        filling = Ingredient(filling_type, filling_name, filling_price)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        expected_price = bun_price * 2 + sauce_price + filling_price

        price = int(burger.get_receipt()[-3] + burger.get_receipt()[-2] + burger.get_receipt()[-1])

        assert bun_name in burger.get_receipt()
        assert sauce_type.lower() in burger.get_receipt()
        assert sauce_name in burger.get_receipt()
        assert filling_type.lower() in burger.get_receipt()
        assert filling_name in burger.get_receipt()

        assert price == expected_price
