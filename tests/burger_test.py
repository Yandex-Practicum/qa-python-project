from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestBurger:
    def setup_method(self):
        self.burger = Burger()
        bun = Bun('Булочка', 100)
        self.burger.set_buns(bun)
        self.database = Database()
        self.ingredients = self.database.available_ingredients()

    def test_set_buns(self):
        assert self.burger.bun.get_name() == 'Булочка'
        assert self.burger.bun.get_price() == 100

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.ingredients[1])
        assert self.burger.ingredients[0].get_name() == 'sour cream'
        assert self.burger.ingredients[0].get_type() == 'SAUCE'
        assert self.burger.ingredients[0].get_price() == 200

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.ingredients[1])
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 0

    def test_move_ingredient(self):
        self.burger.add_ingredient(self.ingredients[1])
        self.burger.add_ingredient(self.ingredients[4])
        self.burger.add_ingredient(self.ingredients[3])
        self.burger.add_ingredient(self.ingredients[5])

        # Переместим слой с ингредиентом
        self. burger.move_ingredient(2, 1)

        assert self.burger.ingredients[1].get_name() == 'cutlet'
        assert self.burger.ingredients[1].get_type() == 'FILLING'
        assert self.burger.ingredients[1].get_price() == 100

    def test_get_price(self):
        price = self.burger.get_price()
        assert price == 200

    def test_get_receipt(self):
        database: Database = Database()
        ingredients: List[Ingredient] = database.available_ingredients()
        self.burger.add_ingredient(ingredients[1])
        self.burger.add_ingredient(ingredients[4])
        self.burger.add_ingredient(ingredients[3])
        self.burger.add_ingredient(ingredients[5])

        # Распечатаем рецепт бургера
        receipt = self.burger.get_receipt()
        assert receipt == ('(==== Булочка ====)\n= sauce sour cream =\n= filling dinosaur =\n= filling cutlet =\n='
                           ' filling sausage =\n(==== Булочка ====)\n\nPrice: 1000')
