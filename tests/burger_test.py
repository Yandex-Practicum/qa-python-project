import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.types import IngredientType


class TestBurger:

    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_name.return_value = "Краторная булка"
        bun.get_price.return_value = 100.0
        return bun

    @pytest.fixture
    def mock_ingredient_sauce(self):
        ingredient = Mock()
        ingredient.get_type.return_value = IngredientType.SAUCE
        ingredient.get_name.return_value = "Соус Spicy-X"
        ingredient.get_price.return_value = 50.0
        return ingredient

    @pytest.fixture
    def mock_ingredient_filling(self):
        ingredient = Mock()
        ingredient.get_type.return_value = IngredientType.FILLING
        ingredient.get_name.return_value = "Мясо бессмертных моллюсков"
        ingredient.get_price.return_value = 200.0
        return ingredient

    def test_set_buns_sets_correct_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self, burger, mock_ingredient_sauce):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == initial_count + 1

    def test_remove_ingredient_removes_from_list(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1

    def test_move_ingredient_changes_position(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        first_ingredient_before = burger.ingredients[0]
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == first_ingredient_before

    def test_get_price_calculates_correctly(self, burger, mock_bun, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_price = (mock_bun.get_price() * 2) + mock_ingredient_sauce.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_formats_correctly(self, burger, mock_bun, mock_ingredient_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)

        receipt = burger.get_receipt()

        assert mock_bun.get_name() in receipt
        assert mock_ingredient_sauce.get_name() in receipt
        assert "Price:" in receipt

    def test_remove_ingredient_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(999)

    def test_move_ingredient_invalid_index(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 999)

    def test_empty_burger_price(self, burger):
        assert burger.get_price() == 0

    def test_burger_with_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == mock_bun.get_price() * 2
