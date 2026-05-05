from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:
    def test_available_buns(self, database):
        assert len(database.available_buns()) == 3  

    def test_available_ingredients(self, database):
        assert len(database.available_ingredients()) == 6

    def test_database_buns_contains_expected_items(self, database):
        buns = database.available_buns()
        names = []
        for bun in buns:
            names.append(bun.get_name())

        assert "black bun" in names
        assert "white bun" in names      
        assert "red bun" in names

    def test_database_ingredients_contains_expected_items(self, database):
        ingredients = database.available_ingredients()
        names = []
        for ingredient in ingredients:
            names.append(ingredient.get_name())

        assert "cutlet" in names
        assert "dinosaur" in names      
        assert "sausage" in names

    def test_available_buns_returns_buns(self, database):
        buns = database.available_buns()

        for bun in buns:
            assert isinstance(bun, Bun)

    def test_available_ingredients_returns_ingredients(self, database):
        ingredients = database.available_ingredients()

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

