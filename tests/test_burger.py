import pytest
from unittest.mock import Mock

from burger import Burger


class TestBurger:

    def test_constructor_sets_bun_to_none(self):
        burger = Burger()

        assert burger.bun is None


    def test_constructor_creates_empty_ingredients_list(self):
        burger = Burger()

        assert burger.ingredients == []


    def test_set_buns_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun


    def test_add_ingredient_adds_ingredient_to_list(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]


    def test_remove_ingredient_removes_ingredient_by_index(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []


    def test_move_ingredient_changes_ingredient_position(self, burger, mock_ingredient):
        second_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [second_ingredient, mock_ingredient]


    def test_get_price_returns_correct_burger_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250


    def test_get_receipt_returns_correct_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== big bun ====)\n"
            "= sauce chilli sauce =\n"
            "(==== big bun ====)\n"
            "\n"
            "Price: 250"
        )

        assert burger.get_receipt() == expected_receipt

    # Негативные проверки

    def test_remove_ingredient_raises_index_error_for_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)


    def test_move_ingredient_raises_index_error_for_invalid_index(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)


    def test_get_price_raises_attribute_error_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()


    def test_get_receipt_raises_attribute_error_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()
