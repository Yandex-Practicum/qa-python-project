import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    
    def test_burger_initialization(self, burger):
        """Тест проверяет, что бургер создается с пустыми ингредиентами и без булки"""
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns(self, burger, mock_bun):
        """Тест проверяет установку булки в бургер"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self, burger, mock_ingredients):
        """Тест проверяет добавление одного ингредиента в бургер"""
        burger.add_ingredient(mock_ingredients[0])
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients[0]
    
    def test_add_multiple_ingredients(self, burger, mock_ingredients):
        """Тест проверяет добавление нескольких ингредиентов в бургер"""
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == len(mock_ingredients)
        assert burger.ingredients == mock_ingredients
    
    def test_remove_ingredient(self, burger, mock_ingredients):
        """Тест проверяет удаление ингредиента из бургера"""
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredients[0]
        assert burger.ingredients[1] == mock_ingredients[2]
    
    def test_move_ingredient_forward(self, burger, mock_ingredients):
        """Тест проверяет перемещение ингредиента вперед"""
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == mock_ingredients[2]
        assert burger.ingredients[1] == mock_ingredients[0]
        assert burger.ingredients[2] == mock_ingredients[1]
    
    def test_move_ingredient_backward(self, burger, mock_ingredients):
        """Тест проверяет перемещение ингредиента назад"""
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == mock_ingredients[1]
        assert burger.ingredients[1] == mock_ingredients[2]
        assert burger.ingredients[2] == mock_ingredients[0]
    
    def test_get_price_with_bun_no_ingredients(self, burger, mock_bun):
        """Тест проверяет расчет цены бургера только с булкой"""
        burger.set_buns(mock_bun)
        price = burger.get_price()
        assert price == 200.0 
        mock_bun.get_price.assert_called_once()
    
    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredients):
        """Тест проверяет расчет цены бургера с булкой и ингредиентами"""
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        expected_price = 200.0 + 50 + 100 + 150
        assert burger.get_price() == expected_price
        
        mock_bun.get_price.assert_called_once()
        for ingredient in mock_ingredients:
            ingredient.get_price.assert_called_once()
    
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [50, 75], 100*2 + 50 + 75),
        (200, [100, 150, 200], 200*2 + 100 + 150 + 200),
        (150, [], 150*2),
        (0, [50, 50], 0*2 + 50 + 50),
    ])
    def test_get_price_parametrized(self, burger, bun_price, ingredient_prices, expected_price):
        """Параметризованный тест проверяет расчет цены с разными данными"""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = float(bun_price)
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = float(price)
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_price
    
    def test_get_price_without_bun(self, burger, mock_ingredients):
        """Тест проверяет расчет цены без булки"""
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == 50 + 100 + 150
    