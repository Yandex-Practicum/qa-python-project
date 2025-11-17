import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:
    
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2
    
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient3, mock_ingredient1]
    
    def test_get_price_calculation(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 75
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        expected_price = 100 * 2 + 50 + 75
        assert burger.get_price() == expected_price
    
    def test_get_receipt_format(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100  
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = "SAUCE"
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 50  
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_name.return_value = "cutlet" 
        mock_filling.get_price.return_value = 75  
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 325" in receipt  
    
    def test_remove_ingredient_invalid_index_raises_error(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)
    
    def test_move_ingredient_invalid_index_raises_error(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)
    
    def test_get_price_without_bun_raises_error(self):
        burger = Burger()

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(AttributeError):
            burger.get_price()