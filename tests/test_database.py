from praktikum.database import Database
import allure


class TestDatabase:
    @allure.title('Проверяем список булок')
    def test_available_bun(self):
        database = Database()
        assert len(database.available_buns()) == 3

    @allure.title('Проверяем список ингредиентов')
    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
        