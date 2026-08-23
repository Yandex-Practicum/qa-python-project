import pytest
from unittest.mock import MagicMock

from burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = MagicMock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = MagicMock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        first_ingredient = MagicMock()
        second_ingredient = MagicMock()

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == [second_ingredient]

    def test_move_ingredient(self):
        burger = Burger()
        first_ingredient = MagicMock()
        second_ingredient = MagicMock()
        third_ingredient = MagicMock()

        burger.ingredients = [
            first_ingredient,
            second_ingredient,
            third_ingredient
        ]

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [
            second_ingredient,
            third_ingredient,
            first_ingredient
        ]

    def test_get_price(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_price.return_value = 100

        first_ingredient = MagicMock()
        first_ingredient.get_price.return_value = 50

        second_ingredient = MagicMock()
        second_ingredient.get_price.return_value = 75

        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        assert burger.get_price() == 325

    @pytest.mark.parametrize(
        "ingredients_data, expected_receipt",
        [
            (
                [],
                "(==== black bun ====)\n"
                "(==== black bun ====)\n\n"
                "Price: 200"
            ),
            (
                [
                    ("SAUCE", "hot sauce", 100),
                    ("FILLING", "cutlet", 100)
                ],
                "(==== black bun ====)\n"
                "= sauce hot sauce =\n"
                "= filling cutlet =\n"
                "(==== black bun ====)\n\n"
                "Price: 400"
            )
        ]
    )
    def test_get_receipt(self, ingredients_data, expected_receipt):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        for ingredient_type, ingredient_name, ingredient_price in ingredients_data:
            ingredient = MagicMock()
            ingredient.get_type.return_value = ingredient_type
            ingredient.get_name.return_value = ingredient_name
            ingredient.get_price.return_value = ingredient_price

            burger.add_ingredient(ingredient)

        assert burger.get_receipt() == expected_receipt