import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    
    @pytest.fixture
    def burger(self):
        return Burger()
    
    @pytest.fixture
    def mock_bun(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 100.0
        bun.get_name.return_value = "hot bun"
        return bun
    
    @pytest.fixture
    def mock_ingredient_sauce(self):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 50.0
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_type.return_value = "SAUCE"
        return ingredient
    
    @pytest.fixture
    def mock_ingredient_filling(self):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 75.0
        ingredient.get_name.return_value = "cutlet"
        ingredient.get_type.return_value = "FILLING"
        return ingredient
    
    def test_set_buns_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient_success(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce
    
    def test_add_multiple_ingredients(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_sauce
        assert burger.ingredients[1] == mock_ingredient_filling
    
    def test_remove_ingredient_success(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_remove_ingredient_middle(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        ingredient3 = Mock(spec=Ingredient)
        ingredient3.get_price.return_value = 25.0
        ingredient3.get_name.return_value = "dinosaur"
        ingredient3.get_type.return_value = "FILLING"
        
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(ingredient3)
        
        burger.remove_ingredient(1)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_sauce
        assert burger.ingredients[1] == ingredient3
    
    def test_move_ingredient_success(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce
    
    def test_move_ingredient_same_position(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == mock_ingredient_sauce
    
    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        expected_price = 100.0 * 2 + 50.0 + 75.0
        assert burger.get_price() == expected_price
    
    def test_get_receipt_full_burger(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        receipt = burger.get_receipt()
        
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 325.0" in receipt
