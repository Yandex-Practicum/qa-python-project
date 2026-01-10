from unittest.mock import patch
from data import Data
from praktikum.database import Database


class TestDatabase:
    # Проверка, что БД наполняет список булок 3 элементами и список ингридиентов 6 элементами
    @patch("praktikum.bun.Bun")
    @patch("praktikum.ingredient.Ingredient")
    def test_database_init_three_buns_and_six_ingredients(self, mock_bun, mock_ingredient):
        database = Database()

        assert len(database.buns) == 3 and len(database.ingredients) == 6

    # Проверка, что в список булок добавляются булки с верными названиями и ценами
    @patch("praktikum.bun.Bun")
    def test_database_init_correct_buns_name_and_price(self, mock_bun):
        database = Database()
        for i, bun_data in enumerate(Data.buns):
            assert database.buns[i].name == bun_data.get("name") and database.buns[i].price == bun_data.get("price")

    # Проверка, что в список ингредиентов добавляются ингредиенты с верными типами, названиями и ценами
    @patch("praktikum.ingredient.Ingredient")
    def test_database_init_correct_ingredients_type_and_name_and_price(self, mock_ingredient):
        database = Database()
        for i, ing_data in enumerate(Data.ingredients):
            assert database.ingredients[i].type == ing_data.get("type") \
                   and database.ingredients[i].name == ing_data.get("name") \
                   and database.ingredients[i].price == ing_data.get("price")

    # Проверка, что метод возвращает верное количество булок
    @patch("praktikum.bun.Bun")
    def test_available_buns_return_tree_objects(self, mock_bun):
        database = Database()
        result = database.available_buns()

        assert len(result) == 3

    # Проверка, что метод возвращает верное количество ингредиентов
    @patch("praktikum.ingredient.Ingredient")
    def test_available_ingredients_return_six_objects(self, mock_ingredient):
        database = Database()
        result = database.available_ingredients()

        assert len(result) == 6
