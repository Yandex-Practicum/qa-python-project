import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_remove_ingredient(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_index_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self, burger, multiple_mock_ingredients):
        mock1, mock2, mock3 = multiple_mock_ingredients
        
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)
        
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock2, mock3, mock1]

    def test_move_ingredient_index_error(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)

    def test_get_price_empty_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_price_with_ingredients(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.get_price() == 400.0

    def test_get_price_no_bun(self, burger):
        with pytest.raises(AttributeError) as exc_info:
            burger.get_price()
        assert "object has no attribute" in str(exc_info.value)

    def test_receipt_structure_empty_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        assert receipt == expected_receipt

    def test_receipt_structure_with_ingredients(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        receipt = burger.get_receipt()
        
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400.0"
        )
        assert receipt == expected_receipt

    def test_receipt_includes_correct_price_for_empty_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert "Price: 200.0" in receipt

    def test_get_receipt_no_bun(self, burger):
        with pytest.raises(AttributeError) as exc_info:
            burger.get_receipt()
        assert "object has no attribute" in str(exc_info.value)

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100.0, [], 200.0),  # только булочки
        (150.0, [50.0], 350.0),  # булочки + 1 ингредиент
        (200.0, [100.0, 50.0, 75.0], 625.0),  # булочки + 3 ингредиента
    ])
    def test_get_price_parameterized(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        
        mock_ingredients = []
        for price in ingredient_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            mock_ingredients.append(mock_ing)
        
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == expected_total

    def test_ingredient_methods_called(self, burger, mock_bun, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        
        burger.get_price()
        burger.get_receipt()
        
        mock_bun.get_name.assert_called()
        mock_bun.get_price.assert_called()
        mock_ingredient_filling.get_name.assert_called()
        mock_ingredient_filling.get_price.assert_called()
        mock_ingredient_filling.get_type.assert_called()

    def test_set_buns_correctly_stores_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_increases_count(self, burger, mock_ingredient_filling):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == initial_count + 1

    def test_add_ingredient_stores_correct_ingredient(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_multiple_ingredients_stored_in_order(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients == [mock_ingredient_sauce, mock_ingredient_filling]

    def test_get_price_for_assembled_burger(self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        assert burger.get_price() == 400.0
