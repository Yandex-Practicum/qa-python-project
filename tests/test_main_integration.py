from praktikum.burger import Burger
from praktikum.database import Database


def test_main_scenario_receipt():
    database = Database()
    burger = Burger()

    buns = database.available_buns()
    ingredients = database.available_ingredients()

    burger.set_buns(buns[0])
    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    burger.move_ingredient(2, 1)
    burger.remove_ingredient(3)

    receipt = burger.get_receipt()


    assert burger.get_price() == 700
    assert "(==== black bun ====)" in receipt
