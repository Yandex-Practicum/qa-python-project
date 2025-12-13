"""Тесты для класса Burger"""
import pytest
from unittest.mock import Mock
from tests.test_data import TEST_PRICE_CALCULATIONS


class TestBurger:
    """Тестовый класс для проверки класса Burger"""
    
    def test_init_creates_empty_burger(self, empty_burger):
        """Тест инициализации пустого бургера - проверяем только конструктор"""
        
        assert empty_burger.bun is None and empty_burger.ingredients == []
    
    def test_set_buns(self, empty_burger, mock_bun):
        """Тест установки булочки - проверяем только метод set_buns"""
        empty_burger.set_buns(mock_bun)
        
        assert empty_burger.bun is not None
    
    def test_add_ingredient(self, burger_with_bun, mock_ingredient_sauce):
        """Тест добавления ингредиента - проверяем только метод add_ingredient"""
        initial_count = len(burger_with_bun.ingredients)
        burger_with_bun.add_ingredient(mock_ingredient_sauce)
        
        assert len(burger_with_bun.ingredients) == initial_count + 1
    
    def test_remove_ingredient_removes_from_list(self, burger_with_ingredients):
        """Тест удаления ингредиента - проверяем только метод remove_ingredient"""
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0)
        
        assert len(burger_with_ingredients.ingredients) == initial_count - 1
    
    def test_move_ingredient_changes_order(self, burger_with_bun):
        """Тест перемещения ингредиента - проверяем только метод move_ingredient"""
        
        ingredient1 = Mock()
        ingredient1.get_name.return_value = "Ingredient 1"
        
        ingredient2 = Mock()
        ingredient2.get_name.return_value = "Ingredient 2"
        
        
        burger_with_bun.add_ingredient(ingredient1)
        burger_with_bun.add_ingredient(ingredient2)
        
        
        burger_with_bun.move_ingredient(0, 1)
        
        
        ingredient_names = [ing.get_name() for ing in burger_with_bun.ingredients]
        assert ingredient_names == ["Ingredient 2", "Ingredient 1"]
    
    def test_get_price_returns_correct_total(self, burger_with_ingredients):
        """Тест расчета цены - проверяем только метод get_price"""
        
        burger_with_ingredients.bun.get_price.return_value = 100.0
        burger_with_ingredients.ingredients[0].get_price.return_value = 50.0
        burger_with_ingredients.ingredients[1].get_price.return_value = 80.0        
       
        assert burger_with_ingredients.get_price() == 330.0
    
    def test_get_price_without_bun_raises_error(self, empty_burger):
        """Тест расчета цены без булочки"""
        
        with pytest.raises(AttributeError):
            empty_burger.get_price()
    
    def test_get_receipt_returns_formatted_string(self, burger_with_ingredients):
        """Тест формирования чека - проверяем только метод get_receipt"""
        
        burger_with_ingredients.bun.get_name.return_value = "Test Bun"
        burger_with_ingredients.ingredients[0].get_type.return_value = "SAUCE"
        burger_with_ingredients.ingredients[0].get_name.return_value = "Hot Sauce"
        burger_with_ingredients.ingredients[1].get_type.return_value = "FILLING"
        burger_with_ingredients.ingredients[1].get_name.return_value = "Cutlet"
        
        
        from unittest.mock import Mock
        burger_with_ingredients.get_price = Mock(return_value=330.0)
        
        
        receipt = burger_with_ingredients.get_receipt()
        expected_lines = [
            "(==== Test Bun ====)",
            "= sauce Hot Sauce =",
            "= filling Cutlet =",
            "(==== Test Bun ====)",
            "",
            "Price: 330.0"
        ]
        assert receipt == "\n".join(expected_lines)