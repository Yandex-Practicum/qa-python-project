import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:

    def test_initial_state(self, burger):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []
    

    def test_burger_with_bun_and_ingredient_state(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        bun = mock_bun('black bun', 100.0)
        ingredient = mock_ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100.0)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.bun == bun
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient(self, burger, mock_ingredient):
        ingredient = mock_ingredient("TOPPING", "Pepperoni", 50.0)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize("index", [0, -1])
    def test_remove_ingredient(self, burger, mock_ingredient, index):
        ingredient = mock_ingredient("SAUCE", "Barbecue", 30.0)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize(
        "start_index, new_index",
        [(0, 1), (1, 0), (0, 0)]
    )
    def test_move_ingredient(self, burger, mock_ingredient, start_index, new_index):
        ingredient1 = mock_ingredient("TOPPING", "Pepperoni", 50.0)
        ingredient2 = mock_ingredient("SAUCE", "Barbecue", 30.0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        original_names = [ingredient1.get_name(), ingredient2.get_name()]

        burger.move_ingredient(start_index, new_index)

        current_names = [ing.get_name() for ing in burger.ingredients]


        expected_names = original_names.copy()
        expected_names.insert(new_index, expected_names.pop(start_index))

        assert current_names == expected_names

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100.0, [], 200.0),
            (150.0, [50.0], 350.0),
            (100.0, [50.0, 30.0], 280.0),
        ]
    )
    def test_get_price(self, burger, mock_bun, mock_ingredient, bun_price, ingredient_prices, expected_price):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for i, price in enumerate(ingredient_prices):
            ingredient = mock_ingredient(f"TYPE_{i}", f"Ingredient_{i}", price)
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        ingredient = mock_ingredient("TOPPING", "Pepperoni", 50.0)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        expected_lines = [
            '(==== Black Bun ====)',
            '= topping Pepperoni =',
            '(==== Black Bun ====)\n',
            f'Price: {200.0 + 50.0}'
        ]
        expected_receipt = '\n'.join(expected_lines)

        assert receipt == expected_receipt

    def test_get_receipt_no_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected_lines = [
            '(==== Black Bun ====)',
            '(==== Black Bun ====)\n',
            'Price: 200.0'
        ]
        expected_receipt = '\n'.join(expected_lines)
        assert receipt == expected_receipt