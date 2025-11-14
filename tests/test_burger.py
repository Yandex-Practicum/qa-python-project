import pytest
from unittest.mock import patch

class TestBurger:
    def test_starting_value_of_burger(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_success_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_success_adding_ingredients_only_sauce(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_success_adding_ingredients_only_filling(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_success_removing_ingredient(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_unsuccess_removing_ingredient_from_empty_burger(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    @pytest.mark.parametrize("start_index, new_index, order", [(0, 1, [1, 0, 2]),(2, 0, [2, 0, 1]), (1, 1, [0, 1, 2]), (0, 2, [1, 2, 0])])
    def test_success_moving_of_ingredients(self, burger, multiple_ingredients, start_index, new_index, order):
        burger.ingredients = multiple_ingredients.copy()
        burger.move_ingredient(start_index, new_index)
        expected_ingredients = [multiple_ingredients[i] for i in order]
        assert burger.ingredients == expected_ingredients

    def test_unsuccess_moving_of_ingredients(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)

    def test_success_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        expected_price = 330.0
        assert burger.get_price() == expected_price

    def test_success_get_price_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        expected_price = 200.0
        assert burger.get_price() == expected_price

    def test_unsuccess_get_price_only_ingredients(self, burger, mock_ingredient_filling, mock_ingredient_sauce):
        with pytest.raises(AttributeError):
            burger.add_ingredient(mock_ingredient_filling)
            burger.add_ingredient(mock_ingredient_sauce)
            burger.get_price()

    def test_unsuccess_get_price_with_empty_burger(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_with_ingredients_success(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()

        expected_lines = [
            "(==== black bun ====)",
            "= sauce karri_sauce =",
            "= filling meat =",
            "(==== black bun ====)",
            "",
            "Price: 330.0"
        ]
        expected_receipt = "\n".join(expected_lines)

        assert receipt == expected_receipt

    def test_success_get_receipt_calls_get_price_internally(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        with patch.object(burger, 'get_price') as mock_get_price:
            mock_get_price.return_value = 200.0
            receipt = burger.get_receipt()
            mock_get_price.assert_called_once()
            assert "Price: 200.0" in receipt