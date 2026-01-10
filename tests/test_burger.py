import pytest

class TestBurger:
    def test_set_bun(self, bun, burger_with_bun):
        assert burger_with_bun.bun == bun

    def test_add_ingredient(self, burger_with_bun, ingredient):
        burger_with_bun.add_ingredient(ingredient)
        assert len(burger_with_bun.ingredients) == 1
        assert burger_with_bun.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger_with_bun, ingredient):
        burger_with_bun.add_ingredient(ingredient)
        burger_with_bun.remove_ingredient(0)
        assert len(burger_with_bun.ingredients) == 0

    def test_move_ingredient(self, burger_with_bun, ingredient, ingredient_2):
        burger_with_bun.add_ingredient(ingredient)
        burger_with_bun.add_ingredient(ingredient_2)
        burger_with_bun.move_ingredient(0,1)

        assert burger_with_bun.ingredients[0] == ingredient_2
        assert burger_with_bun.ingredients[1] == ingredient

    def test_get_price(self, burger_with_bun, ingredient):
        burger_with_bun.add_ingredient(ingredient)
        expected_price = burger_with_bun.bun.get_price() * 2 + ingredient.get_price()
        actual_price = burger_with_bun.get_price()
        assert actual_price == expected_price

    def test_get_receipt(self, burger_with_bun, ingredient):
        burger_with_bun.add_ingredient(ingredient)

        bun_name = burger_with_bun.bun.get_name()
        ingredient_name = ingredient.get_name()
        ingredient_type = ingredient.get_type()
        total_price = burger_with_bun.get_price()

        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"= {ingredient_type} {ingredient_name} =\n"
            f"(==== {bun_name} ====)\n"
            f"\nPrice: {total_price}"
        )

        actual_receipt = burger_with_bun.get_receipt()
        assert actual_receipt == expected_receipt