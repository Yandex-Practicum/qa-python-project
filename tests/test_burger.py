import pytest
from unittest.mock import Mock

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:
    def setup_method(self):
        self.burger = Burger()
    
    def test_set_buns(self):
        """Тестируем установку булочки"""
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Булочка"
        bun.get_price.return_value = 100.0
        
        self.burger.set_buns(bun)
        assert self.burger.bun == bun
    
    def test_add_ingredient(self):
        """Тестируем добавление ингредиента"""
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "Сыр"
        ingredient.get_price.return_value = 50.0
        ingredient.get_type.return_value = "FILLING"
        
        self.burger.add_ingredient(ingredient)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == ingredient
    
    @pytest.mark.parametrize("initial_ingredients_count", [1, 2, 3, 5])
    def test_remove_ingredient(self, initial_ingredients_count):
        """Тестируем удаление ингредиента"""
        # Добавляем несколько ингредиентов
        for i in range(initial_ingredients_count):
            ingredient = Mock(spec=Ingredient)
            ingredient.get_name.return_value = f"Ингредиент {i}"
            ingredient.get_price.return_value = 10.0 * (i + 1)
            ingredient.get_type.return_value = "FILLING"
            self.burger.add_ingredient(ingredient)
        
        # Удаляем ингредиент по индексу 0
        self.burger.remove_ingredient(0)
        
        # Проверяем, что количество ингредиентов уменьшилось на 1
        assert len(self.burger.ingredients) == initial_ingredients_count - 1
    
    @pytest.mark.parametrize("initial_index,new_index", [(0, 1), (1, 0), (0, 2), (2, 0)])
    def test_move_ingredient(self, initial_index, new_index):
        """Тестируем перемещение ингредиента"""
        # Добавляем 3 ингредиента
        ingredients = []
        for i in range(3):
            ingredient = Mock(spec=Ingredient)
            ingredient.get_name.return_value = f"Ингредиент {i}"
            ingredient.get_price.return_value = 10.0 * (i + 1)
            ingredient.get_type.return_value = "FILLING"
            self.burger.add_ingredient(ingredient)
            ingredients.append(ingredient)
        
        # Запоминаем ингредиент, который будем перемещать
        moved_ingredient = ingredients[initial_index]
        
        # Перемещаем ингредиент
        self.burger.move_ingredient(initial_index, new_index)
        
        # Проверяем, что ингредиент находится на новой позиции
        assert self.burger.ingredients[new_index] == moved_ingredient
    
    def test_get_price_with_bun_only(self):
        """Тестируем расчет цены только с булочкой"""
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 100.0
        
        self.burger.set_buns(bun)
        price = self.burger.get_price()
        
        # Цена должна быть равна удвоенной цене булочки
        assert price == 200.0
    
    def test_get_price_with_bun_and_ingredients(self):
        """Тестируем расчет цены с булочкой и ингредиентами"""
        # Устанавливаем булочку
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 100.0
        self.burger.set_buns(bun)
        
        # Добавляем ингредиенты
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 50.0
        
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 30.0
        
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        
        price = self.burger.get_price()
        
        # Цена должна быть равна: 100*2 + 50 + 30 = 280
        assert price == 280.0
    
    @pytest.mark.parametrize("bun_name", ["Булочка", "Ржаная булочка", "Булочка с кунжутом"])
    def test_get_receipt_returns_correct_format(self, bun_name):
        """Тестируем формирование чека"""
        # Устанавливаем булочку
        bun = Mock(spec=Bun)
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = 100.0
        self.burger.set_buns(bun)
        
        # Добавляем ингредиенты
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_name.return_value = "Сыр"
        ingredient1.get_price.return_value = 50.0
        ingredient1.get_type.return_value = "FILLING"
        
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = "Соус"
        ingredient2.get_price.return_value = 30.0
        ingredient2.get_type.return_value = "SAUCE"
        
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        
        receipt = self.burger.get_receipt()
        
        # Проверяем, что чек содержит правильные строки
        assert f"(==== {bun_name} ====)" in receipt
        assert "= filling Сыр =" in receipt
        assert "= sauce Соус =" in receipt
        assert "Price: 280.0" in receipt