import pytest
from unittest.mock import Mock
from tests.data import TestData


class TestBurgerMoveIngredient:
    """Тесты для метода move_ingredient класса Burger"""
    
    def test_move_ingredient_success(self, burger_with_ingredients, mock_sauce, mock_filling):
        """Тест успешного перемещения ингредиента"""
        # Добавляем третий ингредиент
        ingredient_mock = Mock()
        burger_with_ingredients.add_ingredient(ingredient_mock)
        
        # Перемещаем ингредиент с позиции 0 на позицию 2
        burger_with_ingredients.move_ingredient(0, 2)
        
        assert burger_with_ingredients.ingredients[0] == mock_filling
        assert burger_with_ingredients.ingredients[1] == ingredient_mock
        assert burger_with_ingredients.ingredients[2] == mock_sauce

    def test_move_ingredient_same_position(self, burger_with_ingredients, mock_sauce):
        """Тест перемещения ингредиента на ту же позицию"""
        burger_with_ingredients.move_ingredient(0, 0)
        assert burger_with_ingredients.ingredients[0] == mock_sauce

    def test_move_ingredient_invalid_index(self, burger_with_ingredients):
        """Тест перемещения с неверным индексом"""
        with pytest.raises(IndexError):
            burger_with_ingredients.move_ingredient(5, 0)

    @pytest.mark.parametrize("index1,index2", [
        (0, 0),    # Одинаковые индексы
        (0, 1),    # Соседние индексы
    ])
    def test_move_ingredient_various_positions(self, burger_with_ingredients, mock_sauce, mock_filling, index1, index2):
        """Параметризованный тест перемещения ингредиентов в различных позициях"""
        original_order = burger_with_ingredients.ingredients.copy()
        burger_with_ingredients.move_ingredient(index1, index2)
        
        # Проверяем, что порядок изменился если индексы разные
        if index1 != index2:
            assert burger_with_ingredients.ingredients != original_order