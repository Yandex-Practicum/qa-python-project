import pytest
from unittest.mock import Mock, patch
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurgerReceipt:
    
    def setup_method(self):
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "black bun"
        
        self.mock_ingredient = Mock(spec=Ingredient)
        self.mock_ingredient.get_name.return_value = "hot sauce"
        self.mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    
    @patch('burger.Burger.get_price')
    def test_get_receipt_contains_bun_name(self, mock_get_price):
        mock_get_price.return_value = 250
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        
        receipt = self.burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
    
    @patch('burger.Burger.get_price')
    def test_get_receipt_contains_ingredient(self, mock_get_price):
        mock_get_price.return_value = 250
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        
        receipt = self.burger.get_receipt()
        
        assert "= sauce hot sauce =" in receipt
    
    @patch('burger.Burger.get_price')
    def test_get_receipt_contains_price(self, mock_get_price):
        mock_get_price.return_value = 250
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        
        receipt = self.burger.get_receipt()
        
        assert "Price: 250" in receipt
    
    def test_get_receipt_without_bun_raises_error(self):
        with pytest.raises(AttributeError):
            self.burger.get_receipt()