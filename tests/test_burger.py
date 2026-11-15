import pytest
import burger
import bun
import data
import ingredient
import ingredient_types
from unittest.mock import Mock


class TestBurger:

    def test_set_buns_success(self):
        test_burger = burger.Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = data.random_bun
        test_burger.set_buns(mock_bun)

        assert test_burger.bun == mock_bun

    @pytest.mark.parametrize("type_ing, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int),
        (ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_float)
    ])
    def test_add_ingredient_success(self, type_ing, name, price):
        test_burger = burger.Burger()
        test_ingredient = ingredient.Ingredient(type_ing, name, price)
        test_burger.add_ingredient(test_ingredient)

        assert test_ingredient in test_burger.ingredients

    @pytest.mark.parametrize("type_ing, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int),
        (ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_float)
    ])
    def test_remove_ingredient_success (self, type_ing, name, price):
        test_burger = burger.Burger()
        test_ingredient = ingredient.Ingredient(type_ing, name, price)

        test_burger.add_ingredient(test_ingredient)
        test_burger.remove_ingredient(0)

        assert test_ingredient not in test_burger.ingredients

    def test_move_ingredient_success (self):
        test_burger = burger.Burger()
        test_ingredient_0 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_int)
        test_ingredient_1 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_float)
        test_ingredient_2 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_int)
        test_burger.add_ingredient(test_ingredient_0)
        test_burger.add_ingredient(test_ingredient_1)
        test_burger.add_ingredient(test_ingredient_2)

        test_burger.move_ingredient(1, 2)
        assert test_burger.ingredients[2] == test_ingredient_1

    def test_get_price_success(self):
        test_burger = burger.Burger()
        test_bun = bun.Bun(data.random_bun, data.random_price_int)
        test_burger.set_buns(test_bun)

        test_ingredient_1 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_int)
        test_ingredient_2 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_float)
        test_burger.add_ingredient(test_ingredient_1)
        test_burger.add_ingredient(test_ingredient_2)

        assert test_burger.get_price() == test_ingredient_1.get_price() + test_ingredient_2.get_price() + (test_bun.get_price()*2)

    def test_get_receipt_success(self):
        test_burger = burger.Burger()
        test_bun = bun.Bun(data.random_bun, data.random_price_int)
        test_burger.set_buns(test_bun)

        test_ingredient_1 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.random_filling, data.random_price_int)
        test_ingredient_2 = ingredient.Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.random_sauce, data.random_price_float)
        test_burger.add_ingredient(test_ingredient_1)
        test_burger.add_ingredient(test_ingredient_2)

        expected_receipt = (
            f"(==== {test_bun.get_name()} ====)\n"
            f"= {test_ingredient_1.get_type().lower()} {test_ingredient_1.get_name()} =\n"
            f"= {test_ingredient_2.get_type().lower()} {test_ingredient_2.get_name()} =\n"
            f"(==== {test_bun.get_name()} ====)\n\n"
            f"Price: {(test_bun.get_price()*2) + test_ingredient_1.get_price() + test_ingredient_2.get_price()}"
        )

        assert test_burger.get_receipt() == expected_receipt



