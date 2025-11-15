import pytest
from praktikum.burger import Burger
from praktikum.datasets import *

class TestBurger:

    def test_set_buns_valid_bun_return_correct_sets(self):
        burger = Burger()
        burger.set_buns(classic_bun)
        assert burger.bun == classic_bun

    def test_add_ingredient_valid_ingredient_add_to_list(self):
        burger = Burger()
        burger.add_ingredient(ingredient_cutlet)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_cutlet

    def test_remove_ingredient_valid_index_ingredient_remove_succes(self):
        burger = Burger()
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_ketchup

    def test_move_ingredient_valid_index_ingredient_move_succes(self):
        burger = Burger()
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_ketchup
        assert burger.ingredients[1] == ingredient_cutlet

    def test_remove_ingredient_removes_correct_ingredient(self):
        burger = Burger()
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ingredient_ketchup

    def test_move_ingredient_changes_first_element(self):
        burger = Burger()
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_ketchup

    def test_get_price_bun_and_ingredients_return_total_price(self):
        burger = Burger()
        burger.set_buns(classic_bun)
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        price = burger.get_price()
        assert price == 500

    def test_get_receipt_with_ingredients_return_complete_receipt(self):
        burger = Burger()
        burger.set_buns(classic_bun)
        burger.add_ingredient(ingredient_cutlet)
        burger.add_ingredient(ingredient_ketchup)
        receipt = burger.get_receipt()
        assert "(==== Классическая ====)" in receipt
        assert "= котлета начинка =" in receipt
        assert "= кетчуп соус =" in receipt
        assert "Price: 500" in receipt 