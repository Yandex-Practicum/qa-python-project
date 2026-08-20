from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    return Mock(spec=Bun)


def test_init_creates_burger_without_bun_and_ingredients(burger):
    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns_sets_selected_bun(burger, bun_mock):
    burger.set_buns(bun_mock)

    assert burger.bun is bun_mock


def test_add_ingredient_appends_ingredient(burger):
    ingredient = Mock(spec=Ingredient)

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


@pytest.mark.parametrize(
    ('index', 'expected_names'),
    [
        (0, ['second', 'third']),
        (1, ['first', 'third']),
        (-1, ['first', 'second']),
    ],
)
def test_remove_ingredient_removes_item_by_index(burger, index, expected_names):
    burger.ingredients = ['first', 'second', 'third']

    burger.remove_ingredient(index)

    assert burger.ingredients == expected_names


@pytest.mark.parametrize(
    ('index', 'new_index', 'expected_order'),
    [
        (0, 2, ['second', 'third', 'first', 'fourth']),
        (3, 0, ['fourth', 'first', 'second', 'third']),
        (1, 3, ['first', 'third', 'fourth', 'second']),
        (1, 1, ['first', 'second', 'third', 'fourth']),
    ],
)
def test_move_ingredient_moves_item_to_new_index(
    burger, index, new_index, expected_order
):
    burger.ingredients = ['first', 'second', 'third', 'fourth']

    burger.move_ingredient(index, new_index)

    assert burger.ingredients == expected_order


@pytest.mark.parametrize(
    ('bun_price', 'ingredient_prices', 'expected_price'),
    [
        (100.0, [], 200.0),
        (100.0, [25.0], 225.0),
        (125.5, [10.0, 20.5], 281.5),
    ],
)
def test_get_price_returns_double_bun_price_plus_ingredients(
    burger, bun_mock, bun_price, ingredient_prices, expected_price
):
    bun_mock.get_price.return_value = bun_price
    ingredients = []
    for price in ingredient_prices:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = price
        ingredients.append(ingredient)
    burger.bun = bun_mock
    burger.ingredients = ingredients

    result = burger.get_price()

    assert result == expected_price
    bun_mock.get_price.assert_called_once_with()
    for ingredient in ingredients:
        ingredient.get_price.assert_called_once_with()


def test_get_receipt_returns_formatted_burger_description(burger, bun_mock):
    bun_mock.get_name.return_value = 'sesame bun'
    bun_mock.get_price.return_value = 100.0
    sauce = Mock(spec=Ingredient)
    sauce.get_type.return_value = 'SAUCE'
    sauce.get_name.return_value = 'ketchup'
    sauce.get_price.return_value = 25.0
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = 'FILLING'
    filling.get_name.return_value = 'cutlet'
    filling.get_price.return_value = 50.0
    burger.bun = bun_mock
    burger.ingredients = [sauce, filling]
    expected_receipt = (
        '(==== sesame bun ====)\n'
        '= sauce ketchup =\n'
        '= filling cutlet =\n'
        '(==== sesame bun ====)\n\n'
        'Price: 275.0'
    )

    result = burger.get_receipt()

    assert result == expected_receipt
    assert bun_mock.get_name.call_count == 2
    bun_mock.get_price.assert_called_once_with()
    sauce.get_type.assert_called_once_with()
    sauce.get_name.assert_called_once_with()
    sauce.get_price.assert_called_once_with()
    filling.get_type.assert_called_once_with()
    filling.get_name.assert_called_once_with()
    filling.get_price.assert_called_once_with()
