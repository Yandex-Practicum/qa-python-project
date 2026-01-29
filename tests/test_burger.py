from burger import Burger
from helpers import *


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == BUN_NAME

    def test_add_ingredients(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert type(burger.ingredients) == list and len(burger.ingredients) == 1

    def test_remove_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(SAUCE_TYPE)
        burger.add_ingredient(SAUCE_NAME)
        burger.add_ingredient(FILLING_NAME)
        burger.move_ingredient(2, 1)
        assert len(burger.ingredients) == 3 and burger.ingredients[2] == SAUCE_NAME

    def test_get_price(self, mock_bun_name_and_price, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun_name_and_price)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 300.0

    def test_get_receipt(self, mock_bun_name_and_price, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun_name_and_price)
        burger.add_ingredient(mock_ingredient)
        assert receipt() == burger.get_receipt()
