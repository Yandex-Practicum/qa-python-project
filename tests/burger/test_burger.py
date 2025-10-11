import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
import data


class TestBurger():

    @pytest.mark.parametrize(
        'name, price',
        [[data.DEF_BUN_NAME, data.DEF_BUN_PRICE]]
    )
    def test_set_buns_positive_value(self, mock_bun, name, price):
        testburger = Burger()
        testburger.set_buns(mock_bun)
        assert testburger.bun.name == name and testburger.bun.price == price

    @pytest.mark.parametrize(
        'name, price, type',
        [[data.DEF_INGREDIENT_NAME, data.DEF_INGREDIENT_PRICE, data.DEF_INGREDIENT_TYPE]]
    )
    def test_add_ingredient_positive_value(self, mock_ingredient, name, price, type):
        testburger = Burger()
        testburger.add_ingredient(mock_ingredient)
        assert testburger.ingredients[0].name == name and testburger.ingredients[0]. price == price and testburger.ingredients[0].type == type

    @pytest.mark.parametrize(
        'ingr_index',
        [data.DEF_INGREDIENT_INDEX]
    )
    def test_remove_ingredient_positive_value(self, mock_ingredient, ingr_index):
        testburger = Burger()
        testburger.add_ingredient(mock_ingredient)
        testburger.remove_ingredient(ingr_index)
        print(testburger.ingredients)
        assert testburger.ingredients == []

    @pytest.mark.parametrize(
        'ingredient_index, ingredient_new_index, name, price, type',
        [[data.DEF_INGREDIENT_INDEX, 1, "sour cream", 200, "FILLING"]]
    )
    def test_move_ingredient_positive_value(self, mock_ingredient, ingredient_index, ingredient_new_index, name, price, type):
        testburger = Burger()
        testburger.add_ingredient(mock_ingredient)
        mock_new_ingredient = Mock()
        mock_new_ingredient.type = type
        mock_new_ingredient.name = name
        mock_new_ingredient.price = price
        testburger.add_ingredient(mock_new_ingredient)
        current_ingredient = testburger.ingredients[ingredient_index]
        testburger.move_ingredient(ingredient_index, ingredient_new_index)
        assert testburger.ingredients[ingredient_new_index] == current_ingredient

    @pytest.mark.parametrize(
        'bun_price, ingredient_price, result_price',
        [[data.DEF_BUN_PRICE, data.DEF_INGREDIENT_PRICE, 250]]
    )
    def test_get_price_positive(self, mock_bun, mock_ingredient, bun_price, ingredient_price, result_price):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        testburger = Burger()
        testburger.set_buns(mock_bun)
        testburger.add_ingredient(mock_ingredient)
        assert testburger.get_price() == result_price

    @pytest.mark.parametrize(
        'burger_receipt',
        [data.DEF_BURGER_RECEIPT]
    )
    def test_get_receipt_positive(self, mock_bun, mock_ingredient, burger_receipt):
        testburger = Burger()
        mock_bun.get_name.return_value = mock_bun.name
        mock_bun.get_price.return_value = mock_bun.price
        mock_ingredient.get_price.return_value = mock_ingredient.price
        mock_ingredient.get_type.return_value = mock_ingredient.type
        mock_ingredient.get_name.return_value = mock_ingredient.name
        testburger.set_buns(mock_bun)
        testburger.add_ingredient(mock_ingredient)
        assert testburger.get_receipt() == burger_receipt



