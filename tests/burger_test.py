import pytest


class TestBurger:

    def test_set_buns(self, burger_with_bun, bun_mock):
        assert burger_with_bun.bun == bun_mock

    def test_add_ingredient(self, burger_with_one_ingredient, ingredient_mock):
        assert burger_with_one_ingredient.ingredients == [ingredient_mock]

    def test_remove_ingredient(self, burger_with_two_ingredients):
        burger_with_two_ingredients.remove_ingredient(0)

        assert len(burger_with_two_ingredients.ingredients) == 1

    def test_move_ingredient(self, burger_with_two_ingredients, ingredient_mock):
        burger_with_two_ingredients.move_ingredient(0, 1)

        assert burger_with_two_ingredients.ingredients[1] == ingredient_mock

    @pytest.mark.parametrize(
        "burger_for_price, expected",
        [
            ([], 200),
            ([50], 250),
            ([50, 150], 400),
        ],
        indirect=["burger_for_price"],
    )
    def test_get_price(self, burger_for_price, expected):
        assert burger_for_price.get_price() == expected

    def test_get_receipt(self, burger_with_one_ingredient):
        receipt = burger_with_one_ingredient.get_receipt()

        assert "test bun" in receipt
        assert "ketchup" in receipt
        assert "Price: 250" in receipt
