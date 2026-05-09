import pytest
from unittest.mock import Mock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from burger import Burger

class TestBurger:

    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_name.return_value = "Черная булочка"
        bun.get_price.return_value = 100.0
        return bun

    @pytest.fixture
    def mock_ingredient(self):
        ingredient = Mock()
        ingredient.get_name.return_value = "Сыр чеддер"
        ingredient.get_price.return_value = 50.0
        ingredient.get_type.return_value = "cheese"
        return ingredient

    @pytest.fixture
    def mock_sauce(self):
        sauce = Mock()
        sauce.get_name.return_value = "Томатный соус"
        sauce.get_price.return_value = 30.0
        sauce.get_type.return_value = "sauce"
        return sauce

    @pytest.fixture
    def burger_with_ingredients(self, mock_bun, mock_ingredient, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_sauce)
        return burger

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_add_multiple_ingredients(self, mock_ingredient, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient
        assert burger.ingredients[1] == mock_sauce

    def test_remove_ingredient_valid_index(self, burger_with_ingredients):
        burger_with_ingredients.remove_ingredient(0)
        assert len(burger_with_ingredients.ingredients) == 1
        assert burger_with_ingredients.ingredients[0].get_name() == "Томатный соус"

    def test_remove_ingredient_last(self, burger_with_ingredients):
        burger_with_ingredients.remove_ingredient(1)
        assert len(burger_with_ingredients.ingredients) == 1
        assert burger_with_ingredients.ingredients[0].get_name() == "Сыр чеддер"

    def test_remove_ingredient_out_of_range(self, burger_with_ingredients):
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(10)

    def test_remove_ingredient_from_empty_burger(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_forward(self, burger_with_ingredients):
        burger_with_ingredients.move_ingredient(0, 1)
        assert burger_with_ingredients.ingredients[0].get_name() == "Томатный соус"
        assert burger_with_ingredients.ingredients[1].get_name() == "Сыр чеддер"

    def test_move_ingredient_backward(self, burger_with_ingredients):
        burger_with_ingredients.move_ingredient(1, 0)
        assert burger_with_ingredients.ingredients[0].get_name() == "Томатный соус"
        assert burger_with_ingredients.ingredients[1].get_name() == "Сыр чеддер"

    def test_move_ingredient_same_index(self, burger_with_ingredients):
        burger_with_ingredients.move_ingredient(0, 0)
        assert burger_with_ingredients.ingredients[0].get_name() == "Сыр чеддер"
        assert burger_with_ingredients.ingredients[1].get_name() == "Томатный соус"

    def test_move_ingredient_out_of_range(self, burger_with_ingredients):
        with pytest.raises(IndexError):
            burger_with_ingredients.move_ingredient(5, 0)

    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [50, 30], 280),
        (80, [40], 200),
        (0, [20, 20, 20], 60),
        (150, [], 300),
        (75, [10, 20, 30, 40], 250)
    ])
    def test_get_price_parametrized(self, bun_price, ing_prices, expected):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        for price in ing_prices:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)
        assert burger.get_price() == expected

    def test_get_price_no_ingredients(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_receipt_full(self, mock_bun, mock_ingredient, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        expected = (
            "(==== Черная булочка ====)\n"
            "= cheese Сыр чеддер =\n"
            "= sauce Томатный соус =\n"
            "(==== Черная булочка ====)\n"
            "\nPrice: 280.0"
        )
        assert receipt == expected

    def test_get_receipt_only_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected = (
            "(==== Черная булочка ====)\n"
            "(==== Черная булочка ====)\n"
            "\nPrice: 200.0"
        )
        assert receipt == expected

    def test_bun_methods_called(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.get_price()
        mock_bun.get_price.assert_called()
        burger.get_receipt()
        mock_bun.get_name.assert_called()