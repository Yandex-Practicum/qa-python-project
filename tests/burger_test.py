import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_removes_from_list(self):
        # Arrange: создаем бургер и добавляем один ингредиент
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        
        # Act: удаляем этот ингредиент по индексу 0
        burger.remove_ingredient(0)
        
        # Assert: проверяем, что список ингредиентов теперь пуст
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_order_in_list(self):
        # Arrange: добавляем два разных мока ингредиентов
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        # Act: перемещаем элемент с индекса 0 на индекс 1
        burger.move_ingredient(0, 1)
        
        # Assert: проверяем, что они поменялись местами
        assert burger.ingredients[0] == mock_ing_2
        assert burger.ingredients[1] == mock_ing_1

    def test_get_price_calculates_correct_total_price(self):
        # Arrange: настраиваем возвращаемые значения для методов цен через Mock
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0  # Цена булки (в бургере считается х2)
        
        mock_ing = Mock()
        mock_ing.get_price.return_value = 50.0   # Цена ингредиента
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)
        
        # Act: вызываем расчет стоимости
        actual_price = burger.get_price()
        
        # Assert: Формула цены: (100 * 2) + 50 = 250
        assert actual_price == 250.0

    def test_get_receipt_returns_formatted_string(self):
        # Arrange: настраиваем имена и цены для булочки и ингредиентов
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        
        mock_ing = Mock()
        mock_ing.get_type.return_value = "SAUCE"
        mock_ing.get_name.return_value = "chili"
        mock_ing.get_price.return_value = 50.0
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)
        
        # Act: генерируем чек
        receipt = burger.get_receipt()
        
        # Assert: проверяем наличие ключевых слов в строке чека
        assert "black bun" in receipt
        assert "chili" in receipt
        assert "Price: 250" in receipt
