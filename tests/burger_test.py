from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


def test_set_buns_sets_bun(burger):
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient_adds_ingredient_to_end(burger):
    first_ingredient = Mock()
    second_ingredient = Mock()

    burger.add_ingredient(first_ingredient)
    burger.add_ingredient(second_ingredient)

    assert burger.ingredients == [first_ingredient, second_ingredient]


@pytest.mark.parametrize(
    'initial, index, expected',
    [
        (['sauce', 'cutlet', 'cheese'], 0, ['cutlet', 'cheese']),
        (['sauce', 'cutlet', 'cheese'], 1, ['sauce', 'cheese']),
    ],
)
def test_remove_ingredient_removes_by_index(burger, initial, index, expected):
    burger.ingredients = initial.copy()

    burger.remove_ingredient(index)

    assert burger.ingredients == expected


@pytest.mark.parametrize(
    'initial, index, new_index, expected',
    [
        (['sauce', 'cutlet', 'cheese'], 0, 2, ['cutlet', 'cheese', 'sauce']),
        (['sauce', 'cutlet', 'cheese'], 2, 0, ['cheese', 'sauce', 'cutlet']),
    ],
)
def test_move_ingredient_moves_ingredient_to_new_index(burger, initial, index, new_index, expected):
    burger.ingredients = initial.copy()

    burger.move_ingredient(index, new_index)

    assert burger.ingredients == expected


def test_get_price_returns_double_bun_price_plus_ingredients_prices(burger):
    bun = Mock()
    bun.get_price.return_value = 100
    sauce = Mock()
    sauce.get_price.return_value = 20
    filling = Mock()
    filling.get_price.return_value = 50
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    price = burger.get_price()

    assert price == 270


def test_get_receipt_returns_formatted_receipt_with_total_price(burger):
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    sauce = Mock()
    sauce.get_type.return_value = 'SAUCE'
    sauce.get_name.return_value = 'hot sauce'
    sauce.get_price.return_value = 20
    filling = Mock()
    filling.get_type.return_value = 'FILLING'
    filling.get_name.return_value = 'cutlet'
    filling.get_price.return_value = 50
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt()

    assert receipt == (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '(==== black bun ====)\n'
        '\n'
        'Price: 270'
    )
