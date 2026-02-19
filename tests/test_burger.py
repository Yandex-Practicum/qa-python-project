from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)

    assert burger.bun == bun_mock


def test_add_ingredient(ingredient_mock):
    burger = Burger()
    burger.add_ingredient(ingredient_mock)

    assert burger.ingredients == [ingredient_mock]


def test_remove_ingredient():
    burger = Burger()

    i1 = Mock()
    i2 = Mock()

    burger.add_ingredient(i1)
    burger.add_ingredient(i2)

    burger.remove_ingredient(0)

    assert burger.ingredients == [i2]


def test_move_ingredient():
    burger = Burger()

    i1 = Mock()
    i2 = Mock()
    i3 = Mock()

    burger.ingredients = [i1, i2, i3]

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [i2, i3, i1]


@pytest.mark.parametrize('bun_price, ing_prices, expected', [
    (100, [], 200),
    (100, [50], 250),
    (200, [10, 20], 430),
])
def test_get_price(bun_price, ing_prices, expected):
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)

    for price in ing_prices:
        ingredient = Mock()
        ingredient.get_price.return_value = price

        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected
