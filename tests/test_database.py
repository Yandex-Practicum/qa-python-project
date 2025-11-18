import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    # Тест на получение доступных булочек')
    def test_get_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    # Тест на получение доступных ингредиентов
    def test_get_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert len(available_ingredients) == 6

    # Тест на получение доступных соусов
    @pytest.mark.parametrize('ingredient_index', [0, 1, 2])
    def test_available_ingredients_sauce_type(self, ingredient_index):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[ingredient_index].get_type() == INGREDIENT_TYPE_SAUCE

    # Тест на получение доступных начинок
    @pytest.mark.parametrize('ingredient_index', [3, 4, 5])
    def test_available_ingredients_filling_type(self, ingredient_index):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[ingredient_index].get_type() == INGREDIENT_TYPE_FILLING

    # Тест на получение цен на ингредиенты
    def test_get_available_ingredients_prices(self):
        database = Database()
        ingredients = database.available_ingredients()
        hot_sauce_price = ingredients[0].get_price()
        assert hot_sauce_price == 100