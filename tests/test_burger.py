import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    # Тесты для set_buns()
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты для add_ingredient()
    def test_add_ingredient_appends_ingredient_to_list(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients[0])
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients[0]

    def test_add_ingredient_appends_multiple_ingredients(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients[0])
        burger.add_ingredient(mock_ingredients[1])
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredients[0]
        assert burger.ingredients[1] == mock_ingredients[1]

    # Тесты для remove_ingredient()
    def test_remove_ingredient_deletes_correct_element(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredients[0]
        assert burger.ingredients[1] == mock_ingredients[2]

    def test_remove_ingredient_deletes_first_element(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredients[1]
        assert burger.ingredients[1] == mock_ingredients[2]

    def test_remove_ingredient_deletes_last_element(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.remove_ingredient(2)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredients[0]
        assert burger.ingredients[1] == mock_ingredients[1]

    # Тесты для move_ingredient()
    def test_move_ingredient_moves_element_forward(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == mock_ingredients[0]
        assert burger.ingredients[0] == mock_ingredients[1]
        assert burger.ingredients[1] == mock_ingredients[2]

    def test_move_ingredient_moves_element_backward(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == mock_ingredients[2]
        assert burger.ingredients[1] == mock_ingredients[0]
        assert burger.ingredients[2] == mock_ingredients[1]

    def test_move_ingredient_moves_to_same_position(self, mock_ingredients):
        burger = Burger()
        burger.ingredients = mock_ingredients.copy()
        burger.move_ingredient(1, 1)
        assert burger.ingredients[0] == mock_ingredients[0]
        assert burger.ingredients[1] == mock_ingredients[1]
        assert burger.ingredients[2] == mock_ingredients[2]

    # Тесты для get_price()
    def test_get_price_returns_correct_price_with_one_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        ing = Mock()
        ing.get_price.return_value = 100
        burger.add_ingredient(ing)
        assert burger.get_price() == 300.0

    def test_get_price_returns_correct_price_with_multiple_ingredients(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        assert burger.get_price() == 650.0

    def test_get_price_returns_correct_price_without_ingredients(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    @pytest.mark.parametrize("ingredient_prices, expected_price", [
        ([100], 300),
        ([100, 200], 500),
        ([50, 75, 125], 450),
    ])
    def test_get_price_with_different_ingredient_prices(self, mock_bun, ingredient_prices, expected_price):
        burger = Burger()
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)
        assert burger.get_price() == expected_price

    # Тесты для get_receipt()
    def test_get_receipt_returns_correct_format_with_multiple_ingredients(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ing in mock_ingredients:
            burger.add_ingredient(ing)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "= sauce sour cream =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 650"
        )
        assert burger.get_receipt() == expected

    def test_get_receipt_returns_correct_format_without_ingredients(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        expected = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200"
        )
        assert burger.get_receipt() == expected

    def test_get_receipt_returns_correct_format_with_one_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        ing = Mock()
        ing.get_name.return_value = "hot sauce"
        ing.get_type.return_value = "SAUCE"
        ing.get_price.return_value = 100
        burger.add_ingredient(ing)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"
        )
        assert burger.get_receipt() == expected

    def test_get_receipt_returns_correct_format_with_float_price(self, mock_bun):
        burger = Burger()
        mock_bun.get_price.return_value = 100.5
        burger.set_buns(mock_bun)
        ing = Mock()
        ing.get_name.return_value = "hot sauce"
        ing.get_type.return_value = "SAUCE"
        ing.get_price.return_value = 50.25
        burger.add_ingredient(ing)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 251.25"
        )
        assert burger.get_receipt() == expected