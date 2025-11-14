import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

def test_burger_set_buns():
    bun_mock = Mock(spec=Bun)
    burger = Burger()

    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock

def test_burger_add_ingredient():
    ingredient_mock = Mock(spec=Ingredient)
    burger = Burger()

    burger.add_ingredient(ingredient_mock)
    assert ingredient_mock in burger.ingredients

def test_burger_remove_ingredient():
    ingredient_mock = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient_mock)

    burger.remove_ingredient(0)
    assert ingredient_mock not in burger.ingredients

def test_burger_move_ingredient():
    ingredient1_mock = Mock(spec=Ingredient)
    ingredient2_mock = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient1_mock)
    burger.add_ingredient(ingredient2_mock)

    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2_mock, ingredient1_mock]

def test_burger_get_price():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 2.5
    ingredient1_mock = Mock(spec=Ingredient)
    ingredient1_mock.get_price.return_value = 1.0
    ingredient2_mock = Mock(spec=Ingredient)
    ingredient2_mock.get_price.return_value = 1.5

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient1_mock)
    burger.add_ingredient(ingredient2_mock)

    assert burger.get_price() == 7.5

def test_burger_get_receipt():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = "Sesame"
    bun_mock.get_price.return_value = 2.5

    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = "Cheese"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 1.0

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)

    receipt = (
        f"(==== {burger.bun.get_name()} ====)\n"
        f"= filling {burger.ingredients[0].get_name()} =\n"
        f"(==== {burger.bun.get_name()} ====)\n"
        f"Price: {burger.get_price()}"
    )

    expected_receipt = (
        "(==== Sesame ====)\n"
        "= filling Cheese =\n"
        "(==== Sesame ====)\n"
        "Price: 6.0"
    )
    assert receipt == expected_receipt
