import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import TestData


class TestBurger:
    @pytest.mark.parametrize("ingredient_amount", [1, 2, 3])
    def test_add_ingredient(self, ingredient_amount):
        burger = Burger()
        bun_mock = Mock()
        ingredient_mock = Mock()
        burger.set_buns(bun_mock)
        for i in range(ingredient_amount):
            burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == ingredient_amount

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] is ingredient_mock_1
        assert burger.ingredients[0] is ingredient_mock_2

    def test_get_price(self):
        bun_mock = Mock()
        ingredient_mock = Mock()
        burger = Burger()
        bun_mock.get_price.return_value = TestData.bun_price
        ingredient_mock.get_price.return_value = TestData.ingredient_price
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 2 * TestData.bun_price + TestData.ingredient_price

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_name.return_value = TestData.bun_name
        bun_mock.get_price.return_value = TestData.bun_price
        ingredient_mock.get_type.return_value = TestData.ingredient_type
        ingredient_mock.get_name.return_value = TestData.ingredient_name
        ingredient_mock.get_price.return_value = TestData.ingredient_price
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = burger.get_receipt()
        assert TestData.bun_name in receipt
        assert f'{str(TestData.ingredient_type).lower()} {TestData.ingredient_name}' in receipt
        assert f'{'Price:'} {TestData.bun_price * 2 + TestData.ingredient_price}' in receipt
