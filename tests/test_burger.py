import pytest

from unittest.mock import Mock
from data.test_data import BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE, INGREDIENT_TYPE_VALID, INGREDIENT_NAME_VALID, \
    INGREDIENT_PRICE_VALID, EXPECTED_RECEIPT
from praktikum.burger import Burger


class TestBurger:

    def test_set_bun(self):
        mock_bun = Mock()
        mock_bun.name = BUN_VALID_NAME
        mock_bun.price = BUN_VALID_FLOAT_PRICE
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.name == BUN_VALID_NAME, 'Булочка не соответствует ожидаемой'

    def test_add_ingredient(self, mock_and_add_ingredient):
        burger, mock_ingredient = mock_and_add_ingredient
        assert mock_ingredient in burger.ingredients, 'Добавленный ингредиент отсутствует'

    def test_remove_ingredient(self, mock_and_add_ingredient):
        burger, mock_ingredient = mock_and_add_ingredient
        burger.remove_ingredient(0)

        assert mock_ingredient not in burger.ingredients, 'Добавленный ингредиент не был удален'

    def test_move_ingredient(self, mock_and_add_ingredient):
        burger, _ = mock_and_add_ingredient

        second_mock_ingredient = Mock()
        second_mock_ingredient.type = INGREDIENT_TYPE_VALID
        second_mock_ingredient.name = INGREDIENT_NAME_VALID + "2"
        second_mock_ingredient.price = INGREDIENT_PRICE_VALID
        burger.add_ingredient(second_mock_ingredient)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0].name == INGREDIENT_NAME_VALID + "2", 'Ингредиенты не поменялись местами'

    def test_get_price(self, mock_and_add_ingredient, bun):
        burger, mock_ingredient = mock_and_add_ingredient
        burger.set_buns(bun)

        expected_price = bun.get_price() * 2 + mock_ingredient.price
        assert burger.get_price() == pytest.approx(expected_price), 'Ожидаемая цена и полученная не совпадают'
        # без approx() тест падают, т.к. питон странно работает с числами с плавающей запятой

    def test_get_receipt_contents(self, mock_and_add_ingredient, bun):
        burger, _ = mock_and_add_ingredient
        burger.set_buns(bun)

        assert burger.get_receipt() == EXPECTED_RECEIPT, 'Ожидаемый рецепт и фактический не совпадают'

