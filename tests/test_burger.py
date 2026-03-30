# tests/test_burger.py

import test_data as td
from burger import Burger

class TestBurger:
    def test_set_buns_success(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_success(self, burger, mock_ingredients):
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_success(self, burger, mock_ingredients):
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients[1]
    
    # ... и все остальные тесты, которые были в этом файле ...
    def test_get_price_success(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        assert burger.get_price() == td.EXPECTED_PRICE

    def test_get_receipt_success(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        expected_receipt = (
            f"(==== {td.BUN_NAME} ====)\n"
            f"= {td.INGREDIENT_SAUCE_TYPE.lower()} {td.INGREDIENT_SAUCE_NAME} =\n"
            f"= {td.INGREDIENT_FILLING_TYPE.lower()} {td.INGREDIENT_FILLING_NAME} =\n"
            f"(==== {td.BUN_NAME} ====)\n"
            f"\nPrice: {td.EXPECTED_PRICE}"
        )
        assert burger.get_receipt() == expected_receipt
