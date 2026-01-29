from praktikum.burger import Burger
from input_data import Data
from praktikum.bun import Bun
from praktikum.database import Database


class TestBurger:

    def test_set_buns_bon_name_true(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN_NAME, Data.BLACK_BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_list_with_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient(Data.INGREDIENT_HOT_SAUCE_PRICE)
        assert burger.ingredients == [Data.INGREDIENT_HOT_SAUCE_PRICE]

    def test_remove_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient(Data.INGREDIENT_DINOSAUR_NAME)
        burger.remove_ingredient(0)
        assert Data.INGREDIENT_DINOSAUR_NAME not in burger.ingredients

    def test_move_ingredient_success(self):
        burger = Burger()
        burger.add_ingredient(Data.INGREDIENT_DINOSAUR_NAME)
        burger.add_ingredient(Data.INGREDIENT_CUTLET_NAME)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == Data.INGREDIENT_CUTLET_NAME
        assert burger.ingredients[1] == Data.INGREDIENT_DINOSAUR_NAME

    def test_get_price_burger_success(self):
        data = Database()
        burger = Burger()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        assert burger.get_price() == 500

    def test_get_receipt_burger_success(self):
        data = Database()
        burger = Burger()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        result = '''(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300'''
        assert burger.get_receipt() == result

