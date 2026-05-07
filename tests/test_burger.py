from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_stores_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient_changes_order(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient3
        assert burger.ingredients[2] == mock_ingredient1

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [], 200),
        (200, [100], 500),
        (300, [100, 200], 900),
        (150.5, [50.5, 75.0], 426.5),
    ])
    def test_get_price_calculates_correctly(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_formatted_string(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = "SAUCE"
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 100

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = "FILLING"
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 100

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )

        assert burger.get_receipt() == expected_receipt