from unittest.mock import Mock

import DATA
from DATA import *
from praktikum.burger import Burger


def test_burger_constructor_bun(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_burger_constructor_ingridient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert burger.ingredients[0] == mock_ingredient


def test_add_ingredient(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1


def test_remove_ingredient(burger_complete):
    burger_complete.remove_ingredient(0)
    assert len(burger_complete.ingredients) == 0


def test_move_ingredient(burger_complete, mock_ingredient_2):
    burger_complete.add_ingredient(mock_ingredient_2)
    burger_complete.move_ingredient(0, 1)
    assert burger_complete.ingredients[0] is mock_ingredient_2


def test_get_price(burger, mock_bun, mock_ingredient):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    actual_price = burger.get_price()
    expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
    assert actual_price == expected_price


def test_get_receipt():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DATA.Buns.WHITE_BUN
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = Ingridients.HOT_SAUCE
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock = Mock()
    mock.get_price.return_value = DATA.Price.WHITE_BUN_PRICE

    burger = Burger()
    burger.bun = mock_bun
    burger.ingredients = [mock_ingredient]
    burger.get_price = mock.get_price

    assert (burger.get_receipt() == '(==== white bun ====)\n'
                                    '= sauce hot sauce =\n'
                                    '(==== white bun ====)\n'
                                    '\n'
                                    'Price: 200')
