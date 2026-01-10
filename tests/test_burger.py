from _cffi_backend import string
from praktikum.bun import Bun
from conftest import mok_bun, mok_ingredient, mock_ingredients, burger
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


def test_set_buns(mok_bun, burger):
    burger.set_buns(mok_bun)
    assert mok_bun == burger.bun


def test_add_ingredient(mok_ingredient, burger):
    burger.add_ingredient(mok_ingredient)
    assert mok_ingredient in burger.ingredients


def test_remove_ingredient(mok_ingredient, burger):
    burger.add_ingredient(mok_ingredient)
    burger.remove_ingredient(0)
    assert mok_ingredient not in burger.ingredients


def test_move_ingredient(mok_ingredient, burger):
    burger.add_ingredient(mok_ingredient)
    index = burger.ingredients.index(mok_ingredient)
    burger.move_ingredient(0, 3)
    assert burger.ingredients[0] == mok_ingredient


def test_get_receipt(burger):
    burger = Burger()
    bun = Bun("Sdoba", 2.0)
    burger.set_buns(bun)

    ingredient1 = Ingredient("ingredient_type1", "ingredient_name1", 1.0)
    ingredient2 = Ingredient("ingredient_type2", "ingredient_name2", 4.0)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    receipt_output = burger.get_receipt()

    expected_output = """(==== Sdoba ====)
= ingredient_type1 ingredient_name1 =
= ingredient_type2 ingredient_name2 =
(==== Sdoba ====)

Price: 9.0"""
    assert receipt_output.strip() == expected_output.strip()


def test_get_price(burger):
    bun = Bun("Sdoba", 2.0)
    ingredient1 = Ingredient("SAUCE", "tar-tar", 1.0)
    ingredient2 = Ingredient("FILLING", "chocolate", 0.5)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    expected_price = 5.5
    assert burger.get_price() == expected_price
