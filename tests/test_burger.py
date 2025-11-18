from praktikum.burger import Burger
from data import *
from unittest.mock import Mock
import pytest


class TestBurger:
    # Проверяет, что метод set_buns корректно устанавливает булочку в бургер
    def test_set_buns_add_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверяет, что метод add_ingredient увеличивает количество ингредиентов в бургере
    def test_add_ingredient_add_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    # Проверяет, что метод add_ingredient добавляет корректный ингредиент
    def test_add_ingredient_stores_correct_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    # Проверяет, что метод remove_ingredient уменьшает количество ингредиентов в бургере
    def test_remove_ingredient_delete_success(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Проверяет, что метод move_ingredient корректно перемещает ингредиент
    def test_move_ingredient_move_success(self):
        burger = Burger()
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "ingredient1"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "ingredient2"
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ingredient2

     # Проверяет, что метод get_price вкорректно высчитывает конечную стоимость бургера
    def test_get_price_calculates_total_cost_correctly(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
    
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        actual_price = burger.get_price()
    
        assert actual_price == expected_price
    
    # Проверяет, что метод get_receipt возвращает чек в правильном формате с названиями булочки и ингредиентов
    def test_get_receipt_success(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = BunData.bun_name_for_receipt
        mock_bun.get_price.return_value = BunData.bun_price_for_receipt
    
        mock_sauce = Mock()
        mock_sauce.get_name.return_value = IngredientData.sauce_name_for_receipt
        mock_sauce.get_price.return_value = IngredientData.sauce_price_for_receipt
        mock_sauce.get_type.return_value = IngredientData.sauce_type
    
        mock_filling = Mock()
        mock_filling.get_name.return_value = IngredientData.filling_name_for_receipt
        mock_filling.get_price.return_value = IngredientData.filling_price_for_receipt
        mock_filling.get_type.return_value = IngredientData.filling_type
    
        mock_filling_2 = Mock()
        mock_filling_2.get_name.return_value = IngredientData.filling_2_name_for_receipt
        mock_filling_2.get_price.return_value = IngredientData.filling_2_price_for_receipt
        mock_filling_2.get_type.return_value = IngredientData.filling_type
    
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
    
        total_price = burger.get_price()
    
        expected_receipt = (f'(==== {BunData.bun_name_for_receipt} ====)\n'
                           f'= {IngredientData.sauce_type.lower()} {IngredientData.sauce_name_for_receipt} =\n'
                           f'= {IngredientData.filling_type.lower()} {IngredientData.filling_name_for_receipt} =\n'
                           f'= {IngredientData.filling_type.lower()} {IngredientData.filling_2_name_for_receipt} =\n'
                           f'(==== {BunData.bun_name_for_receipt} ====)\n'
                           f'\n'
                           f'Price: {total_price}')
    
        assert burger.get_receipt() == expected_receipt
