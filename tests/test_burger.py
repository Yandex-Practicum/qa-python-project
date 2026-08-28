"""Тесты для класса Burger."""

import pytest
from unittest.mock import Mock

from burger import Burger


class TestBurger:
    """Тесты для класса Burger."""

    def test_set_buns_assigns_bun(self):
        """Проверка, что булочка устанавливается в поле bun."""
        burger = Burger()
        mock_bun = Mock()

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_set_buns_returns_name(self):
        """Проверка, что метод get_name булочки возвращает корректное имя."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"

        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == "black bun"

    def test_set_buns_returns_price(self):
        """Проверка, что метод get_price булочки возвращает корректную цену."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0

        burger.set_buns(mock_bun)

        assert burger.bun.get_price() == 100.0

    def test_add_ingredient_increases_count(self):
        """Проверка, что при добавлении ингредиента его количество увеличивается."""
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_add_ingredient_stores_value(self):
        """Проверка, что добавленный ингредиент хранится в списке."""
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        """Проверка удаления ингредиента."""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_first_to_second(self):
        """Проверка, что первый ингредиент перемещается на позицию второго."""
        burger = Burger()
        mock_1 = Mock()
        mock_2 = Mock()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_2

    def test_move_ingredient_second_to_first(self):
        """Проверка, что второй ингредиент перемещается на позицию первого."""
        burger = Burger()
        mock_1 = Mock()
        mock_2 = Mock()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)

        burger.move_ingredient(0, 1)

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
    def test_get_receipt_contains_bun(self, ingredient_type, ingredient_name, expected_line):
        """Проверка, что чек содержит название булочки."""
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

    @pytest.mark.parametrize("ingredient_type,ingredient_name,expected_line", [
        ("SAUCE", "hot sauce", "= sauce hot sauce ="),
        ("FILLING", "cutlet", "= filling cutlet ="),
    ])
    def test_get_receipt_contains_ingredient(self, ingredient_type, ingredient_name, expected_line):
        """Проверка, что чек содержит ингредиент."""
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

        assert expected_line in receipt

    @pytest.mark.parametrize("ingredient_type,ingredient_name,expected_line", [
        ("SAUCE", "hot sauce", "= sauce hot sauce ="),
        ("FILLING", "cutlet", "= filling cutlet ="),
    ])
    def test_get_receipt_contains_price(self, ingredient_type, ingredient_name, expected_line):
        """Проверка, что чек содержит итоговую цену."""
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

        assert "Price: 300.0" in receipt