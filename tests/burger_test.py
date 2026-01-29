from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from data import expected_receipt
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    # тест проверяет добавление булки
    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ('bun 1', 988),
            ('bun 2', 1255)
        ]
    )
    def test_set_buns(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    # тест проверяет добавление несуществующей булки
    def test_set_no_buns(self):
        burger = Burger()
        burger.set_buns(None)
        assert burger.bun is None

    # тест проверяет добавление ингредиента
    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient_mock

    # тест проверяет удаление ингредиента
    def test_remove_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # тест проверяет перемещение ингредиента
    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock(spec=Ingredient)
        ingredient_2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_2 and burger.ingredients[1] == ingredient_1

    # тест проверяет, что фактическая цена соответствует ожидаемой
    def test_get_price(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 100
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected_price = 100 * 2 + 50
        assert burger.get_price() == expected_price

    #  тест проверяет получение чека
    def test_get_receipt(self):
        burger = Burger()
        bun = Bun('white bun', 200)
        ingredient = Ingredient('sauce', 'hot sauce', 100)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_receipt() == expected_receipt

    # тест проверяет получение чека без добавления в бургер ингредиентов
    def test_receipt_without_ingredients(self):
        burger = Burger()
        burger.set_buns(Bun('white bun', 200))
        receipt = burger.get_receipt()
        assert '(==== white bun ====)' and 'Price: 400' in receipt
