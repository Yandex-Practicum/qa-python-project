import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = 'black bun'
    bun_mock.get_price.return_value = 100
    return bun_mock


def make_ingredient(ingredient_type='SAUCE', name='hot sauce', price=50):
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = ingredient_type
    ingredient_mock.get_name.return_value = name
    ingredient_mock.get_price.return_value = price
    return ingredient_mock


def test_set_buns_sets_bun(burger, bun):
    burger.set_buns(bun)
    assert burger.bun == bun


@pytest.mark.parametrize(
    'ingredient_type, ingredient_name, ingredient_price',
    [
        ('SAUCE', 'hot sauce', 50),
        ('FILLING', 'cutlet', 200),
    ]
)
def test_add_ingredient_adds_ingredient_to_list(
        burger, ingredient_type, ingredient_name, ingredient_price
):
    ingredient = make_ingredient(
        ingredient_type,
        ingredient_name,
        ingredient_price
    )

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_removes_ingredient_by_index(burger):
    first_ingredient = make_ingredient('SAUCE', 'hot sauce', 50)
    second_ingredient = make_ingredient('FILLING', 'cutlet', 200)
    burger.ingredients = [first_ingredient, second_ingredient]

    burger.remove_ingredient(0)

    assert burger.ingredients == [second_ingredient]


def test_move_ingredient_moves_ingredient_to_new_index(burger):
    first_ingredient = make_ingredient('SAUCE', 'hot sauce', 50)
    second_ingredient = make_ingredient('FILLING', 'cutlet', 200)
    third_ingredient = make_ingredient('SAUCE', 'chili sauce', 80)
    burger.ingredients = [first_ingredient, second_ingredient, third_ingredient]

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [
        second_ingredient,
        third_ingredient,
        first_ingredient
    ]


@pytest.mark.parametrize(
    'ingredient_prices, expected_price',
    [
        ([], 200),
        ([50], 250),
        ([50, 200], 450),
    ]
)
def test_get_price_returns_bun_price_twice_plus_ingredients_price(
        burger, bun, ingredient_prices, expected_price
):
    burger.set_buns(bun)
    burger.ingredients = [
        make_ingredient(price=price) for price in ingredient_prices
    ]

    assert burger.get_price() == expected_price


def test_get_receipt_returns_receipt_with_bun_ingredients_and_price(
        burger, bun
):
    burger.set_buns(bun)
    burger.ingredients = [
        make_ingredient('SAUCE', 'hot sauce', 50),
        make_ingredient('FILLING', 'cutlet', 200),
    ]

    expected_receipt = (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '(==== black bun ====)\n\n'
        'Price: 450'
    )

    assert burger.get_receipt() == expected_receipt