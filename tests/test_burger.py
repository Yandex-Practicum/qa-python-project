import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()
        
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_removes_from_list(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_2

    def test_move_ingredient_changes_position(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2, mock_ingredient_3]
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1, mock_ingredient_3]

    def test_get_price_calculates_correct_total_price(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ing_1 = Mock()
        mock_ing_1.get_price.return_value = 50.0
        
        mock_ing_2 = Mock()
        mock_ing_2.get_price.return_value = 30.0
        
        burger.ingredients = [mock_ing_1, mock_ing_2]
        expected_price = 280.0
        
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_string(self):
        burger = Burger()
    
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Флюоресцентная булка"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ing = Mock()
        mock_ing.get_type.return_value = "sauce"
        mock_ing.get_name.return_value = "Chili"
        mock_ing.get_price.return_value = 50.0
        burger.ingredients = [mock_ing]
        receipt = burger.get_receipt()
        
        assert "(==== Флюоресцентная булка ====)" in receipt
        assert "= sauce Chili =" in receipt
        assert "Price: 250.0" in receipt  # 100 * 2 + 50 = 250
