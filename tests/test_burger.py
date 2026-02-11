from praktikum.burger import Burger
from test_data import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestBurger:

    def test_set_buns(self, burger: Burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_single_ingredient(self, burger: Burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]

    def test_remove_sauce_ingredient(self, burger: Burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_single_ingredient_no_change(self, burger: Burger, mock_sauce):
        burger.add_ingredient(mock_sauce)

        burger.move_ingredient(0, 0)
        assert burger.ingredients == [mock_sauce]

    @pytest.mark.parametrize(
    "start_index, new_index, expected_order",
    [
        (0, 2, ["FILLING", "SAUCE", "SAUCE"]),
        (2, 0, ["SAUCE", "SAUCE", "FILLING"]),
        (1, 1, ["SAUCE", "FILLING", "SAUCE"]),
    ]
)
    def test_move_ingredient_various_positions(
        self,
        burger: Burger,
        mock_ingredient_factory,
        start_index,
        new_index,
        expected_order
    ):
        ing1 = mock_ingredient_factory(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE)
        ing2 = mock_ingredient_factory(INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
        ing3 = mock_ingredient_factory(INGREDIENT_TYPE_SAUCE, SAUCE_NAME_2, SAUCE_PRICE_2)

        for ing in [ing1, ing2, ing3]:
            burger.add_ingredient(ing)

        burger.move_ingredient(start_index, new_index)

        remaining_types = [i.get_type() for i in burger.ingredients]
        assert remaining_types == expected_order

    def test_get_price_single_ingredient(self, burger: Burger, mock_bun, mock_sauce):

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price()

        assert burger.get_price() == expected_price   

    def test_burger_get_price_multiple_ingredients(self, burger: Burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_price = mock_bun.get_price() * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_single_ingredient1(self, burger: Burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        receipt = burger.get_receipt()

        expected_lines = [
            f"(==== {MOCK_BUN_NAME} ====)",
            f"= sauce {SAUCE_NAME} =",
            f"(==== {MOCK_BUN_NAME} ====)",
            "",
            f"Price: {burger.get_price()}"
        ]

        assert receipt.split("\n") == expected_lines
