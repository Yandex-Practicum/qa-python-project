"""
Тесты для класса Burger
"""
import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.test_data import (
    BUN_NAME, BUN_PRICE, BUN_NAME_2, BUN_PRICE_2,
    INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_NAME_2, INGREDIENT_PRICE_2,
    BURGER_TOTAL_PRICE_WITH_INGREDIENTS, BURGER_TOTAL_PRICE_WITHOUT_INGREDIENTS
)


class TestBurger:
    """Тесты для класса Burger"""

    def test_burger_creation(self):
        """Тест создания объекта бургера"""
        burger = Burger()
        
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """Тест установки булочек"""
        burger = Burger()
        bun = Bun(BUN_NAME, BUN_PRICE)
        
        burger.set_buns(bun)
        
        assert burger.bun == bun

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient1
        assert burger.ingredients[1] == ingredient2

    def test_remove_ingredient(self):
        """Тест удаления ингредиента"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(0, 1)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price_without_ingredients(self, burger_with_bun):
        """Тест расчета цены бургера без ингредиентов"""
        result = burger_with_bun.get_price()
        
        assert result == BURGER_TOTAL_PRICE_WITHOUT_INGREDIENTS

    def test_get_price_with_ingredients(self, burger_with_ingredients):
        """Тест расчета цены бургера с ингредиентами"""
        result = burger_with_ingredients.get_price()
        
        assert result == BURGER_TOTAL_PRICE_WITH_INGREDIENTS

    def test_get_receipt_without_ingredients(self, burger_with_bun):
        """Тест получения чека бургера без ингредиентов"""
        result = burger_with_bun.get_receipt()
        
        expected_lines = [
            f'(==== {BUN_NAME} ====)',
            f'(==== {BUN_NAME} ====)',
            '',
            f'Price: {BURGER_TOTAL_PRICE_WITHOUT_INGREDIENTS}'
        ]
        expected_receipt = '\n'.join(expected_lines)
        
        assert result == expected_receipt

    def test_get_receipt_with_ingredients(self, burger_with_ingredients):
        """Тест получения чека бургера с ингредиентами"""
        result = burger_with_ingredients.get_receipt()
        
        expected_lines = [
            f'(==== {BUN_NAME} ====)',
            f'= {INGREDIENT_TYPE_SAUCE.lower()} {INGREDIENT_NAME} =',
            f'= {INGREDIENT_TYPE_FILLING.lower()} {INGREDIENT_NAME_2} =',
            f'(==== {BUN_NAME} ====)',
            '',
            f'Price: {BURGER_TOTAL_PRICE_WITH_INGREDIENTS}'
        ]
        expected_receipt = '\n'.join(expected_lines)
        
        assert result == expected_receipt

    def test_burger_with_fixtures(self, burger_with_ingredients):
        """Тест бургера с использованием фикстур"""
        assert len(burger_with_ingredients.ingredients) == 2
        assert burger_with_ingredients.bun is not None
        assert burger_with_ingredients.get_price() == BURGER_TOTAL_PRICE_WITH_INGREDIENTS 