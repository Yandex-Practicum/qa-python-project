from data.bun_data import BUN_NAME
from helpers import calculate_expected_price
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING 
from data.ingredient_data import INGREDIENT_NAME_FILLING, INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE, INGREDIENT_PRICE_FILLING
import pytest

class TestBurger:
    def test_set_buns_sets_correct_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun 

    @pytest.mark.parametrize("count", [1, 2])
    def test_add_ingredient_successfully(self, burger, make_ingredient, count):
        ingredients = []
        for _ in range(count):   
            mock_ingredient = make_ingredient()
            burger.add_ingredient(mock_ingredient)
            ingredients.append(mock_ingredient)

        assert len(burger.ingredients) == count
        assert burger.ingredients == ingredients

    def test_remove_ingredient_successfully(self, burger, make_ingredient):
        burger.add_ingredient(make_ingredient())      
        burger.remove_ingredient(0)   
        assert burger.ingredients == []

    def test_move_ingredient_successfully(self, burger, make_ingredient):
        mock_ingredient1 = make_ingredient()
        mock_ingredient2 = make_ingredient()  

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)       

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    def test_get_price_returns_correct_value(self, burger, mock_bun, make_ingredient):
        mock_ingredient1 = make_ingredient(INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE, INGREDIENT_TYPE_SAUCE)  
        mock_ingredient2 = make_ingredient(INGREDIENT_NAME_FILLING, INGREDIENT_PRICE_FILLING, INGREDIENT_TYPE_FILLING)
        
        burger.set_buns(mock_bun)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2) 

        ingredient_prices = [mock_ingredient1.get_price(), mock_ingredient2.get_price()]
        expected_price = calculate_expected_price(mock_bun.get_price(), ingredient_prices)

        assert burger.get_price() == expected_price


    def test_get_receipt_format_is_correct(self, burger, mock_bun, make_ingredient):
        mock_ingredient1 = make_ingredient(INGREDIENT_NAME_SAUCE, INGREDIENT_PRICE_SAUCE, INGREDIENT_TYPE_SAUCE)
        mock_ingredient2 = make_ingredient(INGREDIENT_NAME_FILLING, INGREDIENT_PRICE_FILLING, INGREDIENT_TYPE_FILLING)

        burger.set_buns(mock_bun)

        burger.add_ingredient(mock_ingredient1)      
        burger.add_ingredient(mock_ingredient2)  

        receipt = burger.get_receipt()
        ingredient_prices = [mock_ingredient1.get_price(), mock_ingredient2.get_price()]
        
        expected_price = calculate_expected_price(mock_bun.get_price(), ingredient_prices)
        
        assert BUN_NAME in receipt
        assert INGREDIENT_NAME_SAUCE in receipt
        assert INGREDIENT_NAME_FILLING in receipt
        assert f"Price: {str(expected_price)}" in receipt
        