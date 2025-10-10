import pytest
from unittest.mock import MagicMock
from burger import Burger
from data.test_data import BURGER_PRICE_CASES, build_expected_receipt


class TestBurger:
    def test_set_buns(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = "Large Bun"
        bun.get_price.return_value = 200.0

        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()

        ingredient = MagicMock()
        ingredient.get_name.return_value = "Tomato"
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_price.return_value = 30.0

        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()

        ingredient = MagicMock()
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()

        ingredient = MagicMock()
        other = MagicMock()

        burger.add_ingredient(ingredient)
        burger.add_ingredient(other)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient

    @pytest.mark.parametrize("ingredient_data, expected_price", BURGER_PRICE_CASES, ids=["case1", "case2"])
    def test_get_price(self, ingredient_data, expected_price):
        burger = Burger()

        # локальный мок булки
        bun = MagicMock()
        bun.get_price.return_value = 200.0
        bun.get_name.return_value = "Large Bun"
        burger.set_buns(bun)

        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = "Large Bun"
        bun.get_price.return_value = 200.0

        ingredient = MagicMock()
        ingredient.get_name.return_value = "Tomato"
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_price.return_value = 30.0

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()


        expected = build_expected_receipt(bun, ingredient, burger)
        assert receipt == expected



