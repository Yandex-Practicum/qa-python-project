import pytest
from burger import Burger
from unittest.mock import MagicMock 

class TestBurgerLogic:
    @pytest.mark.parametrize("bun_price, expected_total", [
        (50.0, 100.0),
        (100.0, 200.0),
        (0.0, 0.0)
    ])
    def test_get_price_with_buns(self, mock_bun, bun_price, expected_total):
        mock_bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        result = burger.get_price()
        assert result == expected_total

    def test_add_ingredient_and_calculate_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = 50.0
        
        ing_mock = mock_ingredient
        ing_mock.get_name.return_value = "Cheese"
        ing_mock.get_price.return_value = 30.0
        ing_mock.get_type.return_value = "filling"
        
        burger.add_ingredient(ing_mock)
        result = burger.get_price()
        assert result == 130.0

    def test_remove_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = 50.0

        ing1 = MagicMock()
        ing1.get_name.return_value = "Cheese"
        ing1.get_price.return_value = 30.0
        ing1.get_type.return_value = "filling"

        ing2 = MagicMock()
        ing2.get_name.return_value = "Tomato"
        ing2.get_price.return_value = 10.0
        ing2.get_type.return_value = "filling"

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing2
        assert burger.get_price() == 110.0