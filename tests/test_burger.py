import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.conftest import burger, bun_mock, ingredient_mock


class TestBurger:
    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient_mock):
        burger.ingredients = [ingredient_mock]
        index_to_remove = 0
        burger.remove_ingredient(index_to_remove)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient_mock):
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()
        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_mock_2, ingredient_mock_1]

    def test_get_price(self, burger, bun_mock, ingredient_mock):
        bun_mock.get_price.return_value = 300.0
        burger.bun = bun_mock

        ingredient_mock_1 = Mock()
        ingredient_mock_1.get_price.return_value = 150.0

        ingredient_mock_2 = Mock()
        ingredient_mock_2.get_price.return_value = 200.0

        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]

        expected_price = 300.0 * 2 + 150.0 + 200.0
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun_mock):
        bun_mock.get_name.return_value = "multi-grain bun"
        bun_mock.get_price.return_value = 50
        burger.bun = bun_mock

        ingredient_mock_1 = Mock()
        ingredient_mock_1.get_type.return_value = "filling"
        ingredient_mock_1.get_name.return_value = "cutlet"
        ingredient_mock_1.get_price.return_value = 300

        ingredient_mock_2 = Mock()
        ingredient_mock_2.get_type.return_value = "sauce"
        ingredient_mock_2.get_name.return_value = "ketchup"
        ingredient_mock_2.get_price.return_value = 200

        burger.ingredients = [ingredient_mock_1, ingredient_mock_2]

        expected_receipt = "(==== multi-grain bun ====)\n= filling cutlet =\n= sauce ketchup =\n(==== multi-grain bun ====)\n\nPrice: 600"
        assert burger.get_receipt() == expected_receipt