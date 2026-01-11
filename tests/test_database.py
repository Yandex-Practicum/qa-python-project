import pytest
from praktikum.database import Database

class TestDatabase:
    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_bun_data(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

