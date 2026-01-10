import pytest

from Diplom_1.praktikum.burger import Burger

from Diplom_1.data import INGREDIENT_DATA, BUN_DATA, INGREDIENT_DATA_1, EXPECTED_RECEIPT

class TestBurger:

    def test_set_buns(self, bun_mock):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        assert BUN_DATA.get('name') in burger.get_receipt()

    def test_add_ingredient(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        ingredient = ingredient_mock
        burger.add_ingredient(ingredient)
        assert INGREDIENT_DATA.get('name') in burger.get_receipt()

    def test_remove_ingredient(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        ingredient = ingredient_mock
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert INGREDIENT_DATA.get('name') not in burger.get_receipt()

    def test_move_ingredient(self, bun_mock, ingredient_mock, ingredient_mock_1):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        ingredient = ingredient_mock
        burger.add_ingredient(ingredient)
        ingredient = ingredient_mock_1
        burger.add_ingredient(ingredient)
        burger.move_ingredient(0, 1)
        receipt = burger.get_receipt()
        assert receipt.find(INGREDIENT_DATA.get('name')) > receipt.find(INGREDIENT_DATA_1.get('name'))

    def test_get_price(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        ingredient = ingredient_mock
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 700

    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun = bun_mock
        burger.set_buns(bun)
        ingredient = ingredient_mock
        burger.add_ingredient(ingredient)
        assert burger.get_receipt() == f'{EXPECTED_RECEIPT}{str(burger.get_price())}'
