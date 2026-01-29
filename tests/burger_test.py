import pytest
from unittest.mock import create_autospec
from conftest import burger, mock_bun, mock_ingredient
from praktikum.ingredient import Ingredient
from data import *


class TestBurger:
    def test_set_buns(self, burger, mock_bun, bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        ingredient1 = create_autospec(Ingredient)
        ingredient2 = create_autospec(Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    @pytest.mark.parametrize('bun_price, ingredient_prices, total_price',
                             [(0.0, [], 0.0),
                              (1255.0, [3000.0], 5510.0),
                              (1255.0, [3000.0, 15.0], 5525.0),
                              (1255.0, [3000.0, 15.0, 424.0], 5949.0)])
    def test_get_price(self, burger, mock_bun, bun_price, ingredient_prices, total_price):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredients = create_autospec(Ingredient)
            mock_ingredients.get_price.return_value = price
            burger.add_ingredient(mock_ingredients)

        expected_price = total_price
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun):
        mock_bun.get_name.return_value = bun_test["name"]
        mock_bun.get_price.return_value = bun_test["price"]
        burger.set_buns(mock_bun)
        ingredient1 = create_autospec(Ingredient)
        ingredient1.get_price.return_value = ingredient1_test["price"]
        ingredient1.get_name.return_value = ingredient1_test["name"]
        ingredient1.get_type.return_value = ingredient1_test["type"]
        ingredient2 = create_autospec(Ingredient)
        ingredient2.get_price.return_value = ingredient2_test["price"]
        ingredient2.get_name.return_value = ingredient2_test["name"]
        ingredient2.get_type.return_value = ingredient2_test["type"]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = '(==== Краторная булка ====)\n= filling Говяжий метеорит (отбивная) =\n= sauce Соус традиционный галактический =\n(==== Краторная булка ====)\n\nPrice: 5525.0'
        assert burger.get_receipt() == expected_receipt
