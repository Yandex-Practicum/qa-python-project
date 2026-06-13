from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


def make_ingredient(ingredient_type, name, price):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient


def test_set_buns_sets_selected_bun(burger, bun):
    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient_adds_ingredient_to_burger(burger):
    ingredient = make_ingredient("SAUCE", "hot sauce", 100)

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_removes_ingredient_by_index(burger):
    first_ingredient = make_ingredient("SAUCE", "hot sauce", 100)
    second_ingredient = make_ingredient("FILLING", "cutlet", 200)
    burger.ingredients = [first_ingredient, second_ingredient]

    burger.remove_ingredient(0)

    assert burger.ingredients == [second_ingredient]


def test_move_ingredient_moves_ingredient_to_new_index(burger):
    first_ingredient = make_ingredient("SAUCE", "hot sauce", 100)
    second_ingredient = make_ingredient("FILLING", "cutlet", 200)
    third_ingredient = make_ingredient("SAUCE", "chili sauce", 300)
    burger.ingredients = [first_ingredient, second_ingredient, third_ingredient]

    burger.move_ingredient(2, 0)

    assert burger.ingredients == [third_ingredient, first_ingredient, second_ingredient]


def test_get_price_returns_buns_twice_plus_ingredient_prices(burger, bun):
    burger.set_buns(bun)
    burger.add_ingredient(make_ingredient("SAUCE", "hot sauce", 100))
    burger.add_ingredient(make_ingredient("FILLING", "cutlet", 200))

    assert burger.get_price() == 500
    bun.get_price.assert_called()


def test_get_receipt_returns_formatted_burger_receipt(burger, bun):
    sauce = make_ingredient("SAUCE", "hot sauce", 100)
    filling = make_ingredient("FILLING", "cutlet", 200)
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt()

    assert receipt == "\n".join(
        [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)\n",
            "Price: 500",
        ]
    )
