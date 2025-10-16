import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_initial_state(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_integration_with_mocks(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        assert burger.bun.get_name() == "black bun"
        assert burger.ingredients[0].get_name() == "hot sauce"
        assert burger.ingredients[1].get_name() == "cutlet"

    def test_get_price(self, mock_bun, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)

        assert burger.get_price() == 300  # 100*2 + 100

    def test_ingredient_types(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert burger.ingredients[1].get_type() == INGREDIENT_TYPE_FILLING

    def test_receipt_format_exact_match(self, mock_bun, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt

    def test_move_ingredient_same_index(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.move_ingredient(0, 0)
        assert burger.ingredients == [mock_ingredient_sauce]

    def test_get_receipt_price_formatting(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        with patch.object(burger, 'get_price', return_value=123.45):
            receipt = burger.get_receipt()
            assert receipt.endswith("Price: 123.45")

    def test_get_receipt_with_no_bun_raises_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_remove_ingredient_from_empty_burger(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_remove_ingredient_success(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_invalid_index(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    def test_integration_with_real_data(self, real_buns, real_ingredients):
        burger = Burger()
        burger.set_buns(real_buns[0])
        burger.add_ingredient(real_ingredients[0])
        burger.add_ingredient(real_ingredients[3])

        assert burger.bun.get_name() == "black bun"
        assert burger.ingredients[0].get_name() == "hot sauce"
        assert burger.ingredients[1].get_name() == "cutlet"
        assert burger.get_price() == 300  # 100*2 + 100 + 100