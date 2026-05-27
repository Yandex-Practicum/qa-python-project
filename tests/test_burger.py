import pytest
import data as D
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = D.BURGER_BUN_PRICE
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = D.INGREDIENT_FILLING_1_PRICE
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_get_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = D.BURGER_BUN_PRICE
        mock_ingr1 = Mock()
        mock_ingr2 = Mock()
        mock_ingr1.get_price.return_value = D.INGREDIENT_FILLING_1_PRICE
        mock_ingr2.get_price.return_value = D.INGREDIENT_FILLING_2_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingr1)
        burger.add_ingredient(mock_ingr2)
        assert burger.get_price() == D.BURGER_EXPECTED_TOTAL

    def test_remove_ingredient(self, burger):
        mock_ingr1 = Mock()
        mock_ingr2 = Mock()
        mock_ingr1.get_price.return_value = D.INGREDIENT_FILLING_1_PRICE
        mock_ingr2.get_price.return_value = D.INGREDIENT_FILLING_2_PRICE
        burger.add_ingredient(mock_ingr1)
        burger.add_ingredient(mock_ingr2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert mock_ingr1 not in burger.ingredients

    def test_move_ingredient(self, burger):
        mock_first = Mock()
        mock_second = Mock()
        burger.add_ingredient(mock_first)
        burger.add_ingredient(mock_second)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_second, mock_first]

    def test_get_receipt(self, burger):
        mock_bun = Mock()
        mock_ingr = Mock()
        mock_bun.get_name.return_value = D.BURGER_BUN_NAME
        mock_bun.get_price.return_value = D.BURGER_BUN_PRICE
        burger.set_buns(mock_bun)
        mock_ingr.get_type.return_value = D.INGREDIENT_TYPE_FILLING
        mock_ingr.get_name.return_value = D.INGREDIENT_FILLING_NAME
        mock_ingr.get_price.return_value = D.INGREDIENT_FILLING_1_PRICE
        burger.add_ingredient(mock_ingr)
        assert burger.get_receipt() == D.EXPECTED_RECEIPT
