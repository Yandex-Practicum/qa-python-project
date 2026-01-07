"""
Тесты для класса Burger 
Включает использование моков и параметризации
"""
import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тестирование модели бургера"""

    def test_burger_initialization(self):
        """Проверка инициализации пустого бургера"""
       
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """Проверка установки булочек в бургер"""
       
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Тестовая булочка"
        mock_bun.get_price.return_value = 100.0

       
        burger.set_buns(mock_bun)

       
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        """Проверка добавления ингредиента в бургер"""
       
        burger = Burger()
        mock_ingredient = Mock()

        
        burger.add_ingredient(mock_ingredient)

       
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        """Проверка удаления ингредиента по индексу"""
       
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

      
        burger.remove_ingredient(1)  # Удаляем второй ингредиент

       
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient3

    @pytest.mark.parametrize("index,new_index,expected_order", [
        (0, 1, [1, 0, 2]),  # Первый на место второго
        (2, 0, [2, 0, 1]),  # Третий на место первого
        (1, 2, [0, 2, 1]),  # Второй на место третьего
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        """Параметризованный тест перемещения ингредиентов"""
        
        burger = Burger()
        mock_ingredients = [Mock(), Mock(), Mock()]
        
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

       
        burger.move_ingredient(index, new_index)

        
        # Проверяем новый порядок ингредиентов
        for i, expected_idx in enumerate(expected_order):
            assert burger.ingredients[i] == mock_ingredients[expected_idx]

    def test_get_price_with_mocks(self):
        """Тест расчета цены бургера с использованием моков"""
        
        burger = Burger()
        
        # Создаем моки для булочки и ингредиентов
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        
        # Настраиваем возвращаемые значения
        mock_bun.get_price.return_value = 100.0  # Булочка стоит 100
        mock_ingredient1.get_price.return_value = 50.0  # Ингредиент 1
        mock_ingredient2.get_price.return_value = 30.0  # Ингредиент 2

       
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        total_price = burger.get_price()

        
        # Ожидаемая цена: (100 * 2) + 50 + 30 = 280
        expected_price = 280.0
        assert total_price == expected_price
        
        # Проверяем, что методы были вызваны
        assert mock_bun.get_price.call_count == 1
        assert mock_ingredient1.get_price.call_count == 1
        assert mock_ingredient2.get_price.call_count == 1

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100.0, [50.0, 30.0], 280.0),  # (100*2) + 50 + 30
        (150.0, [75.0, 45.0, 60.0], 480.0),  # (150*2) + 75 + 45 + 60
        (80.0, [], 160.0),  # Только булочки
    ])
    def test_get_price_parametrized(self, bun_price, ingredient_prices, expected_total):
        """Параметризованный тест расчета цены с разными значениями"""
       
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        
        mock_ingredients = []
        for price in ingredient_prices:
            mock_ingr = Mock()
            mock_ingr.get_price.return_value = price
            mock_ingredients.append(mock_ingr)

       
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        total_price = burger.get_price()

        
        assert total_price == expected_total

    def test_get_receipt_with_real_objects(self):
        """Тест формирования чека с реальными объектами"""
        
        burger = Burger()
        
        bun = Bun("Черная булочка", 100.0)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "горчичный соус", 50.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "котлета", 100.0)

        
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()

        
        assert "(==== Черная булочка ====)" in receipt
        assert "= sauce горчичный соус =" in receipt
        assert "= filling котлета =" in receipt
        assert "Price: 350.0" in receipt  # (100*2) + 50 + 100 = 350

    def test_get_receipt_with_mocks(self):
        """Тест формирования чека с использованием моков"""
       
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Тестовая булочка"
        mock_bun.get_price.return_value = 120.0
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = "SAUCE"
        mock_ingredient1.get_name.return_value = "кетчуп"
        mock_ingredient1.get_price.return_value = 40.0
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = "FILLING"
        mock_ingredient2.get_name.return_value = "салат"
        mock_ingredient2.get_price.return_value = 30.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        receipt = burger.get_receipt()

        
        expected_lines = [
            "(==== Тестовая булочка ====)",
            "= sauce кетчуп =",
            "= filling салат =",
            "(==== Тестовая булочка ====)",
            "Price: 310.0"  # (120*2) + 40 + 30 = 310
        ]
        
        for line in expected_lines:
            assert line in receipt

    def test_remove_ingredient_invalid_index(self):
        """Тест попытки удаления ингредиента с неверным индексом"""
        
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

       
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)  # Неверный индекс

    def test_move_ingredient_invalid_index(self):
        """Тест попытки перемещения ингредиента с неверным индексом"""
        
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)  # Неверный исходный индекс
