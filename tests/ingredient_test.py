from unittest.mock import Mock

import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # тест проверяет, что при запросе цены ингредиента в ответе приходит корректное значение
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_price',
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 9.0, 9.0),
            (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 2.75, 2.75),
            (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 0.5, 0.5),
            (INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 4.2, 4.2),
        ],
        ids=['Sauce price 1',
             'Filling price 1',
             'Sauce price 2',
             'Filling price 2']
    )
    def test_get_price(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price

    # тест проверяет, что при запросе названия ингредиента в ответе приходит корректное значение
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_name',
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 1.5, 'Соус традиционный галактический'),
            (INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 2.75,
             'Филе Люминесцентного тетраодонтимформа'),
            (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 10.5,
             'Соус с шипами Антарианского плоскоходца'),
            (INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 4.2, 'Хрустящие минеральные кольца'),
        ],
        ids=['Sauce price 1',
             'Filling price 1',
             'Sauce price 2',
             'Filling price 2']
    )
    def test_get_name(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    # тест проверяет, что при запросе типа ингредиента в ответе приходит корректное значение
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_type',
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 1.0, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерева', 9.75, INGREDIENT_TYPE_FILLING),
            (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 0.5, INGREDIENT_TYPE_SAUCE),
            (INGREDIENT_TYPE_FILLING, 'Кристаллы марсианских альфа-сахаридов', 5.5, INGREDIENT_TYPE_FILLING),
        ],
        ids=['Sauce price 1',
             'Filling price 1',
             'Sauce price 2',
             'Filling price 2']
    )
    def test_get_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

    # тест проверяет, что при использовании мока цены ингредиента в ответе приходит корректное значение
    def test_get_price_mock(self):
        ingredient = Mock()
        ingredient.get_price.return_value = 11.7
        result = ingredient.get_price()
        assert result == 11.7

    # тест проверяет, что при использовании мока названия ингредиента в ответе приходит корректное значение
    def test_get_name_mock(self):
        ingredient = Mock()
        ingredient.get_name.return_value = 'Mocked ingredient'
        result = ingredient.get_name()
        assert result == 'Mocked ingredient'

    # тест проверяет, что при использовании мока типа ингредиента в ответе приходит корректное значение
    def test_get_type_mock(self):
        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        result = ingredient.get_type()
        assert result == INGREDIENT_TYPE_FILLING
