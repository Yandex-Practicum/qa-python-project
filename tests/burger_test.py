from unittest.mock import Mock

import pytest

from tests.test_data import (
    BUN_NAME,
    BUN_PRICE,
    SAUCE_NAME,
    SAUCE_PRICE,
    FILLING_NAME,
    FILLING_PRICE,
)


class TestBurgerInit:
    """Проверка поведения бургера до установки булки."""

    def test_get_price_without_bun_raises_error(self, burger):
        """Если булка не установлена — get_price() падает."""
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_without_bun_raises_error(self, burger):
        """Если булка не установлена — get_receipt() падает."""
        with pytest.raises(AttributeError):
            burger.get_receipt()


class TestSetBuns:
    """Тесты метода set_buns."""

    def test_set_buns_allows_get_price(self, burger, mock_bun):
        """После set_buns() метод get_price() работает."""
        burger.set_buns(mock_bun)
        assert burger.get_price() == BUN_PRICE * 2

    def test_set_buns_allows_get_receipt(self, burger, mock_bun):
        """После set_buns() метод get_receipt() работает."""
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert BUN_NAME in receipt


class TestAddIngredient:
    """Тесты метода add_ingredient."""

    def test_add_ingredient_increases_price(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        price_before = burger.get_price()

        burger.add_ingredient(mock_sauce)
        price_after = burger.get_price()

        assert price_after == price_before + SAUCE_PRICE

    def test_add_multiple_ingredients_increases_price(
        self, burger, mock_bun, mock_sauce, mock_filling
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE


class TestRemoveIngredient:
    """Тесты метода remove_ingredient."""

    def test_remove_ingredient_decreases_price(
        self, burger, mock_bun, mock_sauce
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        price_before = burger.get_price()

        burger.remove_ingredient(0)
        price_after = burger.get_price()

        assert price_after == price_before - SAUCE_PRICE

    def test_remove_only_ingredient_returns_to_bun_price(
        self, burger, mock_bun, mock_sauce
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        burger.remove_ingredient(0)

        assert burger.get_price() == BUN_PRICE * 2


class TestMoveIngredient:
    """Тесты метода move_ingredient."""

    def test_move_ingredient_changes_order(
        self, burger, mock_bun, mock_sauce, mock_filling
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.move_ingredient(0, 1)

        receipt = burger.get_receipt()
        sauce_position = receipt.index(SAUCE_NAME)
        filling_position = receipt.index(FILLING_NAME)
        assert filling_position < sauce_position


class TestGetPrice:
    """Тесты метода get_price."""

    def test_get_price_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == BUN_PRICE * 2

    @pytest.mark.parametrize("sauce_price", [0.0, 50.0, 100.0, 999.99])
    def test_get_price_with_different_sauce_prices(
        self, burger, mock_bun, sauce_price
    ):
        sauce = Mock()
        sauce.get_price.return_value = sauce_price

        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)

        assert burger.get_price() == BUN_PRICE * 2 + sauce_price


class TestGetReceipt:
    """Тесты метода get_receipt."""

    def test_get_receipt_without_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()

        expected = (
            f"(==== {BUN_NAME} ====)\n"
            f"(==== {BUN_NAME} ====)\n"
            f"\n"
            f"Price: {BUN_PRICE * 2}"
        )
        assert receipt == expected

    def test_get_receipt_with_sauce(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        receipt = burger.get_receipt()
        assert f"= sauce {SAUCE_NAME} =" in receipt

    def test_get_receipt_with_filling(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()
        assert f"= filling {FILLING_NAME} =" in receipt

    def test_get_receipt_full(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()
        expected = (
            f"(==== {BUN_NAME} ====)\n"
            f"= sauce {SAUCE_NAME} =\n"
            f"= filling {FILLING_NAME} =\n"
            f"(==== {BUN_NAME} ====)\n"
            f"\n"
            f"Price: {BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE}"
        )
        assert receipt == expected