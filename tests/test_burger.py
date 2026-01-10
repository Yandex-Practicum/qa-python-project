import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    # --- Тесты для set_buns ---
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    # --- Тесты для add_ingredient ---
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    # --- Тесты для remove_ingredient ---
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.ingredients = [mock_ingredient]

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_remove_ingredient_with_invalid_index(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.ingredients = [mock_ingredient]

        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    # --- Тесты для move_ingredient ---
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    # --- Тесты для get_price ---
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100, [50, 30], 280),  # 100*2 + 50 + 30
        (50.5, [20.25], 121.25),  # 50.5*2 + 20.25
        (0, [10, 20], 30),  # 0*2 + 10 + 20
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()

        # Мокаем булочку
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.bun = mock_bun

        # Мокаем ингредиенты
        burger.ingredients = []
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.ingredients.append(mock_ingredient)

        assert burger.get_price() == expected

    # --- Тесты для get_receipt ---
    def test_get_receipt(self):
        burger = Burger()

        # Мокаем булочку
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100  # Цена булочки
        burger.bun = mock_bun

        # Мокаем ингредиенты с ценами
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = "FILLING"
        mock_ingredient1.get_name.return_value = "cheese"
        mock_ingredient1.get_price.return_value = 50  # Добавляем цену

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = "SAUCE"
        mock_ingredient2.get_name.return_value = "hot sauce"
        mock_ingredient2.get_price.return_value = 30  # Добавляем цену

        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cheese =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 280"  # 100*2 + 50 + 30 = 280
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_ingredients(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 50
        burger.bun = mock_bun

        expected_receipt = (
            "(==== white bun ====)\n"
            "(==== white bun ====)\n"
            "\n"
            "Price: 100"
        )

        assert burger.get_receipt() == expected_receipt