import sys
import os
import types


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import bun
import ingredient


praktikum = types.ModuleType("praktikum")
praktikum.bun = bun
praktikum.ingredient = ingredient

sys.modules["praktikum"] = praktikum
sys.modules["praktikum.bun"] = bun
sys.modules["praktikum.ingredient"] = ingredient

import pytest
from unittest.mock import Mock


from burger import Burger

class TestBurger:

    def setup_method(self):
        self.burger = Burger()


    def test_init_burger(self):
        assert self.burger.bun is None
        assert self.burger.ingredients == []


    def test_set_buns(self):
        bun = Mock()

        self.burger.set_buns(bun)

        assert self.burger.bun == bun


    def test_add_ingredient(self):
        ingredient = Mock()

        self.burger.add_ingredient(ingredient)

        assert self.burger.ingredients == [ingredient]


    def test_remove_ingredient(self):
        ingredient_1 = Mock()
        ingredient_2 = Mock()

        self.burger.add_ingredient(ingredient_1)
        self.burger.add_ingredient(ingredient_2)

        self.burger.remove_ingredient(0)

        assert self.burger.ingredients == [ingredient_2]


    def test_move_ingredient(self):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()

        self.burger.add_ingredient(ingredient_1)
        self.burger.add_ingredient(ingredient_2)
        self.burger.add_ingredient(ingredient_3)

        self.burger.move_ingredient(0, 2)

        assert self.burger.ingredients == [
            ingredient_2,
            ingredient_3,
            ingredient_1
        ]


    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100, [], 200),
            (100, [50], 250),
            (100, [50, 100], 350),
            (200, [100, 200], 700),
        ]
    )
    def test_get_price(
            self,
            bun_price,
            ingredient_prices,
            expected_price
    ):
        bun = Mock()
        bun.get_price.return_value = bun_price

        self.burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            self.burger.add_ingredient(ingredient)

        assert self.burger.get_price() == expected_price


    def test_get_receipt(self):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100


        ingredient_1 = Mock()
        ingredient_1.get_type.return_value = "SAUCE"
        ingredient_1.get_name.return_value = "hot sauce"
        ingredient_1.get_price.return_value = 50


        ingredient_2 = Mock()
        ingredient_2.get_type.return_value = "FILLING"
        ingredient_2.get_name.return_value = "cutlet"
        ingredient_2.get_price.return_value = 100


        self.burger.set_buns(bun)

        self.burger.add_ingredient(ingredient_1)
        self.burger.add_ingredient(ingredient_2)


        receipt = self.burger.get_receipt()


        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 350" in receipt


   