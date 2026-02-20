import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurgerIntegration:
    
    def setup_method(self):
        self.burger = Burger()
        self.bun = Bun("test bun", 100)
        self.sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)
        self.filling = Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 75)

    def test_real_ingredients_price(self):

        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)

        assert self.burger.get_price() == 325

    def test_real_ingredients_receipt(self):

        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.sauce)
        self.burger.add_ingredient(self.filling)

        receipt = self.burger.get_receipt()
        expected_receipt = (
            "(==== test bun ====)\n"
            "= sauce test sauce =\n"
            "= filling test filling =\n"
            "(==== test bun ====)\n\n"
            "Price: 325"
        )

        assert receipt == expected_receipt