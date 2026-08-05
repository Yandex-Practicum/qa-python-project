import pytest
from unittest.mock import MagicMock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_burger_initializes_without_bun():
    burger = Burger()

    assert burger.bun is None


def test_burger_initializes_with_empty_ingredients():
    burger = Burger()

    assert burger.ingredients == []


def test_set_buns_sets_bun():
    burger = Burger()
    bun = Bun("black bun", 100)

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_adds_ingredient_to_burger():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_removes_ingredient_by_index():
    burger = Burger()
    ingredient_to_remove = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    ingredient_to_keep = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    burger.ingredients = [ingredient_to_remove, ingredient_to_keep]

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_to_keep]


@pytest.mark.parametrize("index", [1, -2])
def test_remove_ingredient_with_invalid_index_raises_index_error(index):
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.remove_ingredient(index)


def test_move_ingredient_moves_ingredient_to_new_index():
    burger = Burger()
    first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    third_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "cheese sauce", 60)
    burger.ingredients = [first_ingredient, second_ingredient, third_ingredient]

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [second_ingredient, third_ingredient, first_ingredient]


@pytest.mark.parametrize("index", [1, -2])
def test_move_ingredient_with_invalid_source_index_raises_index_error(index):
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.move_ingredient(index, 0)


def test_get_price_returns_total_price_with_two_buns_and_all_ingredients():
    burger = Burger()
    bun = Bun("black bun", 100.0)
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200.0)
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    price = burger.get_price()

    assert price == 450.0


def test_get_price_returns_total_with_mocked_bun_and_ingredients():
    burger = Burger()
    bun = MagicMock()
    bun.get_price.return_value = 100.0
    sauce = MagicMock()
    sauce.get_price.return_value = 50.0
    filling = MagicMock()
    filling.get_price.return_value = 200.0
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    assert burger.get_price() == 450.0


def test_get_receipt_returns_formatted_receipt():
    burger = Burger()
    bun = Bun("black bun", 100.0)
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0)
    filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200.0)
    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt()

    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 450.0"
    )
    assert receipt == expected_receipt
