import pytest
from unittest.mock import Mock


def make_ingredient(ingredient_type, name, price):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient


def test_set_buns_sets_bun(burger, mock_bun):
    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun


def test_add_ingredient_adds_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)

    assert burger.ingredients == [mock_ingredient]


def test_remove_ingredient_removes_ingredient(burger):
    ingredient1 = make_ingredient("SAUCE", "hot sauce", 100)
    ingredient2 = make_ingredient("FILLING", "cutlet", 200)

    burger.ingredients = [ingredient1, ingredient2]
    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient2]


@pytest.mark.parametrize(
    "index,new_index,expected",
    [
        (0, 2, ["cutlet", "sour cream", "hot sauce"]),
        (2, 0, ["sour cream", "hot sauce", "cutlet"]),
    ]
)
def test_move_ingredient(burger, index, new_index, expected):
    burger.ingredients = [
        make_ingredient("SAUCE", "hot sauce", 100),
        make_ingredient("FILLING", "cutlet", 200),
        make_ingredient("SAUCE", "sour cream", 300),
    ]

    burger.move_ingredient(index, new_index)

    result = [item.get_name() for item in burger.ingredients]

    assert result == expected


@pytest.mark.parametrize(
    "bun_price, ingredients, expected",
    [
        (100, [100, 200], 500),
        (200, [], 400),
    ]
)
def test_get_price(burger, mock_bun, bun_price, ingredients, expected):
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredients:
        burger.add_ingredient(make_ingredient("SAUCE", "test", price))

    assert burger.get_price() == expected


def test_get_receipt(burger, mock_bun):
    burger.set_buns(mock_bun)
    burger.add_ingredient(make_ingredient("SAUCE", "hot sauce", 100))
    burger.add_ingredient(make_ingredient("FILLING", "cutlet", 200))

    expected = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n\n"
        "Price: 500"
    )

    assert burger.get_receipt() == expected