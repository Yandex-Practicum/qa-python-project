import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.test_constants import (
    BUN_BLACK, BUN_WHITE, BUN_RED,
    PRICE_100, PRICE_200, PRICE_300,
    INGREDIENT_HOT_SAUCE, INGREDIENT_SOUR_CREAM, INGREDIENT_CHILI_SAUCE,
    INGREDIENT_CUTLET, INGREDIENT_DINOSAUR, INGREDIENT_SAUSAGE
)


class TestDatabase:
    # Тесты для класса Database.

    def test_database_initialization(self):
        # Проверка инициализации базы данных.
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_available_buns(self):
        # Проверка получения доступных булочек.
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == BUN_BLACK
        assert buns[1].get_name() == BUN_WHITE
        assert buns[2].get_name() == BUN_RED

    def test_available_ingredients(self):
        # Проверка получения доступных ингредиентов.
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
        # Проверка соусов
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == INGREDIENT_HOT_SAUCE
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == INGREDIENT_SOUR_CREAM
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == INGREDIENT_CHILI_SAUCE
        # Проверка начинок
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == INGREDIENT_CUTLET
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == INGREDIENT_DINOSAUR
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == INGREDIENT_SAUSAGE

    def test_bun_prices(self):
        # Проверка цен булочек.
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_price() == PRICE_100
        assert buns[1].get_price() == PRICE_200
        assert buns[2].get_price() == PRICE_300

    def test_ingredient_prices(self):
        # Проверка цен ингредиентов.
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[0].get_price() == PRICE_100
        assert ingredients[1].get_price() == PRICE_200
        assert ingredients[2].get_price() == PRICE_300
        assert ingredients[3].get_price() == PRICE_100
        assert ingredients[4].get_price() == PRICE_200
        assert ingredients[5].get_price() == PRICE_300

    @pytest.mark.parametrize("bun_index,expected_name,expected_price", [
        (0, BUN_BLACK, PRICE_100),
        (1, BUN_WHITE, PRICE_200),
        (2, BUN_RED, PRICE_300),
    ])
    def test_buns_parametrized(self, bun_index, expected_name, expected_price):
        # Параметризованная проверка булочек.
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns[bun_index], Bun)
        assert buns[bun_index].get_name() == expected_name
        assert buns[bun_index].get_price() == expected_price

    @pytest.mark.parametrize("ingredient_index,expected_type,expected_name", [
        (0, INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE, INGREDIENT_SOUR_CREAM),
        (2, INGREDIENT_TYPE_SAUCE, INGREDIENT_CHILI_SAUCE),
        (3, INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET),
        (4, INGREDIENT_TYPE_FILLING, INGREDIENT_DINOSAUR),
        (5, INGREDIENT_TYPE_FILLING, INGREDIENT_SAUSAGE),
    ])
    def test_ingredients_parametrized(self, ingredient_index, expected_type, expected_name):
        # Параметризованная проверка ингредиентов.
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients[ingredient_index], Ingredient)
        assert ingredients[ingredient_index].get_type() == expected_type
        assert ingredients[ingredient_index].get_name() == expected_name
