from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING


def test_set_buns():
    burger = Burger()
    bun = Bun("black bun", 100)

    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient():
    burger = Burger()
    first_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)

    burger.add_ingredient(first_ingredient)
    burger.add_ingredient(second_ingredient)

    burger.remove_ingredient(0)

    assert burger.ingredients == [second_ingredient]


def test_move_ingredient():
    burger = Burger()
    first_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)

    burger.add_ingredient(first_ingredient)
    burger.add_ingredient(second_ingredient)

    burger.move_ingredient(0, 1)

    assert burger.ingredients == [second_ingredient, first_ingredient]


def test_get_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    assert burger.get_price() == 250    

def test_get_receipt():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    expected_receipt = (
    "(==== black bun ====)\n"
    "= filling cutlet =\n"
    "(==== black bun ====)\n"
    "\n"
    "Price: 250")

    assert burger.get_receipt() == expected_receipt