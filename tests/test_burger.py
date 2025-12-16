import pytest
import allure
from data_test import IngredientConstants as IC, Receipt
from praktikum.burger import Burger
from utils import Utils


class TestBurger:
    @allure.title('Проверка начального состояния артибута булка в бургере')
    def test_bun_in_burger_state(self):
        burger = Burger()
        assert burger.bun is None

    @allure.title('Проверка начального состояния артибута ингрeдиенты в бургере')
    def test_ingredients_in_burger_state(self):
        burger = Burger()
        assert burger.ingredients == []

    @allure.title('Успешная установка определенной булки для бургера')
    def test_set_buns_for_burger(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Успешное доваление соуса или начинки в бургер')
    @pytest.mark.parametrize('mock_ingredient', [[IC.SAUCE_TYPE, IC.SAUCE_NAME, IC.SAUCE_PRICE],
                                                 [IC.FILLING_TYPE, IC.FILLING_NAME, IC.FILLING_PRICE]])
    def test_add_one_ingredient_in_burger(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients == [mock_ingredient]

    @allure.title('Успешное добаление двух одинаковых, двух различных и трех ингредиентов в бургер')
    @pytest.mark.parametrize('mock_ingredients, expected_length', [[IC.TWO_SAME_INGREDIENTS, 2],
                                                                   [IC.SAUCE_AND_FILLING, 2],
                                                                   [IC.THREE_INGREDIENTS, 3]])
    def test_add_some_ingredients_in_burger(self, mock_ingredients, expected_length):
        burger = Burger()
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == expected_length and burger.ingredients == mock_ingredients

    @allure.title('Успешное удаление любого ингредиента в бургере')
    @pytest.mark.parametrize('ingredients,index,expected_length', [[IC.TWO_SAME_INGREDIENTS, 0, 1],
                                                                   [IC.SAUCE_AND_FILLING, 1, 1],
                                                                   [IC.THREE_INGREDIENTS, 2, 2]])
    def test_remove_any_ingredient_from_burger(self, ingredients, index, expected_length):
        burger = Burger()
        mock_ingredients = []
        for ingredient in ingredients:
            mock_ingredient = Utils.mock_ingredient(ingredient)
            burger.add_ingredient(mock_ingredient)
            mock_ingredients.append(mock_ingredient)
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == expected_length and mock_ingredients[index] is not burger.ingredients

    @allure.title('Успешное удаление двух ингредиентов в бургере')
    def test_remove_twice_ingredient_from_burger(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0 and burger.ingredients == []

    @allure.title('Успешное перемещение ингредиента в бургере')
    def test_move_one_ingredient_in_burger(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @allure.title('Успешное перемещение двух ингредиенов в бургере')
    def test_move_twice_ingredient_in_burger(self):
        burger = Burger()
        mock_ingredients = []
        for ingredient in IC.THREE_INGREDIENTS:
            mock_ingredient = Utils.mock_ingredient(ingredient)
            burger.add_ingredient(mock_ingredient)
            mock_ingredients.append(mock_ingredient)
        burger.move_ingredient(1, 0)
        burger.move_ingredient(2, 1)
        assert burger.ingredients == [mock_ingredients[1], mock_ingredients[2], mock_ingredients[0]]

    @allure.title('Успешное получение цены бургера с различными ингредиентами')
    @pytest.mark.parametrize('ingredients, expected_price', [[IC.TWO_SAME_INGREDIENTS, 400],
                                                             [IC.SAUCE_AND_FILLING, 400],
                                                             [IC.THREE_INGREDIENTS, 600]])
    def test_get_price_burger(self, mock_bun, ingredients, expected_price):
        burger = Burger()
        burger.set_buns(mock_bun)
        for ingredient in ingredients:
            mock_ingredient = Utils.mock_ingredient(ingredient)
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expected_price

    @allure.title('Успешный чек с названием булки, ингредиентов и итоговой суммы')
    def test_get_receipt_for_burger(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        assert burger.get_receipt() == Receipt.BURGER_RECEIPT