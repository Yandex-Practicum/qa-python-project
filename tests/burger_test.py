from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 200.0
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling


class TestBurgerInit:
    def test_bun_is_none_by_default(self, burger):
        assert burger.bun is None

    def test_ingredients_is_empty_list_by_default(self, burger):
        assert burger.ingredients == []


class TestSetBuns:
    def test_set_buns_stores_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


class TestAddIngredient:
    def test_add_ingredient_appends(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]

    def test_add_multiple_ingredients(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.ingredients == [mock_sauce, mock_filling]


class TestRemoveIngredient:
    def test_remove_first(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    def test_remove_last(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert burger.ingredients == []


class TestMoveIngredient:
    def test_move_forward(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    def test_move_backward(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_filling, mock_sauce]


class TestGetPrice:
    def test_price_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    @pytest.mark.parametrize(
        "bun_price, sauce_price, filling_price, expected",
        [
            (100.0, 100.0, 200.0, 500.0),
            (50.0, 0.0, 0.0, 100.0),
            (0.0, 150.0, 250.0, 400.0),
        ],
    )
    def test_price_with_combinations(
        self, burger, bun_price, sauce_price, filling_price, expected
    ):
        bun = Mock()
        bun.get_price.return_value = bun_price
        sauce = Mock()
        sauce.get_price.return_value = sauce_price
        filling = Mock()
        filling.get_price.return_value = filling_price

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        assert burger.get_price() == expected


class TestGetReceipt:
    def test_receipt_without_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        assert receipt == expected

    def test_receipt_with_sauce(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert "= sauce hot sauce =" in burger.get_receipt()

    def test_receipt_with_filling(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        assert "= filling cutlet =" in burger.get_receipt()

    def test_receipt_full(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 500.0"
        )
        assert burger.get_receipt() == expected