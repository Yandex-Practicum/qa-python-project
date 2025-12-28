import pytest
import data
from praktikum.burger import Burger

class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, mock_create_bun):
        burger = Burger()
        burger.set_buns(mock_create_bun)
        assert burger.bun == mock_create_bun

    def test_add_ingredient(self, mock_create_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_create_ingredient)
        assert mock_create_ingredient in burger.ingredients

    @pytest.mark.parametrize('index', data.DataIngredient.REMOVE_INDEX)
    def test_remove_ingredient(self, prepared_burger, index):
        remove_ingredient = prepared_burger.ingredients[index]
        prepared_burger.remove_ingredient(index)
        assert remove_ingredient not in prepared_burger.ingredients

    @pytest.mark.parametrize('index_1, index_2', data.DataIngredient.MOVING_INDEX)
    def test_move_ingredient(self, prepared_burger, index_1, index_2):
        movable_ingredient = prepared_burger.ingredients[index_1]
        prepared_burger.move_ingredient(index_1, index_2)
        assert prepared_burger.ingredients[index_2] == movable_ingredient

    def test_get_price(self, prepared_burger):
        expected_price = (prepared_burger.bun.get_price() * 2 +
                          sum(ingredient.get_price() for ingredient in prepared_burger.ingredients))
        assert prepared_burger.get_price() == expected_price

    def test_receipt(self, prepared_burger):
        receipt = prepared_burger.get_receipt()
        expected_receipt_lines = [f'(==== {prepared_burger.bun.get_name()} ====)',
                                  *[f'= {ingredient.get_type().lower()} {ingredient.get_name()} ='
                                    for ingredient in prepared_burger.ingredients],
                                  f'(==== {prepared_burger.bun.get_name()} ====)\n',
                                  f'Price: {prepared_burger.get_price()}']
        expected_receipt = '\n'.join(expected_receipt_lines)
        assert receipt == expected_receipt
