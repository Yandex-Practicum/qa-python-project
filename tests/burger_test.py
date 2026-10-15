from unittest.mock import Mock

from tests.test_data import EXPECTED_BURGER_PRICE, EXPECTED_RECEIPT
from burger import Burger


class TestBurger:
    def test_set_buns_sets_bun(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_removes_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_moves_ingredient(self, burger):
        first = Mock()
        second = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second, first]

    def test_get_price_returns_total_price(self, burger, bun, mock_ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == EXPECTED_BURGER_PRICE

    def test_get_receipt_returns_receipt(self, burger, bun, mock_ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == EXPECTED_RECEIPT
