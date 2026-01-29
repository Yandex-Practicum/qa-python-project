from database import Database
from bun import Bun
from ingredient import Ingredient


def test_database_configuration():
    database = Database()

    assert len(database.available_buns()) == 3
    assert len(database.available_ingredients()) == 6
    assert isinstance(database.available_buns()[0], Bun)
    assert isinstance(database.available_ingredients()[0], Ingredient)

def test_available_buns():

    database = Database()
    buns = database.available_buns()

    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[1].get_name() == "white bun"
    assert buns[1].get_price() == 200
    assert buns[2].get_name() == "red bun"
    assert buns[2].get_price() == 300

def test_available_ingredients():

    database = Database()
    ingredients = database.available_ingredients()

    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[1].get_name() == "sour cream"
    assert ingredients[2].get_name() == "chili sauce"
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[4].get_name() == "dinosaur"
    assert ingredients[5].get_name() == "sausage"
    assert ingredients[0].get_price() == 100
    assert ingredients[1].get_price() == 200
    assert ingredients[2].get_price() == 300
    assert ingredients[3].get_price() == 100
    assert ingredients[4].get_price() == 200
    assert ingredients[5].get_price() == 300
