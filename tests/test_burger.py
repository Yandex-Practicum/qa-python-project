import pytest
from unittest.mock import Mock, MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    # Тесты для класса Burger
    
    def setup_method(self):
        #Создание тестового бургера перед каждым тестом
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "black bun"
        self.mock_bun.get_price.return_value = 100
        
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.mock_ingredient1.get_name.return_value = "hot sauce"
        self.mock_ingredient1.get_price.return_value = 100
        
        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        self.mock_ingredient2.get_name.return_value = "cutlet"
        self.mock_ingredient2.get_price.return_value = 200
    
    def test_set_buns_sets_bun_correctly(self):
        # Проверка: установка булочки
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun
    
    def test_add_ingredient_adds_ingredient_to_list(self):
        # Проверка: добавление ингредиента в бургер
        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1
    
    def test_remove_ingredient_removes_ingredient_by_index(self):
        # Проверка: удаление ингредиента по индексу
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient2
    
    def test_remove_ingredient_with_invalid_index_raises_error(self):
        # Проверка: удаление по несуществующему индексу вызывает ошибку
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(0)
    
    def test_move_ingredient_moves_ingredient_to_new_position(self):
        """Проверка: перемещение ингредиента на новую позицию"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient1)
        
        self.burger.move_ingredient(2, 0)
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert len(self.burger.ingredients) == 3
    
    def test_get_price_returns_correct_total_price(self):
        # Проверка: расчёт общей стоимости бургера
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # price 100
        self.burger.add_ingredient(self.mock_ingredient2)  # price 200
        
        # Булочка * 2 (200) + ингредиенты (100 + 200) = 500
        assert self.burger.get_price() == 500
    
    def test_get_price_without_bun_raises_error(self):
        # Проверка: расчёт цены без установленной булочки вызывает ошибку
        with pytest.raises(AttributeError):
            self.burger.get_price()
    
    def test_get_receipt_returns_correct_format(self):
        # Проверка: формирование чека бургера
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        
        receipt = self.burger.get_receipt()
        
        assert f"(==== {self.mock_bun.get_name()} ====)" in receipt
        assert f"= {self.mock_ingredient1.get_type().lower()} {self.mock_ingredient1.get_name()} =" in receipt
        assert f"Price: {self.burger.get_price()}" in receipt
    
    def test_add_multiple_ingredients_orders_correctly(self):
        # Проверка: добавление нескольких ингредиентов сохраняет порядок
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient1)
        
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient2
        assert self.burger.ingredients[2] == self.mock_ingredient1
    
    def test_move_ingredient_to_same_position_does_nothing(self):
        # Проверка: перемещение ингредиента на ту же позицию ничего не меняет
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        original_ingredients = self.burger.ingredients.copy()
        self.burger.move_ingredient(0, 0)
        
        assert self.burger.ingredients[0] == original_ingredients[0]
        assert self.burger.ingredients[1] == original_ingredients[1]
        