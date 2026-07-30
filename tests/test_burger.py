from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_burger_initializes_without_bun_and_ingredients():
    burger = Burger()

    assert burger.bun is None
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


def test_move_ingredient_moves_ingredient_to_new_index():
    burger = Burger()
    first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
    second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
    third_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "cheese sauce", 60)
    burger.ingredients = [first_ingredient, second_ingredient, third_ingredient]

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [second_ingredient, third_ingredient, first_ingredient]
