from burger import Burger
from unittest.mock import Mock

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
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingred_1 = Mock()
        ingred_2 = Mock()
        burger.add_ingredient(ingred_1)
        burger.add_ingredient(ingred_2)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == ingred_2
        assert burger.ingredients[1] == ingred_1

    def test_get_price(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Black Bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Cutlet"
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_type.return_value = "FILLING"
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
    
        assert "Black Bun" in receipt
        assert "Cutlet" in receipt
        assert "Price: 250" in receipt