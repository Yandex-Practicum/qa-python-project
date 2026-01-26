import pytest
from praktikum.database import Database


class TestDatabase:
    @pytest.mark.parametrize("buns", [
        [("black bun", 100)],
        [("white bun", 200)],
        [("red bun", 300)]
    ])
    def test_available_buns(self, buns):
        db = Database()
        db.buns = buns
        available_buns = db.available_buns()
        assert available_buns == buns

    @pytest.mark.parametrize("ingredients_sauce", [
                             [("hot sauce", 100)],
                              [("sour cream", 200)],
                              [("chili sauce", 300)]
    ])

    def test_available_ingredients_sauce(self, ingredients_sauce):
        db = Database()
        db.ingredients = ingredients_sauce
        available_ingredients_sauce = db.available_ingredients()
        assert available_ingredients_sauce == ingredients_sauce


    @pytest.mark.parametrize("ingredients_filling", [
                             [("cutlet", 100)],
                              [("dinosaur", 200)],
                              [("sausage", 300)]
    ])

    def test_available_ingredients_sauce(self, ingredients_filling):
        db = Database()
        db.ingredients = ingredients_filling
        available_ingredients_filling = db.available_ingredients()
        assert available_ingredients_filling == ingredients_filling