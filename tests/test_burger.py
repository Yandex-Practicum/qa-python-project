# test_burger.py

import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient


class TestBurger:
    """Тесты с использованием реальных объектов Bun и Ingredient"""

    def test_set_buns(self, empty_burger, parametrized_bun):
        """Параметризованная проверка установки булок через фикстуру"""
        empty_burger.set_buns(parametrized_bun)
        assert empty_burger.bun == parametrized_bun
        assert empty_burger.bun.get_name() == parametrized_bun.get_name()

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "Соус фирменный Space Sauce", 100),
        ("FILLING", "Биокотлета из марсианской Магнолии", 120)
    ], ids=["sauce", "filling"])
    def test_add_ingredient(self, empty_burger, ingredient_type, name, price):
        """Прямая параметризация создания ингредиентов"""
        ingredient = Ingredient(ingredient_type, name, price)
        empty_burger.add_ingredient(ingredient)
        assert ingredient in empty_burger.ingredients

    def test_add_ingredient_increases_count(self, empty_burger):
        initial_count = len(empty_burger.ingredients)
        empty_burger.add_ingredient(Ingredient("SAUCE", "Соус", 50))
        assert len(empty_burger.ingredients) == initial_count + 1

    def test_added_ingredient_is_present(self, empty_burger):
        ingredient = Ingredient("SAUCE", "Соус", 50)
        empty_burger.add_ingredient(ingredient)
        assert ingredient in empty_burger.ingredients

    def test_add_duplicate_ingredient(self, empty_burger, parametrized_ingredient):
        """Использование параметризованной фикстуры для ингредиента"""
        empty_burger.add_ingredient(parametrized_ingredient)
        empty_burger.add_ingredient(parametrized_ingredient)
        assert len(empty_burger.ingredients) == 2

    def test_remove_ingredient(self, prepared_burger):
        """Тест удаления ингредиента с готовым бургером из фикстуры"""
        initial_count = len(prepared_burger.ingredients)
        removed = prepared_burger.ingredients[0]
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_count - 1
        assert removed not in prepared_burger.ingredients

    @pytest.mark.parametrize("bun_price, ingr_prices, expected", [
        (988, [], 1976),
        (988, [80], 2056),
        (1255, [80, 424], 3014)
    ], ids=["only_bun", "bun+one_ingr", "bun+two_ingr"])
    def test_get_price(self, empty_burger, bun_price, ingr_prices, expected):
        """Комплексная параметризация теста ценообразования"""
        empty_burger.set_buns(Bun("Булка", bun_price))
        for idx, price in enumerate(ingr_prices):
            empty_burger.add_ingredient(Ingredient("FILLING", f"Начинка{idx}", price))
        assert empty_burger.get_price() == expected

    def test_receipt_contains_components(self, prepared_burger):
        """Проверка точного формата чека"""
        expected_receipt = (
            "(==== Краторная булка N-200i ====)\n"
            "= sauce Соус фирменный Space Sauce =\n"
            "= filling Биокотлета из марсианской Магнолии =\n"
            "(==== Краторная булка N-200i ====)\n"
            "\n"
            f"Price: {prepared_burger.get_price()}"  # Динамическая проверка цены
        )
        assert prepared_burger.get_receipt() == expected_receipt

    def test_remove_last_ingredient(self, prepared_burger):
        """Удаление последнего ингредиента"""
        initial_count = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(initial_count - 1)
        assert len(prepared_burger.ingredients) == initial_count - 1

    def test_remove_invalid_index_raises_error(self, prepared_burger):
        """Попытка удаления с неверным индексом"""
        with pytest.raises(IndexError):
            prepared_burger.remove_ingredient(999)

    @pytest.mark.parametrize("from_idx, to_idx, expected_order", [
        (0, 1, ["Биокотлета из марсианской Магнолии", "Соус фирменный Space Sauce"]),
        (1, 0, ["Биокотлета из марсианской Магнолии", "Соус фирменный Space Sauce"]),
        # Для текущей реализации move_ingredient с (0, -1) порядок не изменится
        (0, -1, ["Соус фирменный Space Sauce", "Биокотлета из марсианской Магнолии"])
    ], ids=["first_to_second", "second_to_first", "first_to_end"])
    def test_move_ingredient_order(self, prepared_burger, from_idx, to_idx, expected_order):
        """Проверка изменения порядка при перемещении"""
        prepared_burger.move_ingredient(from_idx, to_idx)
        result = [i.get_name() for i in prepared_burger.ingredients]
        assert result == expected_order

    def test_move_ingredient_keeps_length(self, prepared_burger):
        """При перемещении количество ингредиентов не меняется"""
        initial_length = len(prepared_burger.ingredients)
        prepared_burger.move_ingredient(0, -1)
        assert len(prepared_burger.ingredients) == initial_length

    def test_move_ingredient_preserves_types(self, prepared_burger):
        """При перемещении сохраняются типы объектов"""
        prepared_burger.move_ingredient(0, -1)
        assert all(isinstance(i, Ingredient) for i in prepared_burger.ingredients)

    def test_price_with_no_ingredients(self, empty_burger, default_bun):
        """Цена бургера без ингредиентов"""
        empty_burger.set_buns(default_bun)
        assert empty_burger.get_price() == default_bun.get_price() * 2

    def test_receipt_with_special_chars(self, empty_burger):
        """Чек с ингредиентами, содержащими спецсимволы"""
        empty_burger.set_buns(Bun("Булка*", 100))
        empty_burger.add_ingredient(Ingredient("SAUCE", "Соус#", 50))
        receipt = empty_burger.get_receipt()
        assert "Булка*" in receipt
        assert "Соус#" in receipt


class TestBurgerMockedObjects:
    """Тесты с использованием мок-объектов"""

    def test_set_buns_with_mock(self, mock_bun, empty_burger):
        """Проверка установки мок-булки"""
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun
        mock_bun.get_price.assert_not_called()

    def test_interaction_with_mocks(self, burger_with_mocks, mock_bun, mock_ingredient):
        """Комплексная проверка взаимодействия с моками"""
        assert burger_with_mocks.get_price() == 250
        mock_bun.get_price.assert_called_once()
        mock_ingredient.get_price.assert_called_once()

    @pytest.mark.parametrize("bun_price, ingr_price, expected", [
        (100, 50, 250),
        (200, 100, 500)
    ], ids=["cheap", "expensive"])
    def test_parametrized_mock_prices(self, mock_bun, mock_ingredient, bun_price, ingr_price, expected):
        """Параметризация с использованием готовых фикстур"""
        # Переопределяем возвращаемые значения для параметризованного теста
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingr_price

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected
        mock_bun.get_price.assert_called_once()
        mock_ingredient.get_price.assert_called_once()