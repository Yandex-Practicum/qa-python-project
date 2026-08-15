import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_initialization(self):
        db = Database()
        # Проверяем, что булочки созданы (их 3)
        assert len(db.buns) == 3
        # Проверяем, что ингредиенты созданы (их 6)
        assert len(db.ingredients) == 6

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        # Проверим первые три соуса
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        # Проверим первые три начинки (индексы 3,4,5)
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
