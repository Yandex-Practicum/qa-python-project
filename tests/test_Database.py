from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_available_buns(sample_database):
    buns = sample_database.available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)

def test_available_ingredients(sample_database):
    ingredients = sample_database.available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)