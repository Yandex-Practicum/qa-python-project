import allure

import pytest
from data import *
from praktikum.burger import Burger


class TestBurger:
    @allure.title('Проверка начального состояния атрибута bun')
    @allure.description('Проверяем что начальное состояние атрибута bun равняется None')
    def test_bun_initial_state(self):
        burger = Burger()
        assert burger.bun is None

    @allure.title('Проверка начального состояния атрибута ingredients')
    @allure.description('Проверяем что начальное состояние атрибута ingredients равняется пустому списку')
    def test_ingredients_initial_state(self):
        burger = Burger()
        assert burger.ingredients == []

    @allure.title('Проверка метода set_buns')
    @allure.description('Проверяем, что метод set_buns корректно устанавливает значение атрибута bun')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка метода add_ingredient')
    @allure.description('Проверяем, что метод add_ingredient корректно добавляет ингредиент в атрибут ingredients')
    @pytest.mark.parametrize('mock_ingredients, expected_len', [
        [IngredientsCombinations.only_sauce, len(IngredientsCombinations.only_sauce)],
        [IngredientsCombinations.only_filling, len(IngredientsCombinations.only_filling)],
        [IngredientsCombinations.two_same_sauces, len(IngredientsCombinations.two_same_sauces)],
        [IngredientsCombinations.two_same_fillings, len(IngredientsCombinations.two_same_fillings)],
        [IngredientsCombinations.tree_different_ingredients, len(IngredientsCombinations.tree_different_ingredients)],
    ])
    def test_add_ingredient(self, mock_ingredients, expected_len):
        burger = Burger()
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == expected_len and burger.ingredients == mock_ingredients

    @allure.title('Проверка метода remove_ingredient')
    @allure.description('Проверяем, что метод remove_ingredient корректно удаляет ингредиент из атрибута ingredients')
    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.ingredients.append(mock_sauce)
        burger.ingredients.append(mock_filling)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1 and burger.ingredients == [mock_sauce]

    @allure.title('Проверка метода remove_ingredient: удаление двух ингредиентов')
    @allure.description('Проверяем, что метод remove_ingredient корректно удаляет 2 ингредиента из атрибута ingredients')
    def test_remove_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.ingredients.append(mock_sauce)
        burger.ingredients.append(mock_filling)
        burger.remove_ingredient(0)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0 and burger.ingredients == []

    @allure.title('Проверка метода move_ingredient')
    @allure.description('Проверить, что метод move_ingredient корректно меняет порядок ингредиентов')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.ingredients.append(mock_sauce)
        burger.ingredients.append(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @allure.title('Проверка метода get_price')
    @allure.description(
        'Проверяем, что метод get_price корректно возвращает цену бургера в зависимости от передаваемых ингредиентов')
    @pytest.mark.parametrize('bun, ingredients, expected_price', burgers_variants)
    def test_get_price(self, bun, ingredients, expected_price):
        burger = Burger()
        burger.bun = bun
        burger.ingredients = ingredients
        assert burger.get_price() == expected_price

    @allure.title('Проверка метода get_receipt')
    @allure.description(
        'Проверяем, что метод get_receipt корректно возвращает чек бургера в зависимости от передаваемых ингредиентов')
    @pytest.mark.parametrize('ingredients', [
        IngredientsCombinations.only_sauce,
        IngredientsCombinations.only_filling,
        IngredientsCombinations.two_same_sauces,
        IngredientsCombinations.two_same_fillings,
        IngredientsCombinations.tree_different_ingredients,
    ])
    def test_get_receipt(self, mock_bun, ingredients):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = ingredients
        assert burger.get_receipt() == BurgerReceipt.get_receipt(mock_bun, ingredients)