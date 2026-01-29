import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import DataBurgerIngredients
from generators import *

class TestBurger:

    # Проверяем выбор булочки
    def test_set_buns_correct_bun(self):
        burger = Burger()
        expected_buns = DataBurgerIngredients.data_buns[0][0]
        burger.set_buns(expected_buns)

        assert burger.bun == expected_buns

    # Проверяем добавление одного ингредиента в бургер
    def test_add_ingredient_add_one_ingredient(self):
        burger = Burger()
        expected_ingredient = DataBurgerIngredients.data_ingredients[0]
        burger.add_ingredient(expected_ingredient)

        assert len(burger.ingredients) == 1 and expected_ingredient in burger.ingredients

    # Проверяем удаление ингредиента из бургера
    def test_remove_ingredient_zero_ingredient(self):
        burger = Burger()
        expected_ingredient = DataBurgerIngredients.data_ingredients[0]
        burger.add_ingredient(expected_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0 and expected_ingredient not in burger.ingredients

    # Проверяем перемещение позиции ингредиента
    def test_move_ingredient_in_burger(self):
        burger = Burger()
        expected_ingredient_1 = DataBurgerIngredients.data_ingredients[0]
        expected_ingredient_2 = DataBurgerIngredients.data_ingredients[-1]
        burger.add_ingredient(expected_ingredient_1)
        burger.add_ingredient(expected_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == expected_ingredient_2 and burger.ingredients[-1] == expected_ingredient_1

    # Проверяем получение цены бургера, через моки
    def test_get_price_burger(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        mock_bun.get_price.return_value = mock_bun_price
        mock_ingredient.get_price.return_value = mock_ingredient_price

        assert burger.get_price() == mock_bun_price * 2 + mock_ingredient_price

    # Проверяем получение рецепта бургера, через моки
    def test_get_receipt_return_correct(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        mock_bun.get_name.return_value = mock_bun_name
        mock_bun.get_price.return_value = mock_bun_price
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = mock_ingredient_name
        mock_ingredient.get_price.return_value = mock_ingredient_price
        receipt = f'(==== {mock_bun_name} ====)\n' \
                  f'= sauce {mock_ingredient_name} =\n' \
                  f'(==== {mock_bun_name} ====)\n' \
                  f'\nPrice: {mock_bun_price * 2 + mock_ingredient_price}'

        assert burger.get_receipt() == receipt
