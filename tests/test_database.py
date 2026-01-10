from praktikum.database import Database


def test_database_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"


def test_database_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
