
from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


def test_burger_initialization():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns():
    burger = Burger()
    mock_bun = Mock()

    burger.set_buns(mock_bun)

    assert burger.bun is mock_bun


def test_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock()

    burger.add_ingredient(mock_ingredient)

    assert burger.ingredients == [mock_ingredient]


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, [1, 2]),
        (1, [0, 2]),
        (2, [0, 1]),
    ]
)
def test_remove_ingredient(index, expected):
    burger = Burger()
    burger.ingredients = [0, 1, 2]

    burger.remove_ingredient(index)

    assert burger.ingredients == expected


@pytest.mark.parametrize(
    "index, new_index, expected",
    [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 2, [0, 2, 1]),
        (1, 0, [1, 0, 2]),
        (1, 1, [0, 1, 2]),
    ]
)
def test_move_ingredient(index, new_index, expected):
    burger = Burger()
    burger.ingredients = [0, 1, 2]

    burger.move_ingredient(index, new_index)

    assert burger.ingredients == expected


@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected_price",
    [
        (100, [], 200),
        (100, [30], 230),
        (100, [30, 70], 300),
        (50, [20, 40, 60], 220),
    ]
)
def test_get_price(bun_price, ingredient_prices, expected_price):
    burger = Burger()

    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == expected_price


@pytest.mark.parametrize(
    "ingredients, expected_lines",
    [
        ([], []),
        (
            [("SAUCE", "Сырный соус", 30)],
            ["= sauce Сырный соус ="]
        ),
        (
            [
                ("SAUCE", "Сырный соус", 30),
                ("FILLING", "Котлета", 70)
            ],
            [
                "= sauce Сырный соус =",
                "= filling Котлета ="
            ]
        ),
    ]
)
def test_get_receipt(ingredients, expected_lines):
    burger = Burger()

    mock_bun = Mock()
    mock_bun.get_name.return_value = "Космическая булочка"
    mock_bun.get_price.return_value = 100
    burger.set_buns(mock_bun)

    for ingredient_type, name, price in ingredients:
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)

    expected_receipt = "\n".join(
        [
            "(==== Космическая булочка ====)",
            *expected_lines,
            "(==== Космическая булочка ====)\n",
            f"Price: {200 + sum(item[2] for item in ingredients)}"
        ]
    )

    assert burger.get_receipt() == expected_receipt
