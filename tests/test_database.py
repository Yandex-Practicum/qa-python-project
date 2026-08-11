from database import Database


def test_available_buns_returns_three_buns():
    database = Database()
    buns = database.available_buns()

    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_price() == 200


def test_available_ingredients_returns_sauce_and_filling():
    database = Database()
    ingredients = database.available_ingredients()

    assert len(ingredients) == 6
    assert {ingredient.get_type() for ingredient in ingredients} == {"SAUCE", "FILLING"}
    assert any(ingredient.get_name() == "cutlet" for ingredient in ingredients)
