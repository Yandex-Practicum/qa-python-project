from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


def test_set_buns_sets_bun_reference(bun_mock):
    burger = Burger()

    burger.set_buns(bun_mock)

    assert burger.bun is bun_mock


def test_add_ingredient_appends_to_list(ingredient_mock):
    burger = Burger()

    burger.add_ingredient(ingredient_mock)

    assert burger.ingredients == [ingredient_mock]


def test_remove_ingredient_deletes_by_index():
    burger = Burger()
    ing1, ing2 = Mock(), Mock()
    burger.ingredients = [ing1, ing2]

    burger.remove_ingredient(0)

    assert burger.ingredients == [ing2]


def test_move_ingredient_reorders_list():
    burger = Burger()
    ing1, ing2, ing3 = Mock(), Mock(), Mock()
    burger.ingredients = [ing1, ing2, ing3]

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [ing2, ing3, ing1]


def test_get_price_sums_bun_double_and_ingredients(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)

    ing1, ing2 = Mock(), Mock()
    ing1.get_price.return_value = 10.0
    ing2.get_price.return_value = 15.5
    burger.ingredients = [ing1, ing2]

    assert burger.get_price() == 50.0 * 2 + 10.0 + 15.5


def test_get_receipt_formats_lines_and_uses_lowercase_types(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)

    sauce = Mock()
    sauce.get_type.return_value = 'SAUCE'
    sauce.get_name.return_value = 'hot sauce'
    sauce.get_price.return_value = 10.0

    filling = Mock()
    filling.get_type.return_value = 'FILLING'
    filling.get_name.return_value = 'cutlet'
    filling.get_price.return_value = 20.0

    burger.ingredients = [sauce, filling]

    receipt = burger.get_receipt()

    expected = (
        '(==== test bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '(==== test bun ====)\n\n'
        'Price: 130.0'
    )

    assert receipt == expected
