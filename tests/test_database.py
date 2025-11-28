import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_initialization_creates_data(self):
        """Тест инициализации базы данных создает данные"""
        database = Database()

        # Проверяем, что булочки созданы
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

        # Проверяем типы объектов
        assert all(isinstance(bun, Bun) for bun in database.buns)
        assert all(isinstance(ing, Ingredient) for ing in database.ingredients)

    def test_available_buns_returns_correct_list(self):
        """Тест метода available_buns возвращает правильный список"""
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

        # Проверяем названия булочек
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients_returns_correct_list(self):
        """Тест метода available_ingredients возвращает правильный список"""
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

        # Проверяем типы и названия ингредиентов
        sauce_names = [ing.get_name() for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        filling_names = [ing.get_name() for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauce_names) == 3
        assert len(filling_names) == 3
        assert "hot sauce" in sauce_names
        assert "sour cream" in sauce_names
        assert "chili sauce" in sauce_names
        assert "cutlet" in filling_names
        assert "dinosaur" in filling_names
        assert "sausage" in filling_names

    def test_bun_prices_are_correct(self):
        """Тест цен булочек соответствуют ожидаемым"""
        database = Database()
        buns = database.available_buns()

        prices = [bun.get_price() for bun in buns]
        assert 100 in prices
        assert 200 in prices
        assert 300 in prices

    def test_ingredient_prices_are_correct(self):
        """Тест цен ингредиентов соответствуют ожидаемым"""
        database = Database()
        ingredients = database.available_ingredients()

        prices = [ing.get_price() for ing in ingredients]
        # Проверяем, что все ожидаемые цены присутствуют
        assert 100 in prices
        assert 200 in prices
        assert 300 in prices

    def test_ingredient_types_are_correct(self):
        """Тест типов ингредиентов соответствуют ожидаемым"""
        database = Database()
        ingredients = database.available_ingredients()

        sauce_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING)

        assert sauce_count == 3
        assert filling_count == 3

    def test_database_returns_same_list_objects(self):
        """Тест что база данных возвращает те же объекты списков при многократном вызове"""
        database = Database()

        buns1 = database.available_buns()
        buns2 = database.available_buns()

        # В текущей реализации Database возвращает ссылки на одни и те же списки
        assert buns1 is buns2
        assert buns1 == buns2

    def test_database_returns_same_ingredients_objects(self):
        """Тест что база данных возвращает те же объекты списков ингредиентов"""
        database = Database()

        ingredients1 = database.available_ingredients()
        ingredients2 = database.available_ingredients()

        # В текущей реализации Database возвращает ссылки на одни и те же списки
        assert ingredients1 is ingredients2
        assert ingredients1 == ingredients2

    def test_database_data_is_mutable(self):
        """Тест что данные базы можно изменять через возвращаемые списки"""
        database = Database()

        # Получаем исходные данные
        original_buns_count = len(database.available_buns())
        original_ingredients_count = len(database.available_ingredients())

        # Получаем списки (это ссылки на исходные данные)
        buns = database.available_buns()
        ingredients = database.available_ingredients()

        # Изменяем полученные списки
        buns.clear()
        ingredients.clear()

        # Проверяем что исходные данные изменились
        assert len(database.available_buns()) == 0
        assert len(database.available_ingredients()) == 0

    def test_database_contains_correct_bun_objects(self):
        """Тест что база содержит правильные объекты булочек"""
        database = Database()
        buns = database.available_buns()

        # Проверяем конкретные объекты булочек
        found_black_bun = False
        found_white_bun = False
        found_red_bun = False

        for bun in buns:
            name = bun.get_name()
            price = bun.get_price()

            if name == "black bun" and price == 100:
                found_black_bun = True
            elif name == "white bun" and price == 200:
                found_white_bun = True
            elif name == "red bun" and price == 300:
                found_red_bun = True

        assert found_black_bun, "Black bun not found or has wrong price"
        assert found_white_bun, "White bun not found or has wrong price"
        assert found_red_bun, "Red bun not found or has wrong price"

    def test_database_contains_correct_ingredient_objects(self):
        """Тест что база содержит правильные объекты ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()

        # Проверяем конкретные объекты ингредиентов
        expected_ingredients = {
            ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
            ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
            ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
            ("cutlet", INGREDIENT_TYPE_FILLING, 100),
            ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
            ("sausage", INGREDIENT_TYPE_FILLING, 300),
        }

        found_ingredients = set()
        for ingredient in ingredients:
            found_ingredients.add((
                ingredient.get_name(),
                ingredient.get_type(),
                ingredient.get_price()
            ))

        assert found_ingredients == expected_ingredients, f"Expected {expected_ingredients}, but found {found_ingredients}"