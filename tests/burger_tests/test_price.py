import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurgerPrice:
    
    def setup_method(self):
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_price.return_value = 100
        
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_price.return_value = 50
        
        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_price.return_value = 150
    
    def test_get_price_with_bun_only_returns_double_bun_price(self):
        self.burger.set_buns(self.mock_bun)
        assert self.burger.get_price() == 200
    
    def test_get_price_with_bun_and_ingredients_sums_correctly(self):
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        assert self.burger.get_price() == 400
    
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (100, [50, 75], 325),
        (200, [100], 500),
        (50, [25, 25, 25], 175),
        (0, [0, 0], 0),
    ])
    def test_get_price_parametrized_returns_correct_total(self, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        
        self.burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            self.burger.add_ingredient(mock_ingredient)
        
        assert self.burger.get_price() == expected_total