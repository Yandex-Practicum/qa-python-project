import pytest
from unittest.mock import Mock

from praktikum.ingredient import Ingredient


def test_burger_init(burger):
    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun


def test_add_ingredient(burger, mock_ingredient_sauce):
    burger.add_ingredient(mock_ingredient_sauce)

    assert burger.ingredients == [mock_ingredient_sauce]


@pytest.mark.parametrize(
    "remove_index, expected_ingredients",
    [
        (0, ["ingredient_1", "ingredient_2"]),
        (1, ["ingredient_0", "ingredient_2"]),
        (2, ["ingredient_0", "ingredient_1"]),
    ],
)
def test_remove_ingredient(
    burger,
    multiple_ingredients,
    remove_index,
    expected_ingredients,
):
    for ingredient in multiple_ingredients:
        burger.add_ingredient(ingredient)

    burger.remove_ingredient(remove_index)

    actual_names = [
        ingredient.get_name()
        for ingredient in burger.ingredients
    ]

    assert actual_names == expected_ingredients


@pytest.mark.parametrize(
    "index, new_index, expected_order",
    [
        (0, 1, ["ingredient_1", "ingredient_0", "ingredient_2"]),
        (1, 0, ["ingredient_1", "ingredient_0", "ingredient_2"]),
        (0, 2, ["ingredient_1", "ingredient_2", "ingredient_0"]),
        (2, 0, ["ingredient_2", "ingredient_0", "ingredient_1"]),
    ],
)
def test_move_ingredient(
    burger,
    multiple_ingredients,
    index,
    new_index,
    expected_order,
):
    for ingredient in multiple_ingredients:
        burger.add_ingredient(ingredient)

    burger.move_ingredient(index, new_index)

    actual_names = [
        ingredient.get_name()
        for ingredient in burger.ingredients
    ]

    assert actual_names == expected_order


@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected_price",
    [
        (100.0, [], 200.0),
        (100.0, [50.0], 250.0),
        (100.0, [50.0, 80.0], 330.0),
        (150.0, [50.0, 80.0, 30.0], 460.0),
    ],
)
def test_get_price(
    burger,
    mock_bun,
    bun_price,
    ingredient_prices,
    expected_price,
):
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_price

    mock_bun.get_price.assert_called_once()


def test_get_receipt(
    burger,
    mock_bun,
    mock_ingredient_sauce,
    mock_ingredient_filling,
):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    receipt = burger.get_receipt()

    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce karri_sauce =\n"
        "= filling meat =\n"
        "(==== black bun ====)\n\n"
        "Price: 330.0"
    )

    assert receipt == expected_receipt

    mock_bun.get_name.assert_called()
    mock_bun.get_price.assert_called()