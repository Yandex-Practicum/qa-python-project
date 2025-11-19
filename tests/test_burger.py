import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    """Тест-кейсы для класса Burger"""
    
    # 1. Тест установки булочки
    def test_set_buns_when_called_then_sets_buns_correctly(self, burger, mock_bun):
        """1. Метод set_buns() корректно устанавливает булочку"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    # 2. Тест добавления ингредиента
    def test_add_ingredient_when_called_then_increases_ingredients_count(self, burger, mock_ingredient):
        """2. Метод add_ingredient() увеличивает количество ингредиентов"""
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == initial_count + 1
    
    # 3. Тест удаления ингредиента
    def test_remove_ingredient_when_called_then_decreases_ingredients_count(self, burger, mock_ingredient):
        """3. Метод remove_ingredient() уменьшает количество ингредиентов"""
        burger.add_ingredient(mock_ingredient)
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1
    
    # 4. Тест перемещения ингредиента
    def test_move_ingredient_when_called_then_changes_order(self, burger):
        """4. Метод move_ingredient() корректно меняет порядок ингредиентов"""
        ing1 = Mock()
        ing1.get_name.return_value = "Соус"
        ing2 = Mock()
        ing2.get_name.return_value = "Начинка"
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(1, 0)
        
        assert burger.ingredients[0].get_name() == "Начинка"
    
    # 5. Тест расчета цены
    def test_get_price_when_burger_created_then_returns_correct_sum(self, burger, mock_bun, mock_ingredient):
        """5. Метод get_price() возвращает корректную сумму"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250
    
    # 6. Тест формирования чека
    def test_get_receipt_when_burger_created_then_returns_correct_format(self, burger, mock_bun, mock_ingredient):
        """6. Метод get_receipt() возвращает чек в правильном формате"""
        mock_bun.get_name.return_value = "Белая булка"
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Котлета"
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        assert "(==== Белая булка ====)" in receipt
    
    # 7. Параметризованный тест расчета цены
    @pytest.mark.parametrize("ing_count,expected_price", [
        (0, 200),
        (1, 250),
        (3, 350)
    ])
    def test_get_price_when_different_ingredients_count_then_returns_correct_sum(
        self, burger, mock_bun, mock_ingredient, ing_count, expected_price
    ):
        """7. Метод get_price() корректно считает сумму для разного количества ингредиентов"""
        burger.set_buns(mock_bun)
        for _ in range(ing_count):
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_price