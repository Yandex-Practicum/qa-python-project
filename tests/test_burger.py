import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self, new_bun):
        burger = Burger()
        burger.set_buns(new_bun)
        assert burger.bun == new_bun

    def test_add_ingredient(self, new_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(new_ingredient_sauce)
        assert burger.ingredients == [new_ingredient_sauce]

    def test_remove_ingredient(self, new_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(new_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, new_ingredient_sauce, new_ingredient_filling):
        burger = Burger()
        sauce = new_ingredient_sauce
        filling = new_ingredient_filling
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients ==[filling, sauce]

    @pytest.mark.parametrize(
        "ingredients, expected_price", [
            ([("SAUCE", "Wetdust", 10.0), ("FILLING", "Cobaldmeat", 50.0)], 1460.0),
            ([("FILLING", "Astero", 200.0), ("SAUCE", "Liqiz", 100.0)], 1700.0)
        ]
    )
    def test_get_price(self, new_bun, ingredients, expected_price):
        burger = Burger()
        burger.set_buns(new_bun)
        for ingredient_type, name, price in ingredients:
            ingredient_mock = MagicMock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

    def test_receipt(self, new_bun, new_ingredient_filling):
        burger = Burger()
        burger.set_buns(new_bun)
        burger.add_ingredient(new_ingredient_filling)
        expected_receipt = f'(==== {new_bun.get_name()} ====)\n'\
                           f'= {str(new_ingredient_filling.get_type()).lower()} {new_ingredient_filling.get_name()} =\n'\
                           f'(==== {new_bun.get_name()} ====)\n' \
                           '\n' \
                           f'Price: {burger.get_price()}'
        assert burger.get_receipt() == expected_receipt
