#test_burger.py

import pytest
from unittest.mock import Mock
from .data import (
    get_price_test_cases, 
    get_receipt_test_cases,
    create_burger_for_price_test,
    create_burger_for_receipt_test
)


class TestBurger:
    
    def test_burger_initialization(self, empty_burger):
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []
    
    def test_set_buns(self, empty_burger, mock_bun):
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun
    
    def test_add_ingredient(self, empty_burger, mock_ingredient):
        empty_burger.add_ingredient(mock_ingredient)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == mock_ingredient
    
    
    def test_remove_ingredient(self, empty_burger):
        mock_ingredient = Mock()
        empty_burger.add_ingredient(mock_ingredient)
        empty_burger.remove_ingredient(0)
        assert len(empty_burger.ingredients) == 0
    
    def test_remove_ingredient_invalid_index(self, empty_burger):
        mock_ingredient = Mock()
        empty_burger.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            empty_burger.remove_ingredient(10)
    
    def test_move_ingredient(self, empty_burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        
        empty_burger.add_ingredient(mock_ingredient1)
        empty_burger.add_ingredient(mock_ingredient2)
        
        empty_burger.move_ingredient(0, 1)
        assert empty_burger.ingredients[0] == mock_ingredient2
        assert empty_burger.ingredients[1] == mock_ingredient1
    
    def test_move_ingredient_invalid_index(self, empty_burger):
        mock_ingredient = Mock()
        empty_burger.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            empty_burger.move_ingredient(10, 0)
    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", get_price_test_cases())
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = create_burger_for_price_test(bun_price, ingredient_prices)
        assert burger.get_price() == expected
    
    def test_get_price_no_bun(self, empty_burger):
        mock_ingredient = Mock()
        empty_burger.add_ingredient(mock_ingredient)
        with pytest.raises(AttributeError):
            empty_burger.get_price()
    
    @pytest.mark.parametrize("bun_name,bun_price,ingredients_data,expected_lines", get_receipt_test_cases())
    def test_get_receipt(self, bun_name, bun_price, ingredients_data, expected_lines):
        burger = create_burger_for_receipt_test(bun_name, bun_price, ingredients_data)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        assert len(lines) == len(expected_lines)
        assert lines == expected_lines
    
    def test_get_receipt_no_bun(self, empty_burger):
        with pytest.raises(AttributeError):
            empty_burger.get_receipt()