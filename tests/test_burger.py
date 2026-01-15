import pytest
from praktikum.burger import Burger

class TestBurger:

    def setup_method(self):
        self.burger = Burger()

    def test_set_buns(self, mock_bun):
        self.burger.set_buns(mock_bun)
        assert self.burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        self.burger.add_ingredient(mock_ingredient)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredients):
        self.burger.ingredients = mock_ingredients
        initial_count = len(self.burger.ingredients)
        self.burger.remove_ingredient(1)
        assert len(self.burger.ingredients) == initial_count - 1
        assert "Ingredient 1" not in [ing.get_name() for ing in self.burger.ingredients]

    def test_move_ingredient(self, mock_ingredients):
        self.burger.ingredients = mock_ingredients

        self.burger.move_ingredient(2, 0)
        assert self.burger.ingredients[0].get_name() == "Ingredient 2"
        assert self.burger.ingredients[1].get_name() == "Ingredient 0"

    @pytest.mark.parametrize(
        "ingredient_indexes, expected_price",
        [
            ([], 200 * 2),
            ([0, 1], 200 * 2 + 100 + 150),
            ([0, 1, 2], 200 * 2 + 100 + 150 + 200),
        ],
    )
    def test_get_price(self, mock_bun, mock_ingredients, ingredient_indexes, expected_price):
        self.burger.set_buns(mock_bun)

        for idx in ingredient_indexes:
            self.burger.add_ingredient(mock_ingredients[idx])

        assert self.burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            "\n"
            f"Price: {self.burger.get_price()}"
        )
        assert self.burger.get_receipt() == expected_receipt



