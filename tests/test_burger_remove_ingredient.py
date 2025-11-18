import pytest
from unittest.mock import Mock
from tests.data import TestData


class TestBurgerRemoveIngredient:
    """Тесты для метода remove_ingredient класса Burger"""
    
    def test_remove_ingredient_success(self, burger_with_ingredients):
        """Тест успешного удаления ингредиента"""
        burger_with_ingredients.remove_ingredient(0)
        assert len(burger_with_ingredients.ingredients) == 1

    def test_remove_ingredient_invalid_index(self, burger_with_ingredients):
        """Тест удаления ингредиента с неверным индексом"""
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(5)

    def test_remove_ingredient_empty_list(self, sample_burger):
        """Тест удаления из пустого списка ингредиентов"""
        with pytest.raises(IndexError):
            sample_burger.remove_ingredient(0)

    def test_remove_ingredient_from_middle(self, burger_with_ingredients, mock_sauce, mock_filling):
        """Тест удаления ингредиента из середины списка"""
        # Добавляем третий ингредиент
        ingredient_mock = Mock()
        burger_with_ingredients.add_ingredient(ingredient_mock)
        
        burger_with_ingredients.remove_ingredient(1)  # Удаляем средний элемент
        
        assert len(burger_with_ingredients.ingredients) == 2
        assert burger_with_ingredients.ingredients[0] == mock_sauce
        assert burger_with_ingredients.ingredients[1] == ingredient_mock