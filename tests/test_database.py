import pytest
import allure

from conftest import new_database

@allure.suite('Тесты класса "database"')
class TestDatabase:

    @allure.title('Проверка возвращения корректного типа и длины списка "available_buns"')
    def test_available_buns_return_correct_list(self, new_database):
        bun_list = new_database.available_buns()
        assert type(bun_list) == list and len(bun_list) == 3

    @allure.title('Проверка возвращения корректного типа и длины списка "available_ingredients"')
    def test_available_ingredients_return_correct_list(self, new_database):
        ingredient_list = new_database.available_ingredients()
        assert type(ingredient_list) == list and len(ingredient_list) == 6



