import pytest
from unittest.mock import Mock

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from burger import Burger


class TestBurger:

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [], 200),
        (100, [50], 250),
        (100, [50, 25], 275),
        (0, [10, 20], 30),
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price


    @pytest.mark.parametrize("index, new_index, expected_order", [
        (0, 2, [2, 3, 1]),
        (2, 0, [3, 1, 2]),
        (1, 1, [1, 2, 3]),
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        burger = Burger()

        ingredients = []
        for i in [1, 2, 3]:
            ingredient = Mock()
            ingredient.get_name.return_value = str(i)
            ingredients.append(ingredient)
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        result_order = [int(i.get_name()) for i in burger.ingredients]

        assert result_order == expected_order


    @pytest.mark.parametrize("ingredient_type, expected_type", [
        ("SAUCE", "sauce"),
        ("FILLING", "filling"),
    ])
    def test_get_receipt_contains_correct_ingredient_type(self, ingredient_type, expected_type):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = "ketchup"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert f"= {expected_type} ketchup =" in receipt


    def test_get_receipt_contains_bun(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt


    def test_get_receipt_contains_correct_price(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "ketchup"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert "Price: 250" in receipt