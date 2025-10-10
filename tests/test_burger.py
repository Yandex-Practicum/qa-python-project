import pytest
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self, sample_burger):
        new_bun = Mock()
        new_bun.get_name.return_value = "Новая булка"
        sample_burger.set_buns(new_bun)
        assert sample_burger.bun == new_bun

    def test_add_ingredient(self, sample_burger):
        new_ingredient = Mock()
        initial_count = len(sample_burger.ingredients)
        sample_burger.add_ingredient(new_ingredient)
        assert len(sample_burger.ingredients) == initial_count + 1

    def test_remove_ingredient(self, sample_burger):
        initial_count = len(sample_burger.ingredients)
        sample_burger.remove_ingredient(0)
        assert len(sample_burger.ingredients) == initial_count - 1

    def test_move_ingredient_changes_order(self, sample_burger):
        initial_order = [ingredient.get_name.return_value for ingredient in sample_burger.ingredients]
        sample_burger.move_ingredient(0, 1)
        new_order = [ingredient.get_name.return_value for ingredient in sample_burger.ingredients]
        assert new_order != initial_order

    def test_move_ingredient_correct_position(self, sample_burger):
        sample_burger.move_ingredient(0, 1)
        new_order = [ingredient.get_name.return_value for ingredient in sample_burger.ingredients]
        assert new_order == ["Говяжий метеорит", "Соус традиционный"]

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100, [50, 3000], 100 * 2 + 50 + 3000),
        (200, [100, 200], 200 * 2 + 100 + 200),
        (0, [], 0)
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected, empty_burger):
        burger = empty_burger

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    def test_get_receipt_with_ingredients(self, sample_burger):
        expected_receipt = (
            "(==== Краторная булка ====)\n"
            "= sauce Соус традиционный =\n"
            "= filling Говяжий метеорит =\n"
            "(==== Краторная булка ====)\n"
            "\n"
            "Price: 3250"
        )
        assert sample_burger.get_receipt() == expected_receipt

