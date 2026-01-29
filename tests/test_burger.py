import pytest

from helper import BurgerHelper
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_add_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('slise', [
        [0, 1],
        [0, 2],
        [1, 4],
    ])
    def test_add_ingredient_add_a_few_ingredients(self, mocks_ingredients, slise):
        burger = Burger()
        ingredients = BurgerHelper.add_a_few_ingredients(burger, mocks_ingredients, slise)
        assert burger.ingredients == ingredients

    def test_remove_ingredient_del_one_ingredient(self, mocks_ingredients):
        burger = Burger()
        ingredient = mocks_ingredients[0]
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_swap_two_ingredients(self, mocks_ingredients):
        burger = Burger()
        ingredient_1 = mocks_ingredients[0]
        burger.add_ingredient(ingredient_1)
        ingredient_2 = mocks_ingredients[1]
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] is ingredient_2 and burger.ingredients[1] is ingredient_1

    @pytest.mark.parametrize('quantity_of_ingredients', [1, 3, 4])
    def test_get_price_for_multiple_ingredients(self, mock_bun, mocks_ingredients, quantity_of_ingredients):
        burger = Burger()
        bun = mock_bun
        burger.set_buns(bun)
        price = BurgerHelper.add_ingredients_and_give_price(burger, mocks_ingredients, quantity_of_ingredients)
        assert burger.get_price() == bun.get_price() * 2 + price

    @pytest.mark.parametrize('quantity_of_ingredients', [1, 3, 4])
    def test_get_receipt_check_expected_result(self, mock_bun, mocks_ingredients, quantity_of_ingredients):
        burger = Burger()
        bun = mock_bun
        burger.set_buns(bun)
        part_receipt, price = BurgerHelper.add_ingredients_and_give_data(
            burger, mocks_ingredients, quantity_of_ingredients)
        expected_output = f"(==== {bun.get_name()} ====)\n" + part_receipt + \
                          f"(==== {bun.get_name()} ====)\n\n" \
                          f"Price: {bun.get_price() * 2 + price}"
        assert burger.get_receipt() == expected_output
