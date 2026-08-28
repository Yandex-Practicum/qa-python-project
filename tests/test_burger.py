from unittest.mock import Mock

import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


class TestBurger:
    def test_init_creates_burger_without_bun_and_ingredients(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_sets_bun(self, burger):
        bun = Mock(spec=Bun)

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_appends_ingredient(self, burger):
        ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize("index, expected_indexes",
        [(0, [1, 2]),(1, [0, 2]),(2, [0, 1]),],)
    def test_remove_ingredient_removes_item_by_index(
        self, burger, index, expected_indexes):
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        burger.ingredients = ingredients.copy()

        burger.remove_ingredient(index)

        assert burger.ingredients == [ingredients[i] for i in expected_indexes]

    @pytest.mark.parametrize("index, new_index, expected_indexes",
        [(0, 2, [1, 2, 0]),(2, 0, [2, 0, 1]),(1, 1, [0, 1, 2]),],)
    def test_move_ingredient_moves_item_to_new_index(
        self, burger, index, new_index, expected_indexes):
        ingredients = [Mock(spec=Ingredient) for _ in range(3)]
        burger.ingredients = ingredients.copy()

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredients[i] for i in expected_indexes]

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price",
        [(100, [], 200),(125.5, [10, 20.5], 281.5),],)
    def test_get_price_returns_price_of_two_buns_and_all_ingredients(
        self, burger, bun_price, ingredient_prices, expected_price):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        ingredients = [Mock(spec=Ingredient) for _ in ingredient_prices]
        for ingredient, price in zip(ingredients, ingredient_prices):
            ingredient.get_price.return_value = price
        burger.set_buns(bun)
        burger.ingredients = ingredients

        result = burger.get_price()

        assert result == expected_price

    @pytest.mark.parametrize(
        "ingredient_type, expected_type",
        [("SAUCE", "sauce"),("FILLING", "filling"),],)
    def test_get_receipt_returns_formatted_receipt(
        self, burger, ingredient_type, expected_type):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "space bun"
        bun.get_price.return_value = 100
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = "meteor"
        ingredient.get_price.return_value = 25
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        result = burger.get_receipt()

        assert result == (
            "(==== space bun ====)\n"
            f"= {expected_type} meteor =\n"
            "(==== space bun ====)\n\n"
            "Price: 225")
