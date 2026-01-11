from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


def test_database_available_buns():
    buns = Database().available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)
    assert buns[0].get_name() == 'black bun'
    assert buns[0].get_price() == 100
    assert buns[1].get_name() == 'white bun'
    assert buns[1].get_price() == 200
    assert buns[2].get_name() == 'red bun'
    assert buns[2].get_price() == 300

def test_database_available_ingredients():
    ingredients = Database().available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)
    assert ingredients[0].get_name() == 'hot sauce'
    assert ingredients[0].get_price() == 100
    assert ingredients[1].get_name() == 'sour cream'
    assert ingredients[1].get_price() == 200
    assert ingredients[2].get_name() == 'chili sauce'
    assert ingredients[2].get_price() == 300
    assert ingredients[3].get_name() == 'cutlet'
    assert ingredients[3].get_price() == 100
    assert ingredients[4].get_name() == 'dinosaur'
    assert ingredients[4].get_price() == 200
    assert ingredients[5].get_name() == 'sausage'
    assert ingredients[5].get_price() == 300
