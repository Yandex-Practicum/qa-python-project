import allure
from unittest.mock import patch
from helpers.create_objects import create_database


@allure.story('Проверка класса Database')
class TestDatabase:
    @allure.title('Проверка создания объекта Database')
    @allure.description('В self.buns и self.ingredients добавляются объекты Bun и Ingredient, указанные в __init__')
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_creation_object_database(self, mock_ingredient, mock_bun):
        new_database = create_database()
        assert len(new_database.ingredients) == 6 and len(new_database.buns) == 3

    @allure.title('Проверка метода available_buns()')
    @allure.description('Метод available_buns() возвращает self.buns')
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_available_buns(self, mock_ingredient, mock_bun):
        new_database = create_database()
        assert new_database.available_buns() == new_database.buns

    @allure.title('Проверка метода available_ingredients()')
    @allure.description('Метод available_ingredients() возвращает self.ingredients')
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_available_ingredients(self, mock_ingredient, mock_bun):
        new_database = create_database()
        assert new_database.available_ingredients() == new_database.ingredients
