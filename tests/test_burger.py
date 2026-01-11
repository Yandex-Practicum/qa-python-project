import pytest
from praktikum.burger import Burger

class TestBurgerModification:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient
        assert burger.ingredients[1] == mock_ingredient


class TestBurgerCalculation:
    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        expected_price = 100 * 2 + 50 + 50
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== test bun ====)\n"
            "= sauce test sauce =\n"
            "(==== test bun ====)\n"
            "\n"
            "Price: 250"
        )

        actual_receipt = burger.get_receipt()
        assert actual_receipt.rstrip() == expected_receipt.rstrip()
