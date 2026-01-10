from database import Database
import allure


class TestDatabase:

    @allure.title('Получение количества булочек в базе через метод available_buns')
    def test_available_buns(self):
        database = Database()

        assert len(database.available_buns()) == 3

    @allure.title('Получение количества ингредиентов в базе через метод available_ingredients')
    def test_available_ingredients(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
