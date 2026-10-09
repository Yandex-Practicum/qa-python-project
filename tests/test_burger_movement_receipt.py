import pytest
from burger import Burger
from unittest.mock import MagicMock 

class TestBurgerMovement:
    def test_move_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = 50.0

        ing1 = MagicMock()
        ing1.get_name.return_value = "Cheese"
        ing1.get_price.return_value = 30.0
        ing1.get_type.return_value = "filling"

        ing2 = MagicMock()
        ing2.get_name.return_value = "Tomato"
        ing2.get_price.return_value = 10.0
        ing2.get_type.return_value = "filling"

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.move_ingredient(1, 0)
        
        assert burger.ingredients[0] is ing2
        assert burger.ingredients[1] is ing1
        assert burger.get_price() == 140.0

    def test_get_receipt(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_name.return_value = "Sesame Bun"
        mock_bun.get_price.return_value = 50.0

        ing_mock = MagicMock()
        ing_mock.get_name.return_value = "Cheese"
        ing_mock.get_price.return_value = 30.0
        ing_mock.get_type.return_value = "filling"
        
        burger.add_ingredient(ing_mock)
        
        receipt = burger.get_receipt()
        
        assert "(==== Sesame Bun ====" in receipt
        assert "= filling Cheese =" in receipt
        assert "Price: 130.0" in receipt
