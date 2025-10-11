import allure
import pytest

from praktikum.database import Database


class TestDatabase:
    @allure.title('Проверка списка булок')
    def test_bun_list(self):
        database = Database()
        bun_list = [bun.name for bun in database.available_buns()]
        assert bun_list == ["black bun", "white bun", "red bun"]

    @allure.title('Проверка списка ингредиентов')
    def test_ingredients_list(self):
        database = Database()
        ingredients_list = [ingredient.name for ingredient in database.available_ingredients()]
        assert ingredients_list == ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
