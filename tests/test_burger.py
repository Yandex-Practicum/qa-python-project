import pytest
from data import BUN_NAME, BUN_PRICE, SAUCE_PRICE, SAUCE_NAME, FILLING_NAME, FILLING_PRICE
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient



class TestBurger:
    def test_set_buns(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun.get_name() == BUN_NAME and burger.bun.get_price() == BUN_PRICE

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price",
                             [
                                 ('Соус', SAUCE_NAME, SAUCE_PRICE),
                                 ('Начинка', FILLING_NAME, FILLING_PRICE)
                              ]
                             )
    def test_add_ingredient(self, mock_bun, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0].get_name() == ingredient_name and burger.ingredients[0].get_price() == ingredient_price

    def test_remove_ingredient(self, some_ingredients):
        burger = some_ingredients
        burger.remove_ingredient(1)

        assert burger.ingredients[0].get_name() == SAUCE_NAME

    def test_move_ingredient(self, some_ingredients):
        burger = some_ingredients
        burger.move_ingredient(0,1)

        assert burger.ingredients[0].get_name() == FILLING_NAME

    def test_get_price(self,mock_bun, some_ingredients):
        burger = some_ingredients
        expected_price = mock_bun.get_price() * 2 + SAUCE_PRICE + FILLING_PRICE

        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun,some_ingredients):
        expected_receipt = (
            f'(==== {BUN_NAME} ====)\n'
            f'= соус {SAUCE_NAME} =\n'
            f'= начинка {FILLING_NAME} =\n'
            f'(==== {BUN_NAME} ====)\n'
            f'Price: {mock_bun.get_price() * 2 + SAUCE_PRICE + FILLING_PRICE}'
        )
        receipt = some_ingredients.get_receipt()
        assert receipt == expected_receipt

