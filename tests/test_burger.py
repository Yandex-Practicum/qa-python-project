import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_success(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_success(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing_2

    def test_move_ingredient_success(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ing_2, mock_ing_1]

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_price",
        [
            (100.0, [100.0, 200.0], 500.0),
            (200.0, [], 400.0),
            (150.5, [50.5], 351.5),
        ],
    )
    def test_get_price_success(self, bun_price, ing_prices, expected_price):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ing_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price

    def test_get_receipt_success(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        mock_ing_1 = Mock()
        mock_ing_1.get_type.return_value = "sauce"
        mock_ing_1.get_name.return_value = "chili sauce"
        mock_ing_1.get_price.return_value = 300.0

        mock_ing_2 = Mock()
        mock_ing_2.get_type.return_value = "filling"
        mock_ing_2.get_name.return_value = "cutlet"
        mock_ing_2.get_price.return_value = 100.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce chili sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 600.0"
        )

        assert burger.get_receipt() == expected_receipt