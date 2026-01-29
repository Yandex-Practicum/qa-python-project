import bun
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns("black bun")
        assert burger.bun == "black bun"

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient("hot sauce")
        assert burger.ingredients[0] == "hot sauce"

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient("hot sauce")
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient("hot sauce")
        burger.add_ingredient("sour cream")
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == "hot sauce"

    def test_get_price(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING,"hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        assert burger.get_price() == 400

    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING,"hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        receipt = burger.get_receipt()
        assert receipt == "(==== black bun ====)\n= filling hot sauce =\n= filling cutlet =\n(==== black bun ====)\n\nPrice: 400"

