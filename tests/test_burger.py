from unittest.mock import Mock
import pytest

from data import BurgerData


class TestBurger:

    def test_init_bun_is_none(self, burger):
        assert burger.bun is None

    def test_init_ingredients_is_empty_list(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_bun_to_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_list(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)

        assert burger.ingredients == [mock_sauce]

    def test_remove_ingredient_deletes_ingredient_from_list(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_filling]

    def test_move_ingredient_changes_ingredients_order(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_filling, mock_sauce]

    @pytest.mark.parametrize(
        'bun_price, ingredient_prices, expected_price',
        BurgerData.PRICE_TEST_DATA
    )
    def test_get_price_returns_correct_total_price(self, burger, bun_price, ingredient_prices, expected_price):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_receipt(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_receipt = (
            f'(==== {BurgerData.BUN_NAME} ====)\n'
            f'= sauce {BurgerData.SAUCE_NAME} =\n'
            f'= filling {BurgerData.FILLING_NAME} =\n'
            f'(==== {BurgerData.BUN_NAME} ====)\n'
            '\n'
            'Price: 5066'
        )

        assert burger.get_receipt() == expected_receipt
