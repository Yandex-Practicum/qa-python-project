import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

from test_data import (
    BUN_PRICE, BUN_NAME,
    SAUCE_NAME
)


class TestBurgerSetBuns:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


class TestBurgerAddIngredient:

    def test_add_ingredient(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert mock_sauce in burger_with_bun.ingredients

    def test_add_multiple_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        assert len(burger_with_bun.ingredients) == 2


class TestBurgerRemoveIngredient:

    def test_remove_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        burger_with_bun.remove_ingredient(0)
        assert mock_sauce not in burger_with_bun.ingredients

    def test_remove_ingredient_reduces_count(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.remove_ingredient(0)
        assert len(burger_with_bun.ingredients) == 0


class TestBurgerMoveIngredient:

    def test_move_ingredient(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        burger_with_bun.move_ingredient(1, 0)
        assert burger_with_bun.ingredients[0] == mock_filling
        assert burger_with_bun.ingredients[1] == mock_sauce


class TestBurgerGetPrice:

    def test_get_price_bun_only(self, burger_with_bun):
        expected = BUN_PRICE * 2
        assert burger_with_bun.get_price() == expected

    def test_get_price_with_ingredients(self, burger_with_bun, mock_sauce, mock_filling):
        burger_with_bun.add_ingredient(mock_sauce)
        burger_with_bun.add_ingredient(mock_filling)
        expected = BUN_PRICE * 2 + mock_sauce.get_price() + mock_filling.get_price()
        assert burger_with_bun.get_price() == expected

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),
        (100, [50], 250),
        (200, [100, 150], 650),
    ])
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected):
        bun = MagicMock(spec=Bun)
        bun.get_price.return_value = bun_price
        bun.get_name.return_value = 'bun'

        burger = Burger()
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = MagicMock(spec=Ingredient)
            ingredient.get_price.return_value = price
            ingredient.get_name.return_value = 'ing'
            ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected


class TestBurgerGetReceipt:

    def test_get_receipt_contains_bun_name(self, burger_with_bun):
        assert BUN_NAME in burger_with_bun.get_receipt()

    def test_get_receipt_contains_price(self, burger_with_bun):
        expected_price = BUN_PRICE * 2
        assert f'Price: {expected_price}' in burger_with_bun.get_receipt()

    def test_get_receipt_contains_ingredient_name(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert SAUCE_NAME in burger_with_bun.get_receipt()

    def test_get_receipt_contains_ingredient_type(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert mock_sauce.get_type().lower() in burger_with_bun.get_receipt()

    def test_get_receipt_format(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        receipt = burger_with_bun.get_receipt()

        lines = receipt.split('\n')

        assert lines[0] == f'(==== {BUN_NAME} ====)'
        assert f'(==== {BUN_NAME} ====)' in lines