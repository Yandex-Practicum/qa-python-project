from unittest.mock import Mock

from data.bun_data import BunData
from data.burger_data import BurgerData
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_cheack_name(self):
        burger = Burger()
        burger.set_buns(BunData.bun)
        assert burger.bun == BunData.bun

    def test_add_ingredient(self, add_ingredient):
        add_ingredient.add_ingredient(BurgerData.ingredient_type)
        assert 'Рыба' in add_ingredient.ingredients

    def test_remove_ingredient_remove_one(self, add_ingredient):
        add_ingredient.remove_ingredient(0)
        assert add_ingredient.ingredients == []

    def test_move_ingredient_changest_index(self, add_ingredient_two):
        add_ingredient_two.move_ingredient(0, 1)
        assert add_ingredient_two.ingredients[0] == 'Мясо'

    def test_get_price_get_price_25(self, ingredient_mock, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 25.0 and type(burger.get_price()) == float

    def test_recipte(self, ingredient_mock, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = '(==== Зерновая ====)\n= рыба Скумбрия =\n(==== Зерновая ====)\n\nPrice: 25.0'
        assert receipt == burger.get_receipt()


