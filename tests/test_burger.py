from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_bun(self):
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "cheese", 30)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 90)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient_sauce
        assert burger.ingredients[1] == ingredient_filling
        burger.remove_ingredient(0)
        burger.remove_ingredient(0)

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "cheese", 30)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 90)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 40)
        ingredient_3 = Ingredient(INGREDIENT_TYPE_FILLING, "meet", 150)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_3
        assert burger.ingredients[2] == ingredient_1

    def test_get_price(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 40)
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_price = bun.get_price() * 2 + ingredient_1.get_price() + ingredient_2.get_price()
        print(expected_price)
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 40)
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'= {str(ingredient_1.get_type()).lower()} {ingredient_1.get_name()} =\n'
            f'= {str(ingredient_2.get_type()).lower()} {ingredient_2.get_name()} =\n'
            f'(==== {bun.get_name()} ====)\n'
            '\n'
            f'Price: {burger.get_price()}'
        )
        assert burger.get_receipt() == expected_receipt



