from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger."""

    def test_init_no_args_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_init_no_args_ingredients_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns_valid_bun_stores_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_one_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_add_ingredient_two_ingredients_both_in_list(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        assert burger.ingredients == [mock1, mock2]


    def test_remove_ingredient_valid_index_removes_ingredient(self):
        burger = Burger()
        mock1, mock2, mock3 = Mock(), Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock1, mock3]

    def test_remove_ingredient_last_index_removes_last(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock1]


    def test_move_ingredient_forward_changes_order(self):
        burger = Burger()
        mock1, mock2, mock3 = Mock(), Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock2, mock3, mock1]

    def test_move_ingredient_backward_changes_order(self):
        burger = Burger()
        mock1, mock2, mock3 = Mock(), Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients == [mock3, mock1, mock2]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100.0, [], 200.0),                       # только булочка, ×2
            (100.0, [50.0], 250.0),                   # одна начинка
            (100.0, [50.0, 30.0], 280.0),             # две начинки
            (0.0, [], 0.0),                           # нулевая цена булочки
            (99.99, [0.01], 200.0 - 0.01),            # дробные значения
        ],
    )
    def test_get_price_valid_inputs_returns_sum(
        self, bun_price, ingredient_prices, expected_price
    ):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == pytest.approx(expected_price)

    def test_get_receipt_no_ingredients_returns_only_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        expected = "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200.0"
        assert burger.get_receipt() == expected

    def test_get_receipt_with_ingredients_returns_full_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "cutlet"
        mock_ingredient.get_price.return_value = 50.0
        burger.add_ingredient(mock_ingredient)

        expected = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250.0"
        )
        assert burger.get_receipt() == expected

    @pytest.mark.parametrize(
        "ingredient_type, ingredient_name, expected_line",
        [
            ("FILLING", "cutlet", "= filling cutlet ="),
            ("SAUCE", "hot sauce", "= sauce hot sauce ="),
        ],
    )
    def test_get_receipt_ingredient_type_lowercased_in_line(
        self, ingredient_type, ingredient_name, expected_line
    ):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "bun"
        mock_bun.get_price.return_value = 0.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = 0.0
        burger.add_ingredient(mock_ingredient)

        assert expected_line in burger.get_receipt()
