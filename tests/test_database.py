import allure
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    @allure.title("Проверка, что available_buns возвращает непустой список")
    def test_available_buns_not_empty(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) > 0

    @allure.title("Проверка, что available_buns возвращает список объектов Bun")
    def test_available_buns_returns_bun_objects(self):
        database = Database()
        buns = database.available_buns()
        assert all(isinstance(bun, Bun) for bun in buns)

    @allure.title("Проверка, что available_ingredients возвращает список с ингредиентами всех типов")
    def test_available_ingredients_contains_all_types(self):
        database = Database()
        ingredients = database.available_ingredients()
        types = {ingredient.type for ingredient in ingredients}
        assert INGREDIENT_TYPE_SAUCE in types and INGREDIENT_TYPE_FILLING in types

    @allure.title("Проверка уникальности имён ингредиентов в базе данных")
    def test_available_ingredients_unique_names(self):
        database = Database()
        ingredients = database.available_ingredients()
        names = [ingredient.name for ingredient in ingredients]
        assert len(names) == len(set(names))

    @allure.title("Проверка, что все ингредиенты в списке имеют корректные типы")
    def test_ingredients_have_valid_types(self):
        database = Database()
        ingredients = database.available_ingredients()
        valid_types = {INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING}
        assert all(ingredient.type in valid_types for ingredient in ingredients)

    @allure.title("Проверка цен ингредиентов")
    def test_ingredients_prices_correct(self):
        database = Database()
        ingredients = database.available_ingredients()
        expected_prices = {
            "hot sauce": 100,
            "sour cream": 200,
            "chili sauce": 300,
            "cutlet": 100,
            "dinosaur": 200,
            "sausage": 300
        }
        for ingredient in ingredients:
            assert ingredient.price == expected_prices[ingredient.name]

    @allure.title("Проверка цен ингредиентов без привязки")
    def test_ingredients_prices_positive(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert all(ingredient.price > 0 for ingredient in ingredients)

