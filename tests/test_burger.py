import pytest
from unittest.mock import Mock, patch

from burger import Burger
from data import MakeBurger as mb,  BurgerGetPrice as bp

class TestBurger:
    
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is not None
        assert burger.bun.name == mb.BUN_NAME
        assert burger.bun.price == mb.BUN_PRICE
    
    def test_add_ingredient_one_sause(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        
    def test_add_ingredient_two_component(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 2
        
    def test_remove_inrgedient(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
        
    def test_move_ingredient_two(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        
    def test_get_price_for_two_ingredients(self,mock_ingredient_class,mock_bun_class):
        mock_sauce = Mock()
        mock_bun = Mock()
        mock_filling = Mock()
        mock_sauce.get_price.return_value = mb.SAUSE_PRICE
        mock_bun.get_price.return_value = mb.BUN_PRICE
        mock_filling.get_price.return_value = mb.FILLING_PRICE
        burger = Burger()
        burger.ingredients(mock_sauce)
        burger.ingredients(mock_bun)
        burger.ingredients(mock_filling)
        assert burger.get_price() == bp.BUNS_SAUCE_FILLING_PRICE
        
    def test_get_receipt_with_buns_sauce_filling(self, mock_burger_get_price, mock_ingredient_class, mock_bun_class):
        mock_bun = Mock()
        mock_bun.get_name.return_value = mb.BUN_NAME
        mock_bun.get_price.return_value = mb.BUN_PRICE
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = mb.SAUCE_TYPE
        mock_sauce.get_name.return_value = mb.SAUCE_NAME
        mock_sauce.get_price.return_value = mb.SAUCE_PRICE
        mock_filling = Mock()
        mock_filling.get_type.return_value = mb.FILLING_TYPE
        mock_filling.get_name.return_value = mb.FILLING_NAME
        mock_filling.get_price.return_value = mb.FILLING_PRICE
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        print (burger.get_receipt())     
        assert burger.get_receipt() == ("(==== black bun ====)\n"
                                        "= SAUSE chili sauce =\n"
                                        "= FILLING cutlet  =\n"
                                        "(==== black bun ====)\n"
                                        "\n"
                                        "Price: 600")
        
        
        
        
        
        
        
            
        
        