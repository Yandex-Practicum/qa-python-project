from unittest.mock import MagicMock

import pytest

from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_burger_initialization_default_state():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns_sets_bun():
    burger = Burger()
    bun = Bun("black bun", 100)

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_appends_to_list():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_by_index():
    burger = Burger()
    first = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    second = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
    burger.add_ingredient(first)
    burger.add_ingredient(second)

    burger.remove_ingredient(0)

    assert burger.ingredients == [second]


def test_move_ingredient_changes_order():
    burger = Burger()
    first = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    second = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
    third = Ingredient(INGREDIENT_TYPE_FILLING, "onion", 30)

    burger.add_ingredient(first)
    burger.add_ingredient(second)
    burger.add_ingredient(third)

    burger.move_ingredient(0, 2)

    assert [item.get_name() for item in burger.ingredients] == ["ketchup", "onion", "cutlet"]


@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected_total",
    [
        (100, [], 200),
        (125, [50], 300),
        (150, [40, 60], 400),
    ],
)
def test_get_price_calculates_total(bun_price, ingredient_prices, expected_total):
    burger = Burger()
    bun = MagicMock()
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)

    for price in ingredient_prices:
        ingredient = MagicMock()
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)

    total = burger.get_price()

    assert total == expected_total


def test_get_receipt_returns_expected_multiline_string():
    burger = Burger()

    bun = MagicMock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    burger.set_buns(bun)

    ingredient = MagicMock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "ketchup"
    ingredient.get_price.return_value = 50
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert receipt == "(==== black bun ====)\n= sauce ketchup =\n(==== black bun ====)\n\nPrice: 250"
