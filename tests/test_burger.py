from burger import Burger
import pytest
from parametrize_data import MOVE_DATA


class TestBurger:

    def test_set_bun_valid_bun_sets_bun(self,mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_valid_ingredient_adds_to_list(self,mock_ingredients):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        assert burger.ingredients == mock_ingredients

    def test_remove_ingredient_valid_index_removes_ingredient(self, mock_ingredients):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredients[1]]

    @pytest.mark.parametrize("start_index,new_index,expected_order", MOVE_DATA)
    def test_move_ingredient_index_to_new_index_changes_position(self, mock_ingredients, start_index, new_index, expected_order):
        burger = Burger()
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        burger.move_ingredient(start_index, new_index)
        assert burger.ingredients == [mock_ingredients[i] for i in expected_order]

    def test_get_price_with_bun_and_ingredients_returns_correct_price(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        expected_price = mock_bun.get_price.return_value * 2
        expected_price += sum(ing.get_price.return_value for ing in mock_ingredients)
        assert burger.get_price() == expected_price

    def test_get_receipt_with_bun_and_ingredients_returns_correct_receipt(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ing in mock_ingredients:
            burger.add_ingredient(ing)
        receipt = burger.get_receipt()
        lines = receipt.split("\n")
        assert lines[0] == f"(==== {mock_bun.get_name()} ====)"
        assert lines[-3] == f"(==== {mock_bun.get_name()} ====)"
        assert lines[-1] == f"Price: {burger.get_price()}"
        for ing in mock_ingredients:
            assert any(ing.get_name() in line for line in lines)