import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import PRICE_TEST_DATA, RECEIPT_TEST_DATA, EXPECTED_RECEIPT_MULTIPLE, BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_TYPE, INGREDIENT_PRICE, FILLING_NAME, FILLING_TYPE, FILLING_PRICE


class TestBurger:
    
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock
    
    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock
    
    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_move_ingredient(self, ingredient_mock, filling_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(filling_mock)
        
        assert burger.ingredients[0] == ingredient_mock
        assert burger.ingredients[1] == filling_mock
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == filling_mock
        assert burger.ingredients[1] == ingredient_mock
    
    def test_get_price_with_only_bun(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        price = burger.get_price()
        
        bun_mock.get_price.assert_called_once()
        assert price == 200  # BUN_PRICE * 2 = 100 * 2 = 200
    
    def test_get_price_with_bun_and_ingredients(self, bun_mock, ingredient_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(filling_mock)
        
        price = burger.get_price()
        assert price == 450  # (BUN_PRICE * 2) + INGREDIENT_PRICE + FILLING_PRICE = 200 + 50 + 200 = 450
    
    @pytest.mark.parametrize("bun_name,ingredient_name,ingredient_type,expected_price", PRICE_TEST_DATA)
    def test_get_price_parametrized(self, bun_name, ingredient_name, ingredient_type, expected_price):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 50 if ingredient_type == INGREDIENT_TYPE_SAUCE else 200
        
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        price = burger.get_price()
        assert price == expected_price
    
    @pytest.mark.parametrize("bun_name,ingredient_name,ingredient_type,expected_receipt", RECEIPT_TEST_DATA)
    def test_get_receipt(self, bun_name, ingredient_name, ingredient_type, expected_receipt):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = bun_name
        bun_mock.get_price.return_value = 100
        
        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = ingredient_type
        ingredient_mock.get_name.return_value = ingredient_name
        ingredient_mock.get_price.return_value = 50 if ingredient_type == INGREDIENT_TYPE_SAUCE else 200
        
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        with patch.object(burger, 'get_price') as mock_price:
            mock_price.return_value = 250 if ingredient_type == INGREDIENT_TYPE_SAUCE else 400
            receipt = burger.get_receipt()
        
        assert receipt == expected_receipt
    
    def test_get_receipt_with_multiple_ingredients(self, bun_mock, ingredient_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(filling_mock)
        
        with patch.object(burger, 'get_price', return_value=450):
            receipt = burger.get_receipt()
        
        assert receipt == "\n".join(EXPECTED_RECEIPT_MULTIPLE)
    
    def test_empty_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []