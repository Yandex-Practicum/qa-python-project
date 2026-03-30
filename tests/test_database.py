from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns_returns_list(self):
        """Проверяем, что available_buns возвращает список"""
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_not_empty(self):
        """Проверяем, что список булок не пустой"""
        db = Database()
        buns = db.available_buns()
        assert len(buns) > 0

    def test_available_buns_contains_bun_objects(self):
        """Проверяем, что в списке лежат объекты типа Bun"""
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_ingredients_returns_list(self):
        """Проверяем, что available_ingredients возвращает список"""
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_not_empty(self):
        """Проверяем, что список ингредиентов не пустой"""
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) > 0

    def test_available_ingredients_contains_ingredient_objects(self):
        """Проверяем, что в списке лежат объекты типа Ingredient"""
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
