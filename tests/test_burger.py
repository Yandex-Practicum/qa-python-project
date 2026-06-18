from unittest.mock import Mock

import pytest

from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:

    @pytest.mark.parametrize("bun_name", ["black bun", "white bun"])
    def test_set_buns_set_black_or_white_bun(self, bun_name):
        burger = Burger()
        burger.set_buns(Bun(bun_name, 100))

        assert burger.bun.get_name() == bun_name

    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_add_ingredient_add_different_ingredient_types(self, ingredient_type):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(ingredient_type, "cutlet", 100))

        assert burger.ingredients[0].get_type() == ingredient_type

    @pytest.mark.parametrize(
        "remove_index, expected_names",
        [
            (0, ["b"]),
            (1, ["a"]),
        ],
    )
    def test_remove_ingredient_removes_by_index(self, remove_index, expected_names):
        burger = Burger()
        burger.add_ingredient(Ingredient("SAUCE", "a", 1))
        burger.add_ingredient(Ingredient("FILLING", "b", 2))

        burger.remove_ingredient(remove_index)

        assert [i.get_name() for i in burger.ingredients] == expected_names

    @pytest.mark.parametrize(
        "from_index, to_index, expected_names",
        [
            (0, 1, ["b", "a"]),
            (1, 0, ["b", "a"]),
        ],
    )
    def test_move_ingredient_reorders_list(self, from_index, to_index, expected_names):
        burger = Burger()
        burger.add_ingredient(Ingredient("SAUCE", "a", 1))
        burger.add_ingredient(Ingredient("FILLING", "b", 2))

        burger.move_ingredient(from_index, to_index)

        assert [i.get_name() for i in burger.ingredients] == expected_names

    def test_get_price_zero_bun_no_ingredients_returns_zero(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 0
        burger.bun = mock_bun

        assert burger.get_price() == 0

    def test_get_price_calls_bun_get_price_once(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 0
        burger.bun = mock_bun

        burger.get_price()

        mock_bun.get_price.assert_called_once()

    def test_get_price_doubles_bun_when_no_ingredients(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 10
        burger.bun = mock_bun

        assert burger.get_price() == 20

    def test_get_price_sums_three_ingredient_prices(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 5
        burger.bun = mock_bun
        ing1 = Mock()
        ing1.get_price.return_value = 1
        ing2 = Mock()
        ing2.get_price.return_value = 2
        ing3 = Mock()
        ing3.get_price.return_value = 3
        burger.ingredients.extend([ing1, ing2, ing3])

        assert burger.get_price() == 16

    def test_get_price_handles_float_bun_and_ingredient(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.5
        burger.bun = mock_bun
        ing = Mock()
        ing.get_price.return_value = 0.25
        burger.ingredients.append(ing)

        assert burger.get_price() == 201.25

    def test_get_receipt_no_ingredients_matches_expected_text(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 10
        burger.bun = mock_bun
        expected = (
            "(==== Test Bun ====)\n"
            "(==== Test Bun ====)\n\n"
            "Price: 20"
        )

        assert burger.get_receipt() == expected

    def test_get_receipt_one_ingredient_matches_expected_text(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 10
        burger.bun = mock_bun
        ing = Mock()
        ing.get_type.return_value = "SAUCE"
        ing.get_name.return_value = "hot"
        ing.get_price.return_value = 1
        burger.ingredients.append(ing)
        expected = (
            "(==== Test Bun ====)\n"
            "= sauce hot =\n"
            "(==== Test Bun ====)\n\n"
            "Price: 21"
        )

        assert burger.get_receipt() == expected

    def test_get_receipt_two_ingredients_matches_expected_text(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 10
        burger.bun = mock_bun
        ing_cutlet = Mock()
        ing_cutlet.get_type.return_value = "FILLING"
        ing_cutlet.get_name.return_value = "cutlet"
        ing_cutlet.get_price.return_value = 2
        ing_mayo = Mock()
        ing_mayo.get_type.return_value = "SAUCE"
        ing_mayo.get_name.return_value = "mayo"
        ing_mayo.get_price.return_value = 0.5
        burger.ingredients.extend([ing_cutlet, ing_mayo])
        expected = (
            "(==== Test Bun ====)\n"
            "= filling cutlet =\n"
            "= sauce mayo =\n"
            "(==== Test Bun ====)\n\n"
            "Price: 22.5"
        )

        assert burger.get_receipt() == expected
