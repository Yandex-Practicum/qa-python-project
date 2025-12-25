import pytest


class TestBurger:

    def test_set_buns_with_mock(self, burger, mocked_bun):
        burger.set_buns(mocked_bun)

        assert burger.bun == mocked_bun

    def test_add_ingredient_with_mock(self, burger, mocked_ingredient):
        burger.add_ingredient(mocked_ingredient)

        assert mocked_ingredient in burger.ingredients

    def test_remove_ingredient_with_mock(self, burger, mocked_ingredients_list):
        for ingredient in mocked_ingredients_list:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 2

    def test_move_ingredient_with_mock(self, burger, mocked_ingredients_list):
        for ingredient in mocked_ingredients_list:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[2] == mocked_ingredients_list[0]

    def test_get_price_with_mock_bun_and_ingredients(self, burger, mocked_bun, mocked_ingredient):
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)

        assert burger.get_price() == 250

    def test_get_receipt_with_mock(self, burger, mocked_bun, mocked_ingredient):
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 250" in receipt






