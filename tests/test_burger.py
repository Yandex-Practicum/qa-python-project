import pytest
from unittest.mock import Mock
from data import (
    BUN_NAME,
    BUN_PRICE,
    SAUCE_TYPE,
    SAUCE_NAME,
    SAUCE_PRICE,
    FILLING_TYPE,
    FILLING_NAME,
    FILLING_PRICE,
    SECOND_SAUCE_NAME,
    SECOND_SAUCE_PRICE,
    MOVED_INGREDIENT_NAMES_FROM_FIRST_TO_LAST,
    MOVED_INGREDIENT_NAMES_FROM_LAST_TO_FIRST,
)

def make_ingredient(ingredient_type, name, price):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient


def test_set_buns_sets_bun(burger, mock_bun):
    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun


def test_add_ingredient_adds_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)

    assert burger.ingredients == [mock_ingredient]


def test_remove_ingredient_removes_ingredient(burger):
    ingredient1 = make_ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
    ingredient2 = make_ingredient(FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
    burger.ingredients = [ingredient1, ingredient2]

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient2]


@pytest.mark.parametrize(
    "index,new_index,expected",
    [
        (0, 2, [FILLING_NAME, SECOND_SAUCE_NAME, SAUCE_NAME]),
        (2, 0, [SECOND_SAUCE_NAME, SAUCE_NAME, FILLING_NAME]),
    ],
)
def test_move_ingredient_changes_order(burger, index, new_index, expected):
    burger.ingredients = [
        make_ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE),
        make_ingredient(FILLING_TYPE, FILLING_NAME, FILLING_PRICE),
        make_ingredient(SAUCE_TYPE, SECOND_SAUCE_NAME, SECOND_SAUCE_PRICE),
    ]

    burger.move_ingredient(index, new_index)

    result = [ingredient.get_name() for ingredient in burger.ingredients]
    assert result == expected


@pytest.mark.parametrize(
    "bun_price,ingredient_prices,expected_price",
    [
        (BUN_PRICE, [SAUCE_PRICE, FILLING_PRICE], 400),
        (FILLING_PRICE, [], 200),
    ],
)
def test_get_price_returns_bun_price_twice_plus_ingredients(
    burger, mock_bun, bun_price, ingredient_prices, expected_price
):
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)
    for price in ingredient_prices:
        burger.add_ingredient(make_ingredient(SAUCE_TYPE, SAUCE_NAME, price))

    assert burger.get_price() == expected_price


def test_get_receipt_returns_burger_description_and_price(burger, mock_bun):
    burger.set_buns(mock_bun)
    burger.add_ingredient(make_ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE))
    burger.add_ingredient(make_ingredient(FILLING_TYPE, FILLING_NAME, FILLING_PRICE))
    expected_receipt = (
        f"(==== {BUN_NAME} ====)\n"
        f"= sauce {SAUCE_NAME} =\n"
        f"= filling {FILLING_NAME} =\n"
        f"(==== {BUN_NAME} ====)\n\n"
        "Price: 400"
    )

    assert burger.get_receipt() == expected_receipt