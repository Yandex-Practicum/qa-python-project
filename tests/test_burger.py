import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import BurgerTestData, ReceiptData

class TestBurger:

    def test_bun_should_be_none_by_default(self):
        """отсутствие булочки по умолчанию"""
        burger = Burger()
        assert burger.bun is None

    def test_ingredients_should_be_empty_list_by_default(self):
        """пустой списк ингредиентов по умолчанию"""
        burger = Burger()
        assert not burger.ingredients

    def test_set_buns_updates_bun_correctly(self, mock_bun):
        """корректное установка булочки"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == mock_bun.get_name()

    def test_add_ingredient_appends_to_ingredients_list(self, mock_ingredient_filling):
        """добавление ингредиента в список"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.ingredients[0].get_name() == mock_ingredient_filling.get_name()

    def test_add_ingredient_multiple_same_correctly(self, mock_ingredient_filling):
        """корректное добавление нескольких одинаковых ингредиентов"""
        burger = Burger()
        for _ in range(5):
            burger.add_ingredient(mock_ingredient_filling)
        assert all(ingredient == mock_ingredient_filling for ingredient in burger.ingredients)

    def test_remove_ingredient_decreases_ingredients_count(self, mock_ingredient_filling):
        """удаление ингредиента по индексу"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients[0].get_name() == mock_ingredient_filling.get_name()

    def test_move_ingredient_changes_positions_correctly(self, mock_ingredient_filling):
        """перемещения ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == mock_ingredient_filling.get_name()
        assert burger.ingredients[1].get_name() == mock_ingredient_filling.get_name()

    @pytest.mark.parametrize('bun_price, ingredients_prices, expected_price', BurgerTestData.BURGERS_PRICE_DATA)
    def test_get_price_with_multiple_ingredients_correctly(
        self, mock_bun, bun_price, ingredients_prices, expected_price):
        """расчет цены с разным количеством ингредиентов"""
        burger = Burger()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredients_prices:
            mock = Mock()
            mock.get_price.return_value = price
            burger.add_ingredient(mock)
        assert burger.get_price() == expected_price

    def test_get_price_with_none_bun(self, mock_ingredient_filling):
        """корректная обработка отсутствия булочки при расчёте цены"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_structure_with_only_bun(self, mock_bun):
        """формат чека для бургера только с булочкой"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.get_receipt() == ReceiptData.EXP_ONLY_BUN

    def test_get_receipt_with_ingredients_of_different_type(self, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        """формат чека с разными типами ингредиентов"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.get_receipt() == ReceiptData.EXP_DIFF_INGREDS

    def test_get_receipt_with_multiple_ingredients_of_same_type(self, mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        """Проверк формат чека с повторяющимися ингредиентами"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.get_receipt() == ReceiptData.EXP_SAME_INGREDS

    def test_get_receipt_with_empty_ingredient_name(self, mock_bun, mock_ingredient_filling):
        """формат чека с пустыми названиями"""
        mock_ingredient_filling.get_type.return_value = ""
        mock_ingredient_filling.get_name.return_value = ""
        mock_bun.get_name.return_value = ""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        assert burger.get_receipt() == ReceiptData.EXP_EMPTY_NAME

    def test_get_receipt_with_no_bun_raises_error(self, mock_ingredient_filling):
        """вызов ошибки при генерации чека без булочки"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_filling)
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_with_none_ingredient_raises_error(self, mock_bun):
        """вызов ошибки при None-ингредиенте в чеке"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.ingredients.append(None)  # Добавление None напрямую
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_with_invalid_ingredient_type(self, mock_bun):
        """вызов ошибки при невалидном ингредиенте"""
        class InvalidIngredient:
            pass
        invalid_ingredient = InvalidIngredient()
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(invalid_ingredient)  # Добавление невалидного ингредиента
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_with_long_ingredient_name(self, mock_bun, mock_ingredient_filling):
        """обработка длинных названий в чеке"""
        mock_bun.get_name.return_value = "б" * 100
        mock_ingredient_filling.get_type.return_value = "т" * 100
        mock_ingredient_filling.get_name.return_value = "и" * 100
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()
        assert all(x in receipt for x in ("б" * 100, "т" * 100, "и" * 100))
        