import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    
    def test_new_burger_has_no_bun(self):
        burger = Burger()
        
        assert burger.bun is None
    
    def test_new_burger_has_empty_ingredients_list(self):
        burger = Burger()
        
        assert burger.ingredients == []
    
    def test_set_buns_sets_bun_correctly(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun
    
    def test_add_ingredient_adds_one_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_add_ingredient_adds_multiple_ingredients_in_order(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient2
    
    def test_remove_ingredient_removes_specified_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2
    
    def test_move_ingredient_moves_ingredient_to_new_position(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1
    
    def test_remove_nonexistent_ingredient_raises_index_error(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)
    
    def test_move_nonexistent_ingredient_raises_index_error(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)
    
    @pytest.mark.parametrize("bun_price,ingredient1_price,ingredient2_price,expected_total", [
        (100.0, 50.0, 80.0, 330.0),    
        (200.0, 100.0, 150.0, 650.0),  
        (0.0, 0.0, 0.0, 0.0),          
        (50.0, 10.0, 0.0, 110.0)       
    ])
    def test_get_price_calculates_correct_total(self, bun_price, ingredient1_price, ingredient2_price, expected_total):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = ingredient1_price
        burger.add_ingredient(mock_ingredient1)
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = ingredient2_price
        burger.add_ingredient(mock_ingredient2)
        
        total_price = burger.get_price()
        
        assert total_price == expected_total
    
    def test_get_price_without_bun_raises_attribute_error(self):
        burger = Burger()
        
        with pytest.raises(AttributeError):
            burger.get_price()
    
    def test_get_receipt_includes_bun_name(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
    
    def test_get_receipt_includes_ingredient_details(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "= sauce hot sauce =" in receipt
    
    def test_get_receipt_includes_total_price(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "Price: 300.0" in receipt
    
    def test_get_receipt_for_burger_without_ingredients(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200.0
        burger.set_buns(mock_bun)
        
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        assert len(lines) == 4, f"Некорректное количество строк: {len(lines)}"
        assert lines[0] == "(==== white bun ====)"
        assert lines[1] == "(==== white bun ====)"
        assert lines[2] == ""
        assert lines[3] == "Price: 400.0"
        
        for line in lines:
            assert not line.startswith('= '), f"Найдена неожиданная строка с ингредиентом: {line}"
    
    def test_get_receipt_for_burger_with_multiple_ingredients(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 50.0
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 100.0
        
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        # Act
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        
        assert len(lines) == 6, f"Некорректное количество строк: {len(lines)}. Ожидается 6, получено {len(lines)}"
        assert lines[0] == "(==== black bun ====)"
        assert lines[1] == "= sauce hot sauce ="
        assert lines[2] == "= filling cutlet ="
        assert lines[3] == "(==== black bun ====)"
        assert lines[4] == ""
        assert lines[5] == "Price: 350.0"
    
    def test_get_receipt_ingredient_type_is_lowercase(self):
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 50.0
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "= sauce hot sauce =" in receipt
        assert "= SAUCE hot sauce =" not in receipt
    
    def test_get_receipt_empty_burger_raises_error(self):
        burger = Burger()
        
        with pytest.raises(AttributeError):
            burger.get_receipt()