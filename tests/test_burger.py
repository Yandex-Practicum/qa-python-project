import pytest
from praktikum.burger import Burger
from helpers import make_mock_bun, make_mock_ingredient

class TestBurger:
    def test_get_price_without_ingredients_and_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        expected_price = mock_bun.get_price.return_value * 2
        assert burger.get_price() == expected_price

    def test_get_price_with_single_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value
        assert burger.get_price() == expected_price

    def test_add_ingredient_increases_ingredients_list(self, burger, mock_ingredient):
        initial_count = len(burger.get_ingredients())
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.get_ingredients()
        assert len(burger.get_ingredients()) == initial_count + 1

    def test_get_ingredients_returns_list(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        ingredients = burger.get_ingredients()
        assert isinstance(ingredients, list)
        assert mock_ingredient in ingredients

    def test_move_ingredient_valid_indices(self, burger, mock_ingredient, another_mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(another_mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.get_ingredients()[1] == mock_ingredient

    def test_remove_ingredient_valid_index(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(1)
        assert mock_ingredient not in burger.get_ingredients()

    def test_remove_ingredient_invalid_index_with_assert(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(999)

    def test_clear_ingredients(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        while burger.get_ingredients():
            burger.remove_ingredient(0)
        assert burger.get_ingredients() == []

    def test_get_receipt_includes_bun_and_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        total_price = burger.get_price()
        bun_name = mock_bun.get_name()
        ingredient_type = str(mock_ingredient.get_type()).lower()
        ingredient_name = mock_ingredient.get_name()

        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"= {ingredient_type} {ingredient_name} =\n"
            f"(==== {bun_name} ====)\n"
            f"\n"
            f"Price: {total_price}"
        )

        actual_receipt = burger.get_receipt()

        print("Expected receipt:\n" + expected_receipt)
        print("Actual receipt:\n" + actual_receipt)

        assert actual_receipt == expected_receipt