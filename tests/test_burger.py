import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()

        ing1 = Mock()
        ing2 = Mock()

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_total",
        [
            (100, [50, 70], 320),
            (200, [], 400),
            (50, [25, 25, 50], 200)
        ]
    )
    def test_get_price(self, bun_price, ing_prices, expected_total):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ing_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250"
        )

        assert receipt == expected_receipt