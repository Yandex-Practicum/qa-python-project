import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_success(self):
        burger = Burger()
        mock_bun = Mock()
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock()
        
        burger.add_ingredient(mock_ingredient)
        
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.ingredients.append(mock_ingredient) 
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0

    def test_move_ingredient_success(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.extend([mock_ingredient_1, mock_ingredient_2])
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    @pytest.mark.parametrize("bun_price, ing_price, expected", [
        (100, 50, 250),    
        (200, 100, 500),  
        (0, 0, 0)          
    ])
    def test_get_price_calculates_correctly(self, bun_price, ing_price, expected):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ing_price
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected

    def test_get_receipt_returns_correct_string(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
   
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"
        )
        
        assert receipt == expected_receipt