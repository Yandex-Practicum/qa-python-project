from unittest.mock import MagicMock
import pytest
from data import DataSetPriceTesting
from praktikum.burger import Burger

class TestBurger:
    def test_set_name_bun(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, bun_mock):
        burger = Burger()
        burger.add_ingredient(bun_mock)
        assert burger.ingredients[0] == bun_mock

    def test_del_ingradient(self, ingredient_mock_1, index = 0):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        burger.remove_ingredient(index)
        assert burger.ingredients == []
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, ingredient_mock_1, ingredient_mock_2):
        burger = Burger()
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_mock_2

    @pytest.mark.parametrize("ingredient_data, result", [DataSetPriceTesting.FIRST_DATA_SET, DataSetPriceTesting.SECOND_DATA_SET])
    def test_get_price(self, bun_mock, ingredient_data, result):
        burger = Burger()
        burger.set_buns(bun_mock)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert result == burger.get_price()

    def test_get_receipt(self, bun_mock, ingredient_mock_1):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_1)
        result = f'(==== {bun_mock.get_name()} ====)\n'\
                           f'= {ingredient_mock_1.get_type().lower()} {ingredient_mock_1.get_name()} =\n'\
                           f'(==== {bun_mock.get_name()} ====)\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'
        assert burger.get_receipt() == result
