from database import Database


def test_available_buns_returns_buns():
    db = Database()
    buns = db.available_buns()

    assert len(buns) == 3


def test_available_ingredients_returns_ingredients():
    db = Database()
    ingredients = db.available_ingredients()

    assert len(ingredients) == 6