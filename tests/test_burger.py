from unittest.mock import Mock
import pytest


class TestBurger:

    def test_set_buns_successfully(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun == bun


    def test_add_ingredient_successfully(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        

    def test_remove_ingredient_successfully(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients


    def test_move_ingredient_changes_ingredients_order(self, burger):
        first_ingredient = Mock()
        second_ingredient = Mock()

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second_ingredient, first_ingredient]


    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100, [], 200),
            (100, [50], 250),
            (100, [50, 80], 330),
        ]
    )


    def test_get_price_returns_correct_price(
        self, burger, bun_price, ingredient_prices, expected_price
    ):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price


    def test_get_receipt_returns_correct_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected_receipt = (
            "(==== test bun ====)\n"
            f"= {ingredient.get_type().lower()} test ingredient =\n"
            "(==== test bun ====)\n"
            "\n"
            "Price: 250"
        )

        assert burger.get_receipt() == expected_receipt