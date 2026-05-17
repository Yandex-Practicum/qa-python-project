import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


def test_set_buns_sets_bun():
    burger = Burger()
    mock_bun = Mock()

    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun


def test_add_ingredient_adds_item_to_ingredients():
    burger = Burger()
    mock_ingredient = Mock()

    burger.add_ingredient(mock_ingredient)

    assert burger.ingredients == [mock_ingredient]


def test_remove_ingredient_removes_item_by_index():
    burger = Burger()
    ingredient_1 = Mock()
    ingredient_2 = Mock()

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_2]


def test_move_ingredient_moves_item_to_new_position():
    burger = Burger()
    ingredient_1 = Mock()
    ingredient_2 = Mock()
    ingredient_3 = Mock()

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.add_ingredient(ingredient_3)
    burger.move_ingredient(0, 2)

    assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]


@pytest.mark.parametrize(
    'bun_price, ingredient_prices, expected_price',
    [
        (10, [], 20),
        (10, [5], 25),
        (12, [3, 7], 34),
    ]
)
def test_get_price_returns_correct_price(bun_price, ingredient_prices, expected_price):
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == expected_price


def test_get_receipt_returns_correct_receipt():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100
    burger.set_buns(mock_bun)

    ingredient_1 = Mock()
    ingredient_1.get_type.return_value = 'SAUCE'
    ingredient_1.get_name.return_value = 'hot sauce'
    ingredient_1.get_price.return_value = 100

    ingredient_2 = Mock()
    ingredient_2.get_type.return_value = 'FILLING'
    ingredient_2.get_name.return_value = 'cutlet'
    ingredient_2.get_price.return_value = 200

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    expected_receipt = (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '(==== black bun ====)\n\n'
        'Price: 500'
    )

    assert burger.get_receipt() == expected_receipt