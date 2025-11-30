import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *
from data import *


class TestBurger:

    # Проверка инициализации пустого бургера
    def test_burger_initialization(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    # Проверка установки булочки
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка установки ингредиента
    @pytest.mark.parametrize(
        "ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
    )
    def test_add_ingredient(self, ingredient_type, mock_ingredients):
        burger = Burger()
        ingredient = mock_ingredients[ingredient_type]
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    # Проверка удаления ингредиента
    def test_remove_ingredient(self, mock_ingredient_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Проверка перемещения ингредиента
    def test_move_ingredient(self, mock_ingredient_sauce, mock_ingredient_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce

    # Проверка расчета цены бургера
    @pytest.mark.parametrize(
        "bun_price, sauce_price, filling_price, expected_price", PRICE_CALCULATIONS
    )
    def test_get_price(
        self, bun_price, sauce_price, filling_price, expected_price, mock_bun
    ):
        mock_bun.get_price.return_value = bun_price
        sauce_ingredient = Mock()
        sauce_ingredient.get_price.return_value = sauce_price
        filling_ingredient = Mock()
        filling_ingredient.get_price.return_value = filling_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.get_price() == expected_price

    # Проверка формирования чека
    def test_get_receipt(
        self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling
    ):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        expected_receipt = (
            f"(==== {BUN_DATA['name']} ====)\n"
            f"= {INGREDIENT_SAUCE_DATA['type'].lower()} {INGREDIENT_SAUCE_DATA['name']} =\n"
            f"= {INGREDIENT_FILLING_DATA['type'].lower()} {INGREDIENT_FILLING_DATA['name']} =\n"
            f"(==== {BUN_DATA['name']} ====)\n"
            f"\n"
            f"Price: {burger.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt
