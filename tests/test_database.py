import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_database_initialization():
    """Тест инициализации базы данных"""
    db = Database()
    assert len(db.available_buns()) == 3
    assert len(db.available_ingredients()) == 6

@pytest.mark.parametrize("index,expected_name", [
    (0, "black bun"),
    (1, "white bun"),
    (2, "red bun")
])
def test_available_buns(index, expected_name):
    """Параметризованный тест доступных булочек"""
    db = Database()
    buns = db.available_buns()
    assert buns[index].get_name() == expected_name

@pytest.mark.parametrize("index,expected_type,expected_name", [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce"),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce"),
    (3, INGREDIENT_TYPE_FILLING, "cutlet"),
    (5, INGREDIENT_TYPE_FILLING, "sausage")
])
def test_available_ingredients(index, expected_type, expected_name):
    """Параметризованный тест доступных ингредиентов"""
    db = Database()
    ingredients = db.available_ingredients()
    assert ingredients[index].get_type() == expected_type
    assert ingredients[index].get_name() == expected_name