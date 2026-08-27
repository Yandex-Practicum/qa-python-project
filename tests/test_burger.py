"""Тесты для класса Burger."""

import pytest
from unittest.mock import Mock

from burger import Burger


class TestBurger:
    """Тесты для класса Burger."""

    def test_set_buns(self):
        """Проверка установки булочки."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
        assert burger.bun.get_name() == "black bun"
        assert burger.bun.get_price() == 100.0

    def test_add_ingredient(self):
        """Проверка добавления ингредиента."""
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        """Проверка удаления ингредиента."""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        """Проверка перемещения ингредиента."""
        burger = Burger()
        mock_1 = Mock()
        mock_2 = Mock()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_2
        assert burger.ingredients[1] == mock_1

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100.0, [], 200.0),
        (100.0, [100.0], 300.0),
        (200.0, [100.0, 200.0], 700.0),
        (300.0, [100.0, 200.0, 300.0], 1200.0),
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected):
        """Проверка расчёта цены бургера с параметризацией."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected

    @pytest.mark.parametrize("ingredient_type,ingredient_name,expected_line", [
        ("SAUCE", "hot sauce", "= sauce hot sauce ="),
        ("FILLING", "cutlet", "= filling cutlet ="),
    ])
    def test_get_receipt(self, ingredient_type, ingredient_name, expected_line):
        """Проверка формирования чека с параметризацией."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = 100.0
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert expected_line in receipt
        assert "Price: 300.0" in receipt