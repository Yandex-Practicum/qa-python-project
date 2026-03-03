from unittest.mock import Mock 
from unittest.mock import patch
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import Credentials

class TestGetPrice:
        
    '''Проверяется метод получения цены на бургер
    def get_price(self) -> float:
        price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price
    ''' 
    
    @pytest.mark.parametrize("bun_price, ingredient_price, expected_price", [
        (100, 100, 300),
        (200, 200, 600),
        (300, 300, 900)
    ])
       
    def test_get_price(self, bun_price, ingredient_price, expected_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()

        assert price == expected_price, \
            f"Ожидалась цена {expected_price}, но получена {price}"

    #несколько ингредиентов
    @pytest.mark.parametrize("bun_price, ingredient_price, expected_price", [
        (100, [100, 100], 400),
        (200, [200, 100], 700),
        (300, [300, 200, 100], 1200)
    ])
    def test_get_price_param(self, bun_price, ingredient_price, expected_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ing_price in ingredient_price:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = ing_price
            burger.add_ingredient(mock_ingredient)
        
        price = burger.get_price()

        assert price == expected_price, \
            f"Ожидалась цена {expected_price}, но получена {price}"
