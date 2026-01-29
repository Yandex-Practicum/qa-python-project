from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, FILLING_CHICKEN
from unittest.mock import Mock


def test_set_buns():
    bun = Bun("BigMac", 500)
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    ingredient = Mock()
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, 10)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, FILLING_CHICKEN, 100)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(0)
    assert ingredient1 not in burger.ingredients
    assert len(burger.ingredients) == 1


def test_move_ingredient():
    burger = Burger()
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, 10)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, FILLING_CHICKEN, 100)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1


def test_get_price():
    bun = Bun("Sesame Bun", 50)
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, 10)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, FILLING_CHICKEN, 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.get_price() == 50 * 2 + 10 + 100  # 2 булки + 2 ингредиента


def test_get_receipt():
    bun = Bun("BigMac", 500)
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_KETCHUP, 10)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert "BigMac" in receipt
    assert SAUCE_KETCHUP in receipt
    assert "Price: 1010" in receipt  # 500*2 + 10 = 1010
