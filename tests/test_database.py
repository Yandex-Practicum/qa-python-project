from database import Database
from burger import Burger


def test_set_buns_with_bun_from_database():
    database = Database()
    bun = database.available_buns()[0]

    burger = Burger()
    burger.set_buns(bun)

    assert burger.bun == bun


def test_get_price_with_bun_from_database():
    database = Database()
    bun = database.available_buns()[0]

    burger = Burger()
    burger.set_buns(bun)

    assert burger.get_price() == bun.get_price() * 2


def test_add_ingredient_from_database():
    database = Database()
    ingredient = database.available_ingredients()[0]

    burger = Burger()
    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_get_price_with_bun_and_ingredients_from_database():
    database = Database()
    bun = database.available_buns()[0]
    ingredient = database.available_ingredients()[0]

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    expected_price = bun.get_price() * 2 + ingredient.get_price()
    assert burger.get_price() == expected_price


def test_get_receipt_contains_ingredient_from_database():
    database = Database()
    bun = database.available_buns()[0]
    ingredient = database.available_ingredients()[0]

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert ingredient.get_name() in receipt