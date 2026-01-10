from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from tests.mocks import Mocks


class TestBurger:


    def test_set_bun_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        assert burger.get_price() == 4


    def test_add_ingredient_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient)
        assert burger.get_price() == 34

    def test_remove_ingredient_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.get_price() == 4

    def test_move_ingredient_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient)
        burger.add_ingredient(Mocks.mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == Mocks.mock_ingredient

    def test_get_price_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient)  # Сыр
        burger.add_ingredient(Mocks.mock_sauce)  # BBQ

        expected_price = 4 + 30 + 4
        assert burger.get_price() == expected_price

    def test_get_receipt_for_burger(self):
        burger = Burger()
        burger.set_buns(Mocks.mock_bun)
        burger.add_ingredient(Mocks.mock_ingredient)
        burger.add_ingredient(Mocks.mock_sauce)

        receipt = burger.get_receipt()

        assert "Булочка с кунжутом" in receipt
        assert "Сыр" in receipt
        assert "BBQ" in receipt
        assert "Price: 38" in receipt