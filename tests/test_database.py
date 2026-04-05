from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    def test_available_buns_returns_list(self):
        db = Database()
        assert isinstance(db.available_buns(), list)

    def test_available_buns_not_empty(self):
        db = Database()
        assert len(db.available_buns()) > 0

    def test_available_buns_contains_bun_instances(self):
        db = Database()
        for bun in db.available_buns():
            assert isinstance(bun, Bun)

    def test_available_ingredients_returns_list(self):
        db = Database()
        assert isinstance(db.available_ingredients(), list)

    def test_available_ingredients_not_empty(self):
        db = Database()
        assert len(db.available_ingredients()) > 0

    def test_available_ingredients_contains_ingredient_instances(self):
        db = Database()
        for ingredient in db.available_ingredients():
            assert isinstance(ingredient, Ingredient)
