import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_and_remove_ingredient(self, bun_mock, ingredient_sauce, ingredient_filling):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_filling]

    def test_move_ingredient(self, bun_mock, ingredient_sauce, ingredient_filling):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient_sauce

    @pytest.mark.parametrize(
        "ingredients,expected_price",
        [
            ([], 200),
            ([50], 250),
            ([150], 350),
            ([50, 150], 400),
        ],
    )
    def test_get_price(self, bun_mock, ingredients, expected_price):
        burger = Burger()
        burger.set_buns(bun_mock)
        for price in ingredients:
            ing = Mock()
            ing.get_price.return_value = price
            ing.get_name.return_value = "mock"
            ing.get_type.return_value = INGREDIENT_TYPE_FILLING
            burger.add_ingredient(ing)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun_mock, ingredient_sauce):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_sauce)
        receipt = burger.get_receipt()
        assert "test bun" in receipt
        assert "ketchup" in receipt
        assert "Price: 250" in receipt