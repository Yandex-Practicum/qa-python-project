from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing2

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ing2, mock_ing1]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        
        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = 50.0
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = 30.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        # Расчёт: 100 * 2 + 50 + 30 = 280
        assert burger.get_price() == 280.0

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        mock_ing = Mock()
        mock_ing.get_type.return_value = "SAUCE"
        mock_ing.get_name.return_value = "hot sauce"
        mock_ing.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 250.0"
        )

        assert burger.get_receipt() == expected_receipt