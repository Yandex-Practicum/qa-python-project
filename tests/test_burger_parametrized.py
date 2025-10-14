import pytest
from unittest.mock import Mock


class TestBurgerParametrized:
    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50], 250),  
        (200, [80, 70], 550),  
        (150, [40, 30, 60], 430),  
    ])
    def test_get_price_parametrized(self, burger, bun_price, ingredient_prices, expected_total):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "test bun"
        bun_mock.get_price.return_value = bun_price
        
        ingredient_mocks = []
        for i, price in enumerate(ingredient_prices):
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = "SAUCE"
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_price.return_value = price
            ingredient_mocks.append(ingredient_mock)
        
        burger.set_buns(bun_mock)
        for ingredient_mock in ingredient_mocks:
            burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == expected_total