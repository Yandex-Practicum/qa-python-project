import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == initial_count + 1
        assert burger.ingredients[-1] == mock_ingredient

    def test_remove_ingredient(self, burger, mock_ingredient, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_filling)
        initial_count = len(burger.ingredients)
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient(self, burger, mock_ingredient, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_filling)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [100], 300),  # 100*2 + 100 = 300
        (150, [100, 50], 450),  # 150*2 + 100 + 50 = 450
        (200, [], 400),  # 200*2 + 0 = 400
    ])
    def test_get_price(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_total

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 300" in receipt

    def test_get_receipt_with_multiple_ingredients(self, burger, mock_bun, mock_ingredient, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450" in receipt