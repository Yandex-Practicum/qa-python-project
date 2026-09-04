import pytest

from tests.data import (
    BURGER_BUN,
    BURGER_INGREDIENTS,
    MOVE_INGREDIENT_CASES,
    REMOVE_INGREDIENT_CASES,
)


class TestBurger:
    def test_get_price_without_ingredients_returns_double_bun_price(self, burger, bun_mock):
        burger.set_buns(bun_mock)

        assert burger.get_price() == BURGER_BUN[1] * 2
        bun_mock.get_price.assert_called_once_with()

    def test_add_ingredient_includes_ingredient_in_price(self, burger, bun_mock, ingredient_mocks):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mocks[0])

        expected_price = BURGER_BUN[1] * 2 + BURGER_INGREDIENTS[0][2]
        assert burger.get_price() == expected_price
        assert burger.ingredients == [ingredient_mocks[0]]

    def test_get_price_with_several_ingredients_returns_total(self, burger, bun_mock, ingredient_mocks):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        expected_price = BURGER_BUN[1] * 2 + sum(item[2] for item in BURGER_INGREDIENTS)
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("index, remaining_indices", REMOVE_INGREDIENT_CASES)
    def test_remove_ingredient_excludes_item_from_price(
        self, burger, bun_mock, ingredient_mocks, index, remaining_indices
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(index)

        expected_price = BURGER_BUN[1] * 2 + sum(
            BURGER_INGREDIENTS[item_index][2] for item_index in remaining_indices
        )
        assert burger.get_price() == expected_price
        assert burger.ingredients == [ingredient_mocks[item_index] for item_index in remaining_indices]

    @pytest.mark.parametrize("index, new_index, expected_order", MOVE_INGREDIENT_CASES)
    def test_move_ingredient_changes_order(
        self, burger, bun_mock, ingredient_mocks, index, new_index, expected_order
    ):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredient_mocks[item_index] for item_index in expected_order]

    def test_get_receipt_without_ingredients_returns_bun_only(self, burger, bun_mock):
        burger.set_buns(bun_mock)

        receipt = burger.get_receipt()

        expected_receipt = "\n".join(
            [
                f"(==== {BURGER_BUN[0]} ====)",
                f"(==== {BURGER_BUN[0]} ====)\n",
                f"Price: {burger.get_price()}",
            ]
        )
        assert receipt == expected_receipt

    def test_get_receipt_returns_formatted_receipt(self, burger, bun_mock, ingredient_mocks):
        burger.set_buns(bun_mock)
        for ingredient in ingredient_mocks[:2]:
            burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        expected_receipt = "\n".join(
            [
                f"(==== {BURGER_BUN[0]} ====)",
                f"= {BURGER_INGREDIENTS[0][0].lower()} {BURGER_INGREDIENTS[0][1]} =",
                f"= {BURGER_INGREDIENTS[1][0].lower()} {BURGER_INGREDIENTS[1][1]} =",
                f"(==== {BURGER_BUN[0]} ====)\n",
                f"Price: {burger.get_price()}",
            ]
        )
        assert receipt == expected_receipt
