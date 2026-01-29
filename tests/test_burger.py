
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *
from data import TestData

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = TestData.bun_name
        burger.set_buns(mock_bun)
        assert burger.bun.name == TestData.bun_name

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = TestData.ingredient_name
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == TestData.ingredient_name

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_1.name = TestData.ingredient_name
        mock_ingredient_2 = Mock()
        mock_ingredient_2.name = TestData.ingredient_name_1
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        #проверяем что ингридиент перемещается
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = TestData.ingredient_name
        mock_ingredient_1 = Mock()
        mock_ingredient_1.name = TestData.ingredient_name_1
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == TestData.ingredient_name_1

    def test_get_receipt(self, create_mock_burger_names, create_burger_prices):
        mock_bun, mock_ingredient_1, mock_ingredient_2 = create_mock_burger_names
        mock_bun_price, mock_ingredient_1_price, mock_ingredient_2_price = create_burger_prices
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.get_price = Mock(
            return_value=mock_bun_price.get_price() + mock_ingredient_1_price.get_price() + mock_ingredient_2_price.get_price())
        expected_result = '(==== белая булочка ====)\n' \
                          '= Соус Кетчуп =\n' \
                          '= горчица салат =\n' \
                          '(==== белая булочка ====)\n' \
                          '\nPrice: 1250'
        assert burger.get_receipt() == expected_result



