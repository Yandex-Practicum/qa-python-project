from database import Database


def test_available_buns_returns_three_items():
    database = Database()
    buns = database.available_buns()

    assert len(buns) == 3


def test_available_buns_returns_expected_bun_names():
    database = Database()
    buns = database.available_buns()

    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"


def test_available_buns_contains_expected_bun_price():
    database = Database()
    buns = database.available_buns()

    assert buns[1].get_price() == 200


def test_available_ingredients_returns_six_items():
    database = Database()
    ingredients = database.available_ingredients()

    assert len(ingredients) == 6


def test_available_ingredients_returns_sauce_and_filling_types():
    database = Database()
    ingredients = database.available_ingredients()

    assert {ingredient.get_type() for ingredient in ingredients} == {"SAUCE", "FILLING"}


def test_available_ingredients_contains_cutlet():
    database = Database()
    ingredients = database.available_ingredients()

    assert any(ingredient.get_name() == "cutlet" for ingredient in ingredients)
