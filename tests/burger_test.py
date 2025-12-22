import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


def create_mock_bun(name="black bun", price=100):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun


def create_mock_ingredient(name="cutlet", price=50, ingredient_type="filling"):
    ingredient = Mock()
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    ingredient.get_type.return_value = ingredient_type
    return ingredient


def test_set_buns():
    burger = Burger()
    bun = create_mock_bun()

    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    ingredient = create_mock_ingredient()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()
    ingredient = create_mock_ingredient()
    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)

    assert ingredient not in burger.ingredients


def test_move_ingredient():
    burger = Burger()
    ingredient_1 = create_mock_ingredient(name="cutlet")
    ingredient_2 = create_mock_ingredient(name="cheese")

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == ingredient_2
    assert burger.ingredients[1] == ingredient_1


@pytest.mark.parametrize(
    "ingredients, expected_price",
    [
        ([], 200),  # только булка (100 * 2)
        ([create_mock_ingredient(price=50)], 250),
        (
            [
                create_mock_ingredient(price=50),
                create_mock_ingredient(price=30),
            ],
            280,
        ),
    ],
)
def test_get_price(ingredients, expected_price):
    burger = Burger()
    burger.set_buns(create_mock_bun(price=100))

    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    assert burger.get_price() == expected_price


def test_get_receipt():
    burger = Burger()
    bun = create_mock_bun(name="black bun", price=100)
    ingredient = create_mock_ingredient(name="cutlet", price=50, ingredient_type="filling")

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "(==== black bun ====)" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 250" in receipt
