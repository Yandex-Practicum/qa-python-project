import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestPraktikum:


    def test_burger_creation(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []


    def test_set_bun(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_add_ingredients(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ing1
        assert burger.ingredients[1] == ing2


    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        ing3 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 50)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing3
        assert burger.ingredients[2] == ing1


    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2


    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)

        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450" in receipt                  # 100*2 + 100 + 150


    def test_get_receipt_no_ingredients(self):
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)

        receipt = burger.get_receipt()
        assert "(==== white bun ====)" in receipt
        assert "Price: 400" in receipt


