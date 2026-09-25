from unittest.mock import Mock

from praktikum.burger import Burger
from tests.constants import (
    RECEIPT_EMPTY_BLACK_BUN,
    RECEIPT_BLACK_BUN_WITH_SAUCE,
    RECEIPT_LINE_BLACK_BUN,
    RECEIPT_LINE_SAUCE_HOT,
    RECEIPT_LINE_FILLING_CUTLET,
)


class TestBurgerInit:
    def test_burger_init_bun_is_none(self, burger):
        assert burger.bun is None

    def test_burger_init_ingredients_empty(self, burger):
        assert burger.ingredients == []


class TestSetBuns:
    def test_set_buns_stores_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_set_buns_overwrites_previous(self, burger):
        first, second = Mock(), Mock()
        burger.set_buns(first)
        burger.set_buns(second)
        assert burger.bun is second


class TestAddIngredient:
    def test_add_ingredient_appends(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_add_multiple_ingredients_keeps_order(self, burger):
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        assert burger.ingredients == [ing1, ing2, ing3]


class TestRemoveIngredient:
    def test_remove_ingredient_removes_item(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_ingredient_keeps_others_in_order(self, burger):
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.remove_ingredient(1)

        assert burger.ingredients == [ing1, ing3]

    def test_remove_ingredient_out_of_range_raises_and_keeps_state(self, burger):
        raised = False
        try:
            burger.remove_ingredient(0)
        except IndexError:
            raised = True

        assert raised is True
        assert burger.ingredients == []


class TestMoveIngredient:
    def test_move_ingredient_forward(self, burger):
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    def test_move_ingredient_backward(self, burger):
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients == [ing3, ing1, ing2]

    def test_move_ingredient_same_index_keeps_order(self, burger):
        ing1, ing2 = Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 0)

        assert burger.ingredients == [ing1, ing2]


class TestGetPrice:
    def test_get_price_only_bun_counts_bun_twice(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_price_with_one_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250.0

    def test_get_price_with_multiple_ingredients(
        self, burger, mock_bun, make_mock_ingredient
    ):
        ing1 = make_mock_ingredient(price=50.0)
        ing2 = make_mock_ingredient(price=75.0)
        ing3 = make_mock_ingredient(price=25.0)

        burger.set_buns(mock_bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        assert burger.get_price() == 350.0

    def test_get_price_without_bun_raises(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        raised = False
        try:
            burger.get_price()
        except AttributeError:
            raised = True

        assert raised is True
        assert burger.ingredients == [mock_ingredient]


class TestGetReceipt:
    def test_get_receipt_without_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_receipt() == RECEIPT_EMPTY_BLACK_BUN

    def test_get_receipt_with_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_receipt() == RECEIPT_BLACK_BUN_WITH_SAUCE

    def test_get_receipt_uses_lowercase_type(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert RECEIPT_LINE_FILLING_CUTLET in receipt

    def test_get_receipt_ingredient_order(self, burger, mock_bun, mock_ingredient, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_filling)

        lines = burger.get_receipt().split("\n")

        assert lines[0] == RECEIPT_LINE_BLACK_BUN
        assert lines[1] == RECEIPT_LINE_SAUCE_HOT
        assert lines[2] == RECEIPT_LINE_FILLING_CUTLET

    def test_get_receipt_calls_ingredient_methods(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        burger.get_receipt()

        assert mock_ingredient.get_type.called
        assert mock_ingredient.get_name.called