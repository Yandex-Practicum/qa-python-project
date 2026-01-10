from conftest import mock_bun
from praktikum.burger import Burger
from data import ExpectedResults

class TestBurger:

    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        assert mock_ingredient_1 in burger.ingredients

    def test_burger_remove_ingredient(self, mock_ingredient_1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_move_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_1

    def test_burger_get_price(self, mock_bun, mock_ingredient_1):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)

        price = burger.get_price()
        expected_price = (mock_bun.get_price() * 2) + mock_ingredient_1.get_price()

        assert price == expected_price

    def test_burger_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        expected_result = ExpectedResults.RECEIPT_TEXT

        assert burger.get_receipt() == expected_result
