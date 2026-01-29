import pytest

from praktikum.database import Database

class TestDatabase:
    def test_database(self):
        db = Database()
        buns = db.available_buns()
        b = ""
        for bun in buns:
            b = b + bun.get_name() + ", " + str(bun.get_price()) + "; "
        ingredients = db.available_ingredients()
        i = ""
        for ingredient in ingredients:
            i = i + ingredient.get_type() + ", " + ingredient.get_name() + ", " + str(ingredient.get_price()) + "; "
        assert b == "black bun, 100; white bun, 200; red bun, 300; " and i == "SAUCE, hot sauce, 100; SAUCE, sour cream, 200; SAUCE, chili sauce, 300; FILLING, cutlet, 100; FILLING, dinosaur, 200; FILLING, sausage, 300; "
