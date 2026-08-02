import pytest

from unittest.mock import MagicMock
from praktikum.burger import Burger

def test_simple():
    assert True

class TestBurger:

    def test_initialization(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = MagicMock()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = MagicMock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = MagicMock()

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = MagicMock()
        ingredient2 = MagicMock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_price.return_value = 5.0

        ingredient1 = MagicMock()
        ingredient1.get_price.return_value = 2.0

        ingredient2 = MagicMock()
        ingredient2.get_price.return_value = 3.0

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        total_price = burger.get_price()

        assert total_price == 15.0  # 5 * 2 + 2 + 3

    def test_get_receipt(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = "Bun"
        bun.get_price.return_value = 5.0

        ingredient1 = MagicMock()
        ingredient1.get_name.return_value = "Ingredient 1"
        ingredient1.get_type.return_value = "SAUCE"
        ingredient1.get_price.return_value = 2.0

        ingredient2 = MagicMock()
        ingredient2.get_name.return_value = "Ingredient 2"
        ingredient2.get_type.return_value = "FILLING"
        ingredient2.get_price.return_value = 3.0

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== Bun ====)\n"
            "= sauce Ingredient 1 =\n"
            "= filling Ingredient 2 =\n"
            "(==== Bun ====)\n\n"
            "Price: 15.0"
        )

        assert receipt == expected_receipt
