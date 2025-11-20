import allure

from praktikum.database import Database


class TestDatabase:
    @allure.title('Проверка доступных булок')
    def test_available_buns_buns_count(self):
        data_base = Database()
        assert len(data_base.available_buns()) == 3

    @allure.title('Проверка доступных ингредиентов')
    def test_available_ingredients_ingredients_count(self):
        data_base = Database()
        assert len(data_base.available_ingredients()) == 6


