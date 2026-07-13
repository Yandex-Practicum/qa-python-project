from praktikum.database import Database

def test_database_contains_buns():
    database = Database()
    buns = database.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"

def test_database_contains_ingredients():
    database = Database()
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
