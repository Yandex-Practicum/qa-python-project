import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from data_tests import get_price_test_data

class TestBurger:
    def test_set_buns(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price(self, mock_bun, mock_ingredient, burger):
        mock_bun.get_price.return_value = 5.0
        mock_ingredient.get_price.return_value = 2.0
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = 5.0 * 2 + 2.0  # Цена двух булочек и одного ингредиента
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient, burger):
        mock_bun.get_name.return_value = "Белая булочка"
        mock_bun.get_price.return_value = 5.0
        mock_ingredient.get_name.return_value = "Сыр"
        mock_ingredient.get_type.return_value = "Начинка"
        mock_ingredient.get_price.return_value = 2.0
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_receipt = (
            "(==== Белая булочка ====)\n"
            "= начинка Сыр =\n"
            "(==== Белая булочка ====)\n\n"
            "Price: 12.0"
        )
        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize("ingredient_prices, expected_total_price", get_price_test_data)
    def test_get_price_with_multiple_ingredients(self, mock_bun, burger, ingredient_prices, expected_total_price):
        mock_bun.get_price.return_value = 5.0
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_total_price