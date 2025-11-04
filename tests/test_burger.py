from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_kit_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_delete_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_ingredient_move(self, mock_ingredient):
        burger = Burger()
        burger.ingredients = [Mock(), mock_ingredient]
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient

    def test_get_cost(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = burger.get_price()
        actual_result = 797.0

        assert expected_result == actual_result

    def test_get_check(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = '(==== test_bun ====)\n= filling test_ingredient =\n(==== test_bun ====)\n\nPrice: 797.0'
        actual_result = burger.get_receipt()

        assert actual_result == expected_result