import pytest
from unittest.mock import Mock
from burger import Burger
from ingredient import Ingredient

class TestBurgerIngredientsManagement:
    
    def setup_method(self):
        self.burger = Burger()
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient2 = Mock(spec=Ingredient)
    
    def test_add_ingredient_increases_length(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1
    
    def test_add_ingredient_adds_correct_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        assert self.burger.ingredients[0] == self.mock_ingredient1
    
    def test_add_multiple_ingredients_increases_length(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        assert len(self.burger.ingredients) == 2
    
    def test_remove_ingredient_decreases_length(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
    
    def test_remove_ingredient_removes_correct_element(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients[0] == self.mock_ingredient2
    
    def test_remove_ingredient_invalid_index_raises_error(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(5)
    
    def test_move_ingredient_changes_position(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == self.mock_ingredient2
    
    def test_move_ingredient_places_element_at_new_index(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1] == self.mock_ingredient1
    
    def test_move_ingredient_to_same_position_keeps_first_element(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.move_ingredient(0, 0)
        assert self.burger.ingredients[0] == self.mock_ingredient1
    
    def test_move_ingredient_to_same_position_keeps_second_element(self):
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.move_ingredient(0, 0)
        assert self.burger.ingredients[1] == self.mock_ingredient2