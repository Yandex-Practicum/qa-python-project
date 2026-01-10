import pytest
from unittest.mock import patch
from praktikum.burger import Burger
from data import Data


class TestBurger:
    def test_burger_object_successful(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_bun_successful(self, awesome_bun):
        burger = Burger()
        burger.set_buns(awesome_bun)
        assert burger.bun == awesome_bun

    def test_add_ingredient(self, awesome_ingredient):
        burger = Burger()
        burger.add_ingredient(awesome_ingredient)
        assert burger.ingredients == [awesome_ingredient]

    def test_remove_ingredient(self, awesome_ingredient):
        burger = Burger()
        burger.add_ingredient(awesome_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, awesome_ingredient, another_awesome_ingredient):
        burger = Burger()
        burger.add_ingredient(awesome_ingredient)
        burger.add_ingredient(another_awesome_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [another_awesome_ingredient, awesome_ingredient]

    @patch('praktikum.bun.Bun.get_price', return_value=10.50)
    @patch('praktikum.ingredient.Ingredient.get_price', return_value=20.50)
    def test_get_price(self, mock_bun_price, mock_ingredient_price, awesome_bun, awesome_ingredient):
        burger = Burger()
        burger.set_buns(awesome_bun)
        burger.add_ingredient(awesome_ingredient)
        assert burger.get_price() == 10.50 * 2 + 20.50

    @patch('praktikum.bun.Bun.get_name',
           return_value=Data.get_receipt_params.get('bun_get_name'))
    @patch('praktikum.ingredient.Ingredient.get_type',
           return_value=Data.get_receipt_params.get('ingredient_get_type'))
    @patch('praktikum.ingredient.Ingredient.get_name',
           return_value=Data.get_receipt_params.get('ingredient_get_name'))
    @patch('praktikum.burger.Burger.get_price',
           return_value=Data.get_receipt_params.get('burger_get_price'))
    @pytest.mark.parametrize('mocked_param_value',
                             [
                                 Data.get_receipt_params.get('bun_get_name'),
                                 Data.get_receipt_params.get('ingredient_get_type'),
                                 Data.get_receipt_params.get('ingredient_get_name'),
                                 Data.get_receipt_params.get('burger_get_price')
                             ]
                             )
    def test_get_receipt(self, mock_bun_get_name,
                         mock_ingredient_get_type,
                         mock_ingredient_get_name,
                         mock_burger_get_price,
                         awesome_bun,
                         awesome_ingredient,
                         mocked_param_value):
        burger = Burger()
        burger.set_buns(awesome_bun)
        burger.add_ingredient(awesome_ingredient)
        assert mocked_param_value in burger.get_receipt()
