from unittest.mock import Mock
import pytest
from burger import Burger

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
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.move_ingredient(0, 1)
        # Проверяем, что ингредиенты поменялись местами
        assert burger.ingredients == [mock_ing2, mock_ing1]

    def test_get_price_with_buns_and_ingredients(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100  # Цена булки 100 (х2 = 200)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50   # Цена ингредиента 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        # Ожидаемая цена: (100 * 2) + 50 = 250
        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Краторная булка"
        mock_bun.get_price.return_value = 100
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Space Sauce"
        mock_ingredient.get_price.return_value = 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "Краторная булка" in receipt
        assert "Space Sauce" in receipt
        assert "Price: 250" in receipt
