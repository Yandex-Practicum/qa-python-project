from typing import List

from Prakticum.bun import Bun
from Prakticum.burger import Burger
from database import Database
from Prakticum.ingredient import Ingredient



class TestBurger:
    def test_get_receipt(self):
        database: Database = Database()
        burger: Burger = Burger()
        buns: List[Bun] = database.available_buns()
        burger.set_buns(buns[0])

        assert burger.bun.get_name() == 'black bun'


    def test_add_ingredient_correctly(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[3])

        assert burger.ingredients[0].get_name() == 'cutlet'

    def test_remove_ingredient_correctly(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[3])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        burger.add_ingredient(ingredients[3])
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[0])
        burger.move_ingredient(2,0)

        assert burger.ingredients[0].name == 'hot sauce'

    def test_get_price(self):
        database: Database = Database()
        burger: Burger = Burger()
        ingredients: List[Ingredient] = database.available_ingredients()
        bun = ingredients[0]
        burger.set_buns(bun)
        burger.add_ingredient(ingredients[3])  # 100
        burger.add_ingredient(ingredients[1])  # 200
        price = burger.get_price()
        expected_price = bun.get_price() * 2 + 300

        assert price == expected_price

