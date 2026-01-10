import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_initialization(self):
        """Тест инициализации базы данных"""
        db = Database()

        # Проверяем, что булки созданы
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

        # Проверяем, что ингредиенты созданы
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    @pytest.mark.parametrize("expected_name,expected_price,index", [
        ("black bun", 100, 0),
        ("white bun", 200, 1),
        ("red bun", 300, 2),
    ])
    def test_available_buns_parameterized(self, expected_name, expected_price, index):
        """Параметризованный тест проверки булок в базе данных"""
        db = Database()
        buns = db.available_buns()

        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize("expected_type,expected_name,expected_price,index", [
        # Соусы
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 0),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200, 1),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, 2),
        # Начинки
        (INGREDIENT_TYPE_FILLING, "cutlet", 100, 3),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200, 4),
        (INGREDIENT_TYPE_FILLING, "sausage", 300, 5),
    ])
    def test_available_ingredients_parameterized(self, expected_type, expected_name, expected_price, index):
        """Параметризованный тест проверки ингредиентов в базе данных"""
        db = Database()
        ingredients = db.available_ingredients()

        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price