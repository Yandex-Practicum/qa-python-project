from database import Database


def test_database_returns_buns():
    database = Database()
    buns = database.available_buns()

    assert isinstance(buns, list)
    assert len(buns) > 0


def test_database_returns_ingredients():
    database = Database()
    ingredients = database.available_ingredients()

    assert isinstance(ingredients, list)
    assert len(ingredients) > 0
