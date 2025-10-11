import pytest
from unittest.mock import MagicMock
from ingredient import Ingredient


class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        second_ingredient = MagicMock(spec=Ingredient)
        second_ingredient.get_price.return_value = 25.0
        second_ingredient.get_name.return_value = "Tomato"
        second_ingredient.get_type.return_value = "vegetable"

        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second_ingredient
        assert burger.ingredients[1] == ingredient

    @pytest.mark.parametrize(
        "bun_price, ingredient_price, expected_total",
        [
            (50, 20, 120),
            (40, 30, 110),
            (60, 0, 120),
        ]
    )
    def test_get_price_parametrized(self, burger, bun, ingredient, bun_price, ingredient_price, expected_total):
        bun.get_price.return_value = bun_price
        ingredient.get_price.return_value = ingredient_price

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_total

    @pytest.mark.parametrize(
        "ingredient_type, ingredient_name, expected_line",
        [
            ("vegetable", "Lettuce", "= vegetable Lettuce ="),
            ("sauce", "BBQ", "= sauce BBQ ="),
            ("filling", "Bacon", "= filling Bacon ="),
        ]
    )
    def test_get_receipt_parametrized(self, burger, bun, ingredient, ingredient_type, ingredient_name, expected_line):
        bun.get_name.return_value = "White bun"
        bun.get_price.return_value = 30.0
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_price.return_value = 60.0

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"{expected_line}\n"
            f"(==== {bun.get_name()} ====)\n"
            f"Price: {burger.get_price()}"
        )

        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt
