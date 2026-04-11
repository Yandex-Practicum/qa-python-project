# tests/test_burger.py

import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """
    Тесты для класса Burger.
    Все внешние зависимости (Bun, Ingredient) заменяются моками (Mock).
    """

    # ------------------------------------------------------------------
    # Тесты для set_buns()
    # ------------------------------------------------------------------
    def test_set_buns_sets_bun_attribute(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # ------------------------------------------------------------------
    # Тесты для add_ingredient()
    # ------------------------------------------------------------------
    def test_add_ingredient_appends_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_add_multiple_ingredients_increases_list_correctly(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [mock1, mock2]

    # ------------------------------------------------------------------
    # Тесты для remove_ingredient()
    # ------------------------------------------------------------------
    def test_remove_ingredient_deletes_correct_item(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)

        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock2

    def test_remove_ingredient_with_last_index(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)

        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock1

    # ------------------------------------------------------------------
    # Тесты для move_ingredient()
    # ------------------------------------------------------------------
    def test_move_ingredient_changes_order_correctly(self):
        burger = Burger()
        mock1, mock2, mock3 = Mock(), Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.add_ingredient(mock3)

        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock2, mock3, mock1]

    def test_move_ingredient_to_same_index_does_nothing(self):
        burger = Burger()
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)

        burger.move_ingredient(1, 1)
        assert burger.ingredients == [mock1, mock2]

    # ------------------------------------------------------------------
    # Тесты для get_price() (параметризованные)
    # ------------------------------------------------------------------
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected", [
        (100.0, [], 200.0),                     # только булка
        (150.0, [50.0], 350.0),                 # булка + 1 ингредиент
        (200.0, [50.0, 75.5, 30.0], 555.5),     # булка + 3 ингредиента
        (300.0, [100.0, 200.0], 900.0)          # 2*300 + 100 + 200 = 900
    ])
    def test_get_price_with_various_ingredients(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected

    # ------------------------------------------------------------------
    # Тесты для get_receipt() (параметризованные)
    # ------------------------------------------------------------------
    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredients_data, expected_receipt",
        [
            # 1. Без ингредиентов
            (
                "black bun", 100.0,
                [],
                "(==== black bun ====)\n"
                "(==== black bun ====)\n\n"
                "Price: 200.0"
            ),
            # 2. Один соус
            (
                "red bun", 300.0,
                [("SAUCE", "hot sauce", 100.0)],
                "(==== red bun ====)\n"
                "= sauce hot sauce =\n"
                "(==== red bun ====)\n\n"
                "Price: 700.0"
            ),
            # 3. Одна начинка
            (
                "white bun", 200.0,
                [("FILLING", "cutlet", 150.0)],
                "(==== white bun ====)\n"
                "= filling cutlet =\n"
                "(==== white bun ====)\n\n"
                "Price: 550.0"
            ),
            # 4. Соус + начинка
            (
                "black bun", 100.0,
                [("SAUCE", "chili sauce", 300.0), ("FILLING", "dinosaur", 200.0)],
                "(==== black bun ====)\n"
                "= sauce chili sauce =\n"
                "= filling dinosaur =\n"
                "(==== black bun ====)\n\n"
                "Price: 700.0"
            ),
            # 5. Несколько ингредиентов одного типа
            (
                "red bun", 300.0,
                [("SAUCE", "sour cream", 200.0), ("SAUCE", "ketchup", 50.0)],
                "(==== red bun ====)\n"
                "= sauce sour cream =\n"
                "= sauce ketchup =\n"
                "(==== red bun ====)\n\n"
                "Price: 850.0"
            ),
        ]
    )
    def test_get_receipt_with_various_combinations(self, bun_name, bun_price, ingredients_data, expected_receipt):
        """
        Параметризованный тест для проверки формирования чека.
        ingredients_data: список кортежей (тип, имя, цена)
        """
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for ing_type, ing_name, ing_price in ingredients_data:
            mock_ing = Mock()
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_name.return_value = ing_name
            mock_ing.get_price.return_value = ing_price
            burger.add_ingredient(mock_ing)

        assert burger.get_receipt() == expected_receipt
        