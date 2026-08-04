from praktikum.database import Database


def test_available_buns_count():
    db = Database()
    assert len(db.available_buns()) == 3


def test_available_buns_content():
    db = Database()
    buns = db.available_buns()
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100


def test_available_ingredients_count():
    db = Database()
    assert len(db.available_ingredients()) == 6


def test_available_ingredients_sauce():
    db = Database()
    ingredients = db.available_ingredients()
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_type() == "SAUCE"


def test_available_ingredients_filling():
    db = Database()
    ingredients = db.available_ingredients()
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[3].get_type() == "FILLING"
