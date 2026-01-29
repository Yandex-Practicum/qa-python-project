# test_database.py

import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabaseStructure:
    """Проверка структуры базы данных"""

    def test_buns_list_exists(self, initialized_database):
        """Проверка существования списка булочек"""
        assert hasattr(initialized_database, 'buns')

    def test_ingredients_list_exists(self, initialized_database):
        """Проверка существования списка ингредиентов"""
        assert hasattr(initialized_database, 'ingredients')


class TestDatabaseInitialData:
    """Проверка начальных данных"""

    def test_initial_buns_count(self, initialized_database):
        """Проверка количества булочек"""
        assert len(initialized_database.available_buns()) == 3

    def test_initial_ingredients_count(self, initialized_database):
        """Проверка количества ингредиентов"""
        assert len(initialized_database.available_ingredients()) == 6


class TestBunProperties:
    """Проверка свойств булочек"""

    @pytest.mark.parametrize("index, expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun")
    ])
    def test_bun_name(self, initialized_database, index, expected_name):
        """Проверка названия булочки"""
        assert initialized_database.available_buns()[index].get_name() == expected_name

    @pytest.mark.parametrize("index, expected_price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_bun_price(self, initialized_database, index, expected_price):
        """Проверка цены булочки"""
        assert initialized_database.available_buns()[index].get_price() == expected_price


class TestIngredientProperties:
    """Проверка свойств ингредиентов"""

    @pytest.mark.parametrize("index, expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING)
    ])
    def test_ingredient_type(self, initialized_database, index, expected_type):
        """Проверка типа ингредиента"""
        assert initialized_database.available_ingredients()[index].get_type() == expected_type

    @pytest.mark.parametrize("index, expected_name", [
        (0, "hot sauce"),
        (1, "sour cream")
    ])
    def test_ingredient_name(self, initialized_database, index, expected_name):
        """Проверка названия ингредиента"""
        assert initialized_database.available_ingredients()[index].get_name() == expected_name


class TestDatabaseEdgeCases:
    """Проверка граничных случаев"""

    def test_empty_database_buns(self, empty_database):
        """Проверка пустого списка булочек"""
        assert len(empty_database.available_buns()) == 0

    def test_empty_database_ingredients(self, empty_database):
        """Проверка пустого списка ингредиентов"""
        assert len(empty_database.available_ingredients()) == 0


class TestMockFunctionality:
    """Проверка работы с mock-объектами"""

    def test_mock_bun_addition(self, empty_database, mock_bun):
        """Проверка добавления mock-булочки"""
        empty_database.buns.append(mock_bun)
        assert len(empty_database.available_buns()) == 1

    def test_mock_ingredient_addition(self, empty_database, mock_ingredient):
        """Проверка добавления mock-ингредиента"""
        empty_database.ingredients.append(mock_ingredient)
        assert len(empty_database.available_ingredients()) == 1