import pytest
from database import Database

class TestDatabase:
    @pytest.fixture
    def db(self):
        return Database()

    @pytest.mark.parametrize("expected_bun_names", [
        (["black bun", "white bun", "red bun"])
    ])
    def test_available_buns(self, db, expected_bun_names):
        buns = db.available_buns()
        bun_names = [bun.name for bun in buns]
        assert bun_names == expected_bun_names

    @pytest.mark.parametrize("expected_ingredient_names", [
        (["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"])
    ])
    def test_available_ingredients(self, db, expected_ingredient_names):
        ingredients = db.available_ingredients()
        ingredient_names = [ingredient.name for ingredient in ingredients]
        assert ingredient_names == expected_ingredient_names