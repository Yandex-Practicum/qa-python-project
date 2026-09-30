import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_initial_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_burger_initial_ingredients_empty(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_increases_list_length(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_stores_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_decreases_list_length(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_correct_item(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ing_2

    @pytest.mark.parametrize(
        "start_idx, end_idx, expected_order",
        [
            (0, 2, ["ing_2", "ing_3", "ing_1"]),
            (2, 0, ["ing_3", "ing_1", "ing_2"]),
            (0, 1, ["ing_2", "ing_1", "ing_3"]),
            (1, 0, ["ing_2", "ing_1", "ing_3"]),
        ],
    )
    def test_move_ingredient(self, start_idx, end_idx, expected_order):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_1.name = "ing_1"
        mock_ing_2 = Mock()
        mock_ing_2.name = "ing_2"
        mock_ing_3 = Mock()
        mock_ing_3.name = "ing_3"

        for ingredient in [mock_ing_1, mock_ing_2, mock_ing_3]:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(start_idx, end_idx)

        actual_order = [ingredient.name for ingredient in burger.ingredients]
        assert actual_order == expected_order

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_total",
        [
            (100.0, [50.0, 30.0], 280.0),
            (0.0, [15.0], 15.0),
            (50.5, [], 101.0),
        ],
    )
    def test_get_price(self, bun_price, ing_prices, expected_total):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ing_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_sauce = Mock()
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "chili"
        mock_sauce.get_price.return_value = 50.0
        burger.add_ingredient(mock_sauce)

        mock_filling = Mock()
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 100.0
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce chili =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 350.0"
        )

        assert receipt == expected_receipt