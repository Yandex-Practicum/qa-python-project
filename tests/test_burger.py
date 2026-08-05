from unittest.mock import MagicMock
import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = MagicMock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = MagicMock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ing_1 = MagicMock()
        mock_ing_2 = MagicMock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing_2

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing_1 = MagicMock()
        mock_ing_2 = MagicMock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ing_2
        assert burger.ingredients[1] == mock_ing_1

    def test_get_price(self):
        burger = Burger()
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 100.0
        mock_ingredient = MagicMock()
        mock_ingredient.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250.0

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = MagicMock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        mock_ingredient = MagicMock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 250.0" in receipt