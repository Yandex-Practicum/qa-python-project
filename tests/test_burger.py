import pytest
import allure

from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import TestData


class TestBurger:
    @allure.title("Проверка выбора булочки")
    def test_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Проверка добавления ингредиента")
    def test_add_ingredient(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.ingredients == [mock_ingredient_sauce]

    @allure.title("Проверка удаления ингредиента")
    def test_remove_ingredient(self, burger, mock_ingredient_filling):
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @allure.title("Проверка перемещения ингредиента")
    def test_move_ingredient(
        self, burger, mock_ingredient_filling, mock_ingredient_sauce
    ):
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient_sauce
        assert burger.ingredients[1] == mock_ingredient_filling

    @allure.title("Проверка получения цены")
    def test_get_price(self, burger, mock_bun, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient_filling.get_price()
        assert burger.get_price() == expected_price

    @allure.title("Проверка получения чека")
    def test_get_receipt(
        self, burger, mock_bun, mock_ingredient_filling, mock_ingredient_sauce
    ):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_receipt = f"""(==== {mock_bun.get_name()} ====)
= {mock_ingredient_filling.get_type().lower()} {mock_ingredient_filling.get_name()} =
= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =
(==== {mock_bun.get_name()} ====)

Price: {burger.get_price()}"""

        assert burger.get_receipt() == expected_receipt
