import sys
import os
from unittest.mock import Mock
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from burger import Burger

class TestBurger:

    def test_burger_init(self, burger):
        assert burger.bun == None
        assert burger.ingredients == []

    def test_burger_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_burger_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self, burger, mock_ingredient):
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 15.0
        mock_ingredient2.get_name.return_value = f"new{mock_ingredient.get_type().lower().capitalize()}"
        mock_ingredient2.get_type.return_value = mock_ingredient.get_type()
        
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient]

    def test_burger_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        # Expected price: (99.5 * 2) + 12.99 = 211.99
        assert burger.get_price() == 211.99

    def test_burger_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        # Expected receipt:
        ingredient_type = mock_ingredient.get_type().lower()
        ingredient_name = mock_ingredient.get_name()
        bun_name = mock_bun.get_name()
        price = burger.get_price()
        expected_receipt = f"(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n(==== testBun ====)\n\nPrice: {price}"
        assert burger.get_receipt() == expected_receipt