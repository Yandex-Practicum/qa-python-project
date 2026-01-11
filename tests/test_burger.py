from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


def test_burger_set_buns():
    bun = Bun('bun', 3)
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_burger_add_ingredient():
    ingredient = Ingredient('ingredient', 'name', 3)
    burger = Burger()
    burger.add_ingredient(ingredient)
    assert burger.ingredients[0] == ingredient


def test_burger_remove_ingredient():
    ingredient = Ingredient('ingredient', 'name', 3)
    burger = Burger()
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert burger.ingredients == []


def test_burger_move_ingredient():
    ingredient1 = Ingredient('ingredient', 'name1', 3)
    ingredient2 = Ingredient('ingredient', 'name2', 3)
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1


def test_burger_get_receipt():
    bun = Bun('bun', 3)
    ingredient1 = Ingredient('ingredient', 'name1', 3)
    ingredient2 = Ingredient('ingredient', 'name2', 3)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    receipt = burger.get_receipt()
    assert ('(==== bun ====)\n'
            '= ingredient name1 =\n'
            '= ingredient name2 =\n'
            '(==== bun ====)\n'
            '\n'
            'Price: 12') in receipt
