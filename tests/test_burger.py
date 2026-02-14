import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_constants import (
    BUN_BLACK, BUN_WHITE, BUN_RED, BUN_TEST,
    PRICE_50, PRICE_100, PRICE_150, PRICE_200, PRICE_500, PRICE_400, PRICE_75,
    INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING,
    INGREDIENT_HOT_SAUCE, INGREDIENT_SOUR_CREAM, INGREDIENT_CUTLET
)


class TestBurger:
    # Тесты для класса Burger.

    def test_set_buns(self, bun):
        # Проверка установки булочек.
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, ingredient):
        # Проверка добавления ингредиента.
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_add_multiple_ingredients(self):
        # Проверка добавления нескольких ингредиентов.
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self):
        # Проверка удаления ингредиента.
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        # Проверка перемещения ингредиента.
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_100)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_SOUR_CREAM, PRICE_200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == ingredient1

    @pytest.mark.parametrize("bun_name,bun_price,ingredient_count,expected_price", [
        (BUN_BLACK, PRICE_100, 0, PRICE_200),
        (BUN_WHITE, PRICE_50, 1, PRICE_200),
        (BUN_RED, PRICE_100, 3, PRICE_500),
    ])
    def test_get_price(self, bun_name, bun_price, ingredient_count, expected_price):
        # Проверка расчета цены бургера.
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        
        # Добавляем ингредиенты с фиксированной ценой
        for i in range(ingredient_count):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun):
        # Проверка получения чека.
        burger = Burger()
        burger.set_buns(bun)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        receipt = burger.get_receipt()
        assert BUN_BLACK in receipt
        assert INGREDIENT_HOT_SAUCE in receipt
        assert INGREDIENT_CUTLET in receipt
        assert f"Price: {PRICE_400}" in receipt

    def test_get_receipt_empty_ingredients(self, bun):
        # Проверка получения чека без ингредиентов.
        burger = Burger()
        burger.set_buns(bun)
        
        receipt = burger.get_receipt()
        assert BUN_BLACK in receipt
        assert f"Price: {PRICE_200}" in receipt

    def test_get_price_with_mocked_bun(self):
        # Проверка расчета цены с использованием мока для булочки.
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = PRICE_50
        burger.set_buns(mock_bun)
        
        price = burger.get_price()
        assert price == PRICE_100  # Две булочки
        mock_bun.get_price.assert_called()

    def test_get_price_with_mocked_ingredients(self):
        # Проверка расчета цены с использованием моков для ингредиентов.
        burger = Burger()
        bun = Bun(BUN_TEST, PRICE_100)
        burger.set_buns(bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = PRICE_75
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        price = burger.get_price()
        expected_price = PRICE_200 + PRICE_150  # 200 за булочки (100*2) + 150 за ингредиенты (75*2)
        assert price == expected_price
        assert mock_ingredient.get_price.call_count == 2

    def test_remove_ingredient_with_invalid_index(self):
        # Проверка удаления ингредиента с недопустимым индексом.
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        burger.add_ingredient(ingredient)
        
        # Попытка удалить несуществующий индекс должна вызвать IndexError
        with pytest.raises(IndexError) as excinfo:
            burger.remove_ingredient(1)

        assert isinstance(excinfo.value, IndexError)

    def test_move_ingredient_with_invalid_indices(self):
        # Проверка перемещения ингредиента с недопустимыми индексами.
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)
        burger.add_ingredient(ingredient)
        
        # Попытка переместить несуществующий индекс должна вызвать IndexError
        with pytest.raises(IndexError) as excinfo:
            burger.move_ingredient(1, 0)

        assert isinstance(excinfo.value, IndexError)

