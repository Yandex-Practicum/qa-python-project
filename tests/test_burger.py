from unittest.mock import Mock
from praktikum.burger import Burger
from data import *


class TestBurger:

    def test_set_buns(self):
        mock = Mock()
        mock.get_name.return_value = BunTestData.buns[0]
        mock.get_price.return_value = BunTestData.price[0]
        burger = Burger()
        burger.set_buns(mock)
        assert burger.bun.get_name() == mock.get_name() and burger.bun.get_price() == mock.get_price()

    def test_add_ingredient(self):
        mock = Mock()
        mock.get_name.return_value = IngredientTestData.ingredients[0]
        mock.get_price.return_value = IngredientTestData.price[0]
        mock.get_type.return_value = IngredientTestData.type[0]
        burger = Burger()
        burger.add_ingredient(mock)
        assert (burger.ingredients[0].get_name() == mock.get_name() and
                burger.ingredients[0].get_price() == mock.get_price() and
                burger.ingredients[0].get_type() == mock.get_type())

    def test_remove_ingredient(self):
        mock = Mock()
        burger = Burger()
        burger.add_ingredient(mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        first_ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        burger = Burger()
        burger.add_ingredient(first_ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == second_ingredient_mock

    def test_get_price(self):
        mock = Mock()
        mock.get_price.return_value = BunTestData.price[0]
        burger = Burger()
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        assert burger.get_price() == (mock.get_price() * 3)

    def test_get_receipt(self):
        bun_mock = Mock()
        bun_mock.get_name.return_value = BunTestData.buns[0]
        bun_mock.get_price.return_value = BunTestData.price[0]
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = IngredientTestData.ingredients[0]
        ingredient_mock.get_type.return_value = IngredientTestData.type[0]
        ingredient_mock.get_price.return_value = BunTestData.price[0]
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_receipt() == BurgerTestData.receipt