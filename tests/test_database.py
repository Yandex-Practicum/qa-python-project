import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


@pytest.mark.parametrize("index, expected_name, expected_price", [
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300),
])
def test_available_buns(index, expected_name, expected_price):
    db = Database()
    buns = db.available_buns()

    assert len(buns) == 3 and buns[index].name == expected_name and buns[index].price == expected_price


@pytest.mark.parametrize("index, expected_type, expected_name, expected_price", [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
])
def test_available_ingredients(index, expected_type, expected_name, expected_price):
    db = Database()
    ingredients = db.available_ingredients()

    assert len(ingredients) == 6 and ingredients[index].type == expected_type and ingredients[index].name == expected_name and ingredients[index].price == expected_price