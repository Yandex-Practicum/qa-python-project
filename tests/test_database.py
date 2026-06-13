from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_available_buns_returns_expected_buns():
    database = Database()

    buns = database.available_buns()

    assert len(buns) == 3
    assert [(bun.get_name(), bun.get_price()) for bun in buns] == [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ]


def test_available_ingredients_returns_expected_ingredients():
    database = Database()

    ingredients = database.available_ingredients()

    assert len(ingredients) == 6
    assert [
        (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
        for ingredient in ingredients
    ] == [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
