import allure
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger


class TestDatabase:

    def setup_method(self):
        self.database = Database()
        self.buns = self.database.available_buns()
        self.ingredients = self.database.available_ingredients()

    @allure.title("Проверка, что available_buns возвращает непустой список")
    def test_available_buns_not_empty(self):
        assert len(self.buns) > 0

    @allure.title("Проверка, что available_buns возвращает список объектов Bun")
    def test_available_buns_returns_bun_objects(self):
        assert all(isinstance(item, Bun) for item in self.buns)

    @allure.title("Проверка, что available_ingredients возвращает непустой список")
    def test_available_ingredients_not_empty(self):
        assert len(self.ingredients) > 0

    @allure.title("Проверка, что available_ingredients возвращает список объектов Ingredient")
    def test_available_ingredients_returns_ingredient_objects(self):
        assert all(isinstance(item, Ingredient) for item in self.ingredients)

    @allure.title("Проверка, что available_ingredients возвращает ингредиенты всех типов")
    def test_available_ingredients_contains_all_types(self):
        types = {ingredient.type for ingredient in self.ingredients}
        assert INGREDIENT_TYPE_SAUCE in types and INGREDIENT_TYPE_FILLING in types

    @allure.title("Проверка корректности имён ингредиентов")
    def test_ingredients_have_valid_names(self):
        assert all(
            isinstance(ingredient.name, str) and len(ingredient.name) > 0
            for ingredient in self.ingredients
        )

    @allure.title("Проверка корректности цен ингредиентов")
    def test_ingredients_have_positive_prices(self):
        assert all(
            isinstance(ingredient.price, (int, float)) and ingredient.price > 0
            for ingredient in self.ingredients
        )

    @allure.title("Проверка корректности типов ингредиентов")
    def test_ingredients_have_valid_types(self):
        valid_types = {INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING}
        assert all(ingredient.type in valid_types for ingredient in self.ingredients)

    @allure.title("Проверка взаимодействия с бизнес‑логикой: создание бургера")
    def test_burger_creation_with_database_methods(self):
        selected_bun = self.buns[0]
        filling = next(i for i in self.ingredients if i.type == INGREDIENT_TYPE_FILLING)
        sauce = next(i for i in self.ingredients if i.type == INGREDIENT_TYPE_SAUCE)

        burger = Burger()
        burger.set_buns(selected_bun)
        burger.add_ingredient(filling)
        burger.add_ingredient(sauce)

        total_price = burger.get_price()
        expected_price = (selected_bun.get_price() * 2) + filling.get_price() + sauce.get_price()
        assert total_price == expected_price
