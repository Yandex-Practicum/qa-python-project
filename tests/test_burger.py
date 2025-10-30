import pytest
from praktikum.burger import Burger
from data import data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []

    def test_set_buns_to_burger(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun.name == data.bun_name

    def test_add_ingredient_one_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].name == data.ingredient_name
        assert burger.ingredients[0].type == data.ingredient_type
        assert burger.ingredients[0].price == data.ingredient_price

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].name == data.ingredient_name
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].name == data.ingredient_name
        assert burger.ingredients[1].name == data.ingredient_name

    def test_get_price_burger(self, burger, ingredient, bun):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        price = burger.bun.price * 2 + burger.ingredients[0].price
        assert price == burger.get_price()

    def test_get_receipt_burger(self, burger, ingredient, bun):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        price = burger.bun.price * 2 + burger.ingredients[0].price
        assert (
            burger.get_receipt()
            == f"(==== {data.bun_name} ====)\n= {data.ingredient_type.lower()} {data.ingredient_name} =\n(==== {data.bun_name} ====)\n\nPrice: {price}"
        )
