import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_available_buns(db):
    """Тестируем метод available_buns в мокированном экземпляре базы данных."""
    buns = db.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[-1].get_name() == "red bun"
    assert buns[-1].get_price() == 300

def test_available_ingredients(db):
    """Тестируем метод available_ingredients в мокированном экземпляре базы данных."""
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_price() == 100
    assert ingredients[-1].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[-1].get_name() == "sausage"
    assert ingredients[-1].get_price() == 300

