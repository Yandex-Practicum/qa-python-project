import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    def test_burger_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and mock_filling in burger.ingredients

    @pytest.mark.parametrize(
        "ingredients, indices, expected_order", [
            (
            [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING], (1, 0), [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]),
            ([INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE], (0, 1), [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]), ], )
    def test_burger_move_ingredient(self, mock_sauce, mock_filling, ingredients, indices, expected_order):
        burger = Burger()
        ingredient_map = {INGREDIENT_TYPE_SAUCE: mock_sauce, INGREDIENT_TYPE_FILLING: mock_filling, }
        for ingredient_type in ingredients:
            burger.add_ingredient(ingredient_map[ingredient_type])
        burger.move_ingredient(*indices)
        actual_order = [mock.get_type() for mock in burger.ingredients]
        assert actual_order == expected_order

    def test_burger_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = (200 * 2) + 100 + 100
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_receipt = "(==== bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== bun ====)\n\nPrice: 600"
        assert burger.get_receipt() == expected_receipt
