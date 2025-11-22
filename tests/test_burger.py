from unittest.mock import Mock, patch
import pytest
import data
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_burger_bun_ingredient_true(self):
        burger = Burger()
        assert burger.bun is None and len(burger.ingredients) == 0

    def test_set_buns_success(self):
        bun_mock = Mock()
        bun_mock.name = "black bun"
        bun_mock.price = 100
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == "black bun"

    @pytest.mark.parametrize("types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_add_ingredient_success(self, types):
        ingredient_mock = Mock()
        ingredient_mock.type = types
        ingredient_mock.name = 'hot_one'
        ingredient_mock.price = 100
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) != 0

    def test_remove_ingredient_number_1_success(self):
        burger = Burger()
        burger.ingredients = data.list_for_del
        del_elem = burger.ingredients[1]
        burger.remove_ingredient(1)
        assert del_elem not in burger.ingredients

    def test_move_ingredient_number_1_to_0_success(self):
        burger = Burger()
        for ingredient in data.list_for_del:
            burger.ingredients.append(ingredient)
        elem_for_move = burger.ingredients[1]
        prev_elem = burger.ingredients[0]
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == elem_for_move and burger.ingredients[1] == prev_elem

    def test_get_price_with_3_ingredients_success(self):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 200
        burger = Burger()
        burger.bun = bun_mock
        for i in range(3):
            burger.ingredients.append(ingredient_mock)
        assert burger.get_price() == 800

    @pytest.mark.parametrize("types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt_success(self, mock_get_price, types):
        bun_mock = Mock()
        bun_mock.get_name.return_value = 'black'
        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = types
        ingredient_mock.get_name.return_value = "hot_one"
        burger = Burger()
        burger.bun = bun_mock
        for i in range(3):
            burger.ingredients.append(ingredient_mock)
        mock_get_price.return_value = 800
        text_receipt = burger.get_receipt()
        list_receipt = text_receipt.split('\n')
        assert ((len(list_receipt) == 7)
                and (f'(==== black ====)' == (list_receipt[0] and (list_receipt[-3]))
                and (f'= {types.lower()} hot_one =' == (list_receipt[1] and list_receipt[2] and list_receipt[3])))
                and (f'Price: 800' in list_receipt[-1]))

