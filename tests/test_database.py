from unittest.mock import patch

from praktikum.database import Database


class TestDatabase:

    # Тестируем метод _init_ создание БД
    def test_init_database_got_database_not_empty(self):
        database = Database()
        assert len(database.buns) > 0 and len(database.ingredients) > 0

    @patch('praktikum.database.Database.available_buns')
    def test_available_buns_got_list_buns(self, mock_available_buns, bun):
        mock_available_buns.return_value = bun

        assert Database.available_buns() == bun
        mock_available_buns.assert_called()

    @patch('praktikum.database.Database.available_ingredients')
    def test_available_ingredients_got_list_ingredients(self, mock_available_ingredients, ingredients):
        mock_available_ingredients.return_value = ingredients

        assert Database.available_ingredients() == ingredients
        mock_available_ingredients.assert_called()
