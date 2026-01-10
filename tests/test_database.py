import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        # Проверяем количество булочек
        assert len(buns) == 3
        # Проверяем, что элементы являются экземплярами Bun
        assert all(isinstance(bun, Bun) for bun in buns)
        # Проверяем первую булочку
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        # Проверяем количество ингредиентов
        assert len(ingredients) == 6
        # Проверяем, что элементы являются экземплярами Ingredient
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        # Проверяем первый соус
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100