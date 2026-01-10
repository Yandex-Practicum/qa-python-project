from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


def main():
    database: Database = Database()
    burger: Burger = Burger()
    buns: List[Bun] = database.available_buns()
    ingredients: List[Ingredient] = database.available_ingredients()
    burger.set_buns(buns[0])
    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])
    burger.move_ingredient(2, 1)
    burger.remove_ingredient(3)
    print(burger.get_receipt())

if __name__ == "__main__":
    main()
