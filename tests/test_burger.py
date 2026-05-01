import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 200
    return bun


@pytest.mark.parametrize("name, price", [("cheese", 50), ("sauce", 25), ("bacon", 100)])
def test_add_ingredient_appends_in_order(burger, name, price):
    ingredient = Mock()
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price

    burger.add_ingredient(ingredient)

    assert burger.ingredients[-1] is ingredient


def test_set_buns_sets_bun_instance(burger, bun_mock):
    burger.set_buns(bun_mock)

    assert burger.bun is bun_mock


def test_remove_ingredient_by_index(burger):
    first = Mock()
    second = Mock()
    burger.ingredients = [first, second]

    burger.remove_ingredient(0)

    assert burger.ingredients == [second]


@pytest.mark.parametrize(
    "start, index, new_index, expected",
    [
        (["a", "b", "c"], 0, 2, ["b", "c", "a"]),
        (["a", "b", "c"], 2, 0, ["c", "a", "b"]),
    ],
)
def test_move_ingredient_reorders_items(burger, start, index, new_index, expected):
    burger.ingredients = start.copy()

    burger.move_ingredient(index, new_index)

    assert burger.ingredients == expected


def test_get_price_uses_bun_price_twice_and_all_ingredients(burger, bun_mock):
    ingredient_1 = Mock()
    ingredient_1.get_price.return_value = 50
    ingredient_2 = Mock()
    ingredient_2.get_price.return_value = 25

    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    total = burger.get_price()

    assert total == 475
    bun_mock.get_price.assert_called_once_with()
    ingredient_1.get_price.assert_called_once_with()
    ingredient_2.get_price.assert_called_once_with()


def test_get_receipt_returns_expected_text_and_calls_dependencies(burger, bun_mock):
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot chili"
    ingredient.get_price.return_value = 30

    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert receipt == "\n".join(
        [
            "(==== black bun ====)",
            "= sauce hot chili =",
            "(==== black bun ====)\n",
            "Price: 430",
        ]
    )
    assert bun_mock.get_name.call_count == 2
    ingredient.get_type.assert_called_once_with()
    ingredient.get_name.assert_called_once_with()
    bun_mock.get_price.assert_called_once_with()
    ingredient.get_price.assert_called_once_with()
