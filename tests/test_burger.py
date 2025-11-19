import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import *
from helpers import *


class TestBurger:

    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_set_buns(self, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price

        burger = Burger()
        burger.set_buns(bun=mock_bun)
        assert burger.bun.name == bun_name, f"Ожидаемая булка: {bun_name}, получена булка: {burger.bun.name}"
        assert burger.bun.price == bun_price, f"Ожидаемая цена: {bun_price}, получена цена: {burger.bun.price}"

    def test_add_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_burger_add_ingredient_in_burger(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        ingredient = Mock()
        ingredient.type = ingredient_type
        ingredient.name = ingredient_name
        ingredient.price = ingredient_price
        burger.add_ingredient(ingredient)
        added_ingredient_sauce = [burger.ingredients[0].type, burger.ingredients[0].name, burger.ingredients[0].price]
        expected_value = [ingredient_type, ingredient_name, ingredient_price]
        TestTools.check_unit_test_result(expected_value, actually_value=added_ingredient_sauce)

    def test_burger_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient=mock_ingredient)
        burger.remove_ingredient(index=0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_and_swap_them_by_index(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    @pytest.mark.parametrize("bun_price, ingredient_price, expected_value",[(500, 300, 1300), (800, 400, 2000), (1200, 600, 3000)])
    def test_get_price_burger(self, mock_bun, mock_ingredient, bun_price, ingredient_price, expected_value):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)
        TestTools.check_unit_test_result(expected_value=expected_value, actually_value=burger.get_price())

    def test_get_receipt(self, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = mock_bun.name
        mock_bun.get_price.return_value = mock_bun.price
        mock_ingredient.get_type.return_value = mock_ingredient.type
        mock_ingredient.get_name.return_value = mock_ingredient.name
        mock_ingredient.get_price.return_value = mock_ingredient.price
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            f'(==== {mock_bun.name} ====)\n'
            f'= {mock_ingredient.type.lower()} {mock_ingredient.name} =\n'
            f'(==== {mock_bun.name} ====)\n'
            f"\n"
            f'Price: {burger.get_price()}'
        )
        assert receipt == expected_receipt
