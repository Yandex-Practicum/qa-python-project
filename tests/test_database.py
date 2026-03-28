import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from database import Database
from burger import Burger


class TestDatabase:

    def test_burger_price_with_single_bun(self):
        db = Database()
        burger = Burger()

        bun = db.available_buns()[0]
        burger.set_buns(bun)
        
        expected_price = bun.get_price() * 2
        assert burger.get_price() == expected_price

    def test_burger_price_with_bun_and_ingredients(self):
        db = Database()
        burger = Burger()

        bun = db.available_buns()[0]
        burger.set_buns(bun)

        ingredient = db.available_ingredients()[0]
        burger.add_ingredient(ingredient)

        
        expected_price = bun.get_price() * 2 + ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_burger_receipt_contains_bun_and_ingredient(self):
        db = Database()
        burger = Burger()

        bun = db.available_buns()[0]
        burger.set_buns(bun)

        ingredient = db.available_ingredients()[0]
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        
        assert bun.get_name() in receipt
        assert ingredient.get_name() in receipt

        
        expected_price = bun.get_price() * 2 + ingredient.get_price()
        assert f"Price: {expected_price}" in receipt

    def test_burger_with_multiple_ingredients(self):
        db = Database()
        burger = Burger()

        bun = db.available_buns()[0]
        burger.set_buns(bun)

        ingredients = db.available_ingredients()[:3]
        for ing in ingredients:
            burger.add_ingredient(ing)

        expected_price = bun.get_price() * 2 + sum(ing.get_price() for ing in ingredients)
        assert burger.get_price() == expected_price