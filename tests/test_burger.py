import pytest
from unittest.mock import Mock

from burger import Burger
from ingredient import Ingredient


def test_burger_init_sets_empty_state():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns_assigns_bun_object():
    bun = Mock(get_name=Mock(return_value="plain bun"), get_price=Mock(return_value=100.0))
    burger = Burger()

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_appends_ingredient_to_list():
    ingredient = Ingredient("FILLING", "cutlet", 35.0)
    burger = Burger()

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_deletes_item_by_index():
    first = Ingredient("SAUCE", "hot sauce", 10.0)
    second = Ingredient("FILLING", "cutlet", 35.0)
    burger = Burger()
    burger.add_ingredient(first)
    burger.add_ingredient(second)

    burger.remove_ingredient(0)

    assert burger.ingredients == [second]


@pytest.mark.parametrize(
    "ingredient_prices,expected_total",
    [
        ([100.0], 300.0),
        ([10.0, 20.0], 230.0),
        ([5.0, 15.0, 25.0], 245.0),
    ],
)
def test_get_price_includes_bun_twice_and_all_ingredient_prices(
    ingredient_prices, expected_total
):
    # Мокаем булочку и ингредиенты, чтобы тест был независим от реализации Ingredient.
    bun = Mock(get_name=Mock(return_value="mock bun"), get_price=Mock(return_value=100.0))
    burger = Burger()
    burger.set_buns(bun)

    for price in ingredient_prices:
        ingredient = Mock(get_price=Mock(return_value=price))
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_total


@pytest.mark.parametrize(
    "initial_names,move_from,move_to,expected_names",
    [
        (["hot sauce", "cutlet", "sausage"], 2, 0, ["sausage", "hot sauce", "cutlet"]),
        (["sour cream", "dinosaur", "cutlet"], 0, 2, ["dinosaur", "cutlet", "sour cream"]),
    ],
)
def test_move_ingredient_reorders_list_correctly(
    initial_names, move_from, move_to, expected_names
):
    burger = Burger()

    for name in initial_names:
        burger.add_ingredient(Ingredient("FILLING", name, 1.0))

    burger.move_ingredient(move_from, move_to)
    assert [ingredient.get_name() for ingredient in burger.ingredients] == expected_names


def test_get_receipt_outputs_bun_and_ingredient_lines():
    bun = Mock(get_name=Mock(return_value="test bun"), get_price=Mock(return_value=50.0))
    ingredient = Mock(
        get_type=Mock(return_value="SAUCE"),
        get_name=Mock(return_value="hot sauce"),
        get_price=Mock(return_value=10.0),
    )
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "(==== test bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "Price: 110.0" in receipt
