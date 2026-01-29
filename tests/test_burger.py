from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import pytest

def test_burger_init():
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []

def test_burger_set_buns():
    burger = Burger()
    bun = Bun("black bun", 100)
    burger.set_buns(bun)
    assert burger.bun == bun

def test_burger_add_ingredient():
    burger = Burger()
    ingredient = Ingredient("SAUCE", "hot sauce", 100)
    burger.add_ingredient(ingredient)
    assert burger.ingredients[0] == ingredient

def test_burger_remove_ingredient():
    burger = Burger()
    ingredient1 = Ingredient("SAUCE", "hot sauce", 100)
    ingredient2 = Ingredient("FILLING", "cutlet", 200)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(1)
    assert burger.ingredients == [ingredient1]

def test_burger_move_ingredient():
    burger = Burger()
    ingredient1 = Ingredient("SAUCE", "hot sauce", 100)
    ingredient2 = Ingredient("FILLING", "cutlet", 200)
    ingredient3 = Ingredient("FILLING", "dinosaur", 300)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)
    burger.move_ingredient(2, 1)
    assert burger.ingredients == [ingredient1, ingredient3, ingredient2]

def test_burger_get_price():
    burger = Burger()
    bun = Bun("black bun", 100)
    ingredient1 = Ingredient("SAUCE", "hot sauce", 100)
    ingredient2 = Ingredient("FILLING", "cutlet", 200)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.get_price() == 500

def test_burger_get_receipt():
    burger = Burger()
    bun = Bun("black bun", 100)
    ingredient1 = Ingredient("SAUCE", "hot sauce", 100)
    ingredient2 = Ingredient("FILLING", "cutlet", 200)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    receipt = burger.get_receipt()
    expected_receipt = "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== black bun ====)\n\nPrice: 500"
    assert receipt == expected_receipt

def test_burger_remove_ingredient_with_incorrect_index():
    burger = Burger()
    with pytest.raises(IndexError):
        burger.remove_ingredient(10)  # Пытаемся удалить ингредиент по несуществующему индексу







