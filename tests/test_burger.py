import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.database import Database


class TestBurger:

    # Тесты для set_buns()
    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Проверяем, что set_buns() устанавливает булочку"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты для add_ingredient()
    def test_add_ingredient_adds_to_list(self, mock_ingredient):
        """Проверяем, что add_ingredient() добавляет ингредиент"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    # Тесты для remove_ingredient()
    def test_remove_ingredient_removes_correctly(self, mock_ingredient):
        """Проверяем, что remove_ingredient() удаляет по индексу"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Тесты для move_ingredient()
    def test_move_ingredient_changes_position(self, mock_ingredient):
        """Проверяем, что move_ingredient() перемещает ингредиент"""
        burger = Burger()
        second_ingredient = MagicMock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    # Тесты для get_price()
    def test_get_price_calculates_correctly(self, mock_bun, mock_ingredient):
        """Проверяем расчет цены с булочкой и ингредиентами"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250  # (100*2) + 50

    # Тесты для get_receipt()
    def test_get_receipt_includes_bun_name(self, mock_bun):
        """Проверяем, что чек содержит название булочки"""
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n" \
                           "= sauce hot sauce =\n" \
                           "= filling cutlet =\n" \
                           "(==== black bun ====)\n\n" \
                           "Price: 400"
        assert expected_receipt == burger.get_receipt()