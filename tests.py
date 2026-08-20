import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_initialization(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_to_burger(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_from_burger(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_3
        assert burger.ingredients[2] == ingredient_1

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        result = burger.get_price()
        assert result == 250.0

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.get_price = Mock(return_value=300.0)

        expected = (
            "(==== green bun ====)\n"
            "= sauce space sauce =\n"
            "(==== green bun ====)\n\n"
            "Price: 300.0"
        )
        assert burger.get_receipt() == expected