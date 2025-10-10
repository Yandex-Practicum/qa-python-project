import pytest
from tests.conftest import TEST_BUNS


class TestBurger:
    def test_burger_constructor(self, create_burger):
        assert create_burger.bun is None and create_burger.ingredients == []

    def test_set_bun(self, create_burger, create_bun):
        create_burger.set_buns(create_bun)
        assert create_burger.bun == create_bun

    def test_add_ingredient(self, create_burger, create_random_ingredient):
        create_burger.add_ingredient(create_random_ingredient)
        assert create_burger.ingredients

    @pytest.mark.parametrize("create_burger_with_ingredients", [2, 3], indirect=True)
    def test_remove_ingredient(self, create_burger_with_ingredients):
        burger = create_burger_with_ingredients
        initial_len = len(burger.ingredients)

        index_to_remove = 0
        removed_ingredient = burger.ingredients[index_to_remove]

        burger.remove_ingredient(index_to_remove)

        assert len(burger.ingredients) == initial_len - 1 and removed_ingredient not in burger.ingredients

    @pytest.mark.parametrize("create_burger_with_ingredients", [2], indirect=True)
    def test_move_ingredient(self, create_burger_with_ingredients):
        burger = create_burger_with_ingredients
        original_ingredients = burger.ingredients.copy()
        index_to_move = 0
        new_index = index_to_move + 1
        burger.move_ingredient(index_to_move, new_index)
        expected_ingredients = original_ingredients.copy()
        expected_ingredients.insert(new_index, expected_ingredients.pop(index_to_move))
        assert burger.ingredients == expected_ingredients

    @pytest.mark.parametrize("create_burger_with_ingredients", [2], indirect=True)
    @pytest.mark.parametrize("bun", TEST_BUNS)
    def test_get_price(self, create_burger_with_ingredients, bun):
        burger = create_burger_with_ingredients
        burger.set_buns(bun)
        expected_price = bun.get_price() * 2 + sum(i.get_price() for i in burger.ingredients)
        assert burger.get_price() == pytest.approx(expected_price)

    @pytest.mark.parametrize("create_burger_with_ingredients", [2], indirect=True)
    @pytest.mark.parametrize("bun", TEST_BUNS)
    def test_get_receipt(self, create_burger_with_ingredients, bun):
        burger = create_burger_with_ingredients
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        ingredients_check = all(
            (ingredient.get_type().lower() in receipt and ingredient.get_name() in receipt)
            for ingredient in burger.ingredients
        )
        bun_check = (receipt.count(burger.bun.name) == 2 and f"==== {burger.bun.name} ====" in receipt)
        price_check = f"Price: {burger.get_price()}" in receipt
        assert ingredients_check and bun_check and price_check