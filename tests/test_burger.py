from burger import Burger
from bun import Bun
from ingredient import Ingredient
import pytest
from unittest.mock import Mock

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock1 = Mock(spec=Ingredient)
        ingredient_mock2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)
        burger.remove_ingredient(0)
        assert ingredient_mock1 not in burger.ingredients
        assert ingredient_mock2 in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_mock1 = Mock(spec=Ingredient)
        ingredient_mock2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_mock2, ingredient_mock1]

    def test_get_price(self):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 50

        ingredient_mock1 = Mock()
        ingredient_mock1.get_price.return_value = 20
        ingredient_mock2 = Mock()
        ingredient_mock2.get_price.return_value = 30

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)

        expected_price = 50 * 2 + 20 + 30  # 2 булки + ингредиенты
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_correct_format(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Тестовая булка"
        bun_mock.get_price.return_value = 100

        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Тестовый ингредиент"
        ingredient_mock.get_type.return_value = "Начинка"
        ingredient_mock.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        expected_receipt = "(==== Тестовая булка ====)\n= начинка Тестовый ингредиент =\n(==== Тестовая булка ====)\n\nPrice: 250"
        assert burger.get_receipt() == expected_receipt