import pytest
from data import order_data
from unittest.mock import patch
from burger import Burger


class TestBurger:

    def test_set_buns_add_bun_at_order(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_add_ingriedient_at_order(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient_remove_ingredient_from_order(self, burger, mock_sauce, mock_filling):        
        burger.ingredients = [mock_sauce, mock_filling]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients == [mock_filling]

    def test_move_ingredient_swaps_positions_of_ingredients(self, burger, mock_sauce, mock_filling):
        burger.ingredients = [mock_sauce, mock_filling]
        burger.move_ingredient(1, 0)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_get_price_get_price_of_order(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.bun = mock_bun
        burger.ingredients = [mock_sauce, mock_filling]
        actual_price = burger.get_price()
        expected_price = 800
        assert actual_price == expected_price
        mock_bun.get_price.assert_called_once()
        mock_sauce.get_price.assert_called_once()
        mock_filling.get_price.assert_called_once()

    @patch.object(Burger, 'get_price', return_value=800)
    def test_get_receipt_get_check_of_order(self, mock_get_price, burger, mock_bun, mock_sauce, mock_filling):
        burger.bun = mock_bun
        burger.ingredients = [mock_sauce, mock_filling]
        actual_receipt = burger.get_receipt()
        assert actual_receipt == order_data.expected_check
        mock_bun.get_name.assert_called()
        mock_sauce.get_name.assert_called_once()
        mock_sauce.get_type.assert_called_once()
        mock_filling.get_name.assert_called_once()
        mock_filling.get_type.assert_called_once()
        mock_get_price.assert_called_once()
