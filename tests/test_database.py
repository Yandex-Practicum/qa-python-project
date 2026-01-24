# tests/test_database.py
import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тестирование получения доступных булочек
def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3  # Проверяем, что добавлено 3 булочки
    assert buns[0].get_name() == "black bun"  # Проверяем первую булочку
    assert buns[1].get_price() == 200  # Проверяем цену второй булочки

# Тестирование получения доступных ингредиентов
@pytest.mark.parametrize("expected_count", [6])  # Ожидаем 6 ингредиентов
def test_available_ingredients(expected_count):
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == expected_count  # Проверяем общее количество ингредиентов