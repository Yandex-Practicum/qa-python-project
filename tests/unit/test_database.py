from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_database_available_lists(monkeypatch):
    monkeypatch.setattr(Database, "available_buns", lambda self: [Bun("black bun", 100.0)])
    monkeypatch.setattr(Database, "available_ingredients", lambda self: [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0),
        Ingredient(INGREDIENT_TYPE_FILLING, "lettuce", 20.0),
    ])
    db = Database()
    buns = db.available_buns()
    ingredients = db.available_ingredients()
    assert isinstance(buns, list)
    assert len(buns) == 1
    assert isinstance(buns[0], Bun)
    assert isinstance(ingredients, list)
    assert len(ingredients) == 2
    assert all(isinstance(i, Ingredient) for i in ingredients)