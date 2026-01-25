import pytest
from unittest.mock import Mock
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.ingredient import Ingredient


def test_burger_init():
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []


def test_burger_set_buns():
    burger = Burger()
    bun = Mock(spec=Bun)
    burger.set_buns(bun)
    assert burger.bun == bun


def test_burger_add_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients


def test_burger_remove_ingredient():
    burger = Burger()
    ingredient = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients


def test_burger_move_ingredient():
    burger = Burger()
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]


def test_burger_get_price():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    burger.add_ingredient(ingredient)

    assert burger.get_price() == 300  # 100*2 + 50*2


def test_burger_get_receipt():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "bun"
    bun.get_price.return_value = 100
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "ingredient"
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_price.return_value = 50

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()
    assert "(==== bun ====)" in receipt
    assert "= sauce ingredient =" in receipt
    assert "Price: 250" in receipt
