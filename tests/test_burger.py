from unittest.mock import Mock

from burger import Burger


class TestBurger:

    def test_constructor_creates_empty_burger(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []


    def test_set_buns_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun


    def test_add_ingredient_adds_ingredient_to_list(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]


    def test_remove_ingredient_removes_ingredient_by_index(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []


    def test_move_ingredient_changes_ingredient_position(self, burger, mock_ingredient):
        second_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second_ingredient, mock_ingredient]


    def test_get_price_returns_correct_burger_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250


    def test_get_receipt_returns_correct_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert "big bun" in receipt
        assert "sauce chilli sauce" in receipt
        assert "250" in receipt
