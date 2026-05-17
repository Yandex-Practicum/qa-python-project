from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        first_ingredient = Mock()
        second_ingredient = Mock()
        burger.ingredients = [first_ingredient, second_ingredient]

        burger.remove_ingredient(0)

        assert burger.ingredients == [second_ingredient]

    def test_move_ingredient_moves_ingredient_to_new_index(self):
        burger = Burger()
        first_ingredient = Mock()
        second_ingredient = Mock()
        third_ingredient = Mock()
        burger.ingredients = [first_ingredient, second_ingredient, third_ingredient]

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [second_ingredient, third_ingredient, first_ingredient]

    def test_get_price_returns_sum_of_bun_and_ingredients_prices(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        ingredient_one = Mock()
        ingredient_one.get_price.return_value = 50
        ingredient_two = Mock()
        ingredient_two.get_price.return_value = 70
        burger.set_buns(bun)
        burger.ingredients = [ingredient_one, ingredient_two]

        price = burger.get_price()

        assert price == 320

    @pytest.mark.parametrize(
        "ingredient_type,ingredient_name",
        [
            ("SAUCE", "hot sauce"),
            ("FILLING", "cutlet"),
        ],
    )
    def test_get_receipt_returns_correct_receipt(self, ingredient_type, ingredient_name):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_price.return_value = 50
        burger.set_buns(bun)
        burger.ingredients = [ingredient]

        receipt = burger.get_receipt()

        assert (
            receipt
            == "(==== black bun ====)\n"
            f"= {ingredient_type.lower()} {ingredient_name} =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )
