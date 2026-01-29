import pytest
from burger import Burger
from data import DataReceipt

class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        assert burger.ingredients == [mock_ingredient1]

    def test_remove_ingredient(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient1

    def test_get_price(self, mock_bun, mock_ingredient1):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        price = burger.get_price()
        expected_price = mock_bun.get_price() * 2 + mock_ingredient1.get_price()
        assert price == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient2)
        assert burger.get_receipt() == DataReceipt.BURGER_RECEIPT
