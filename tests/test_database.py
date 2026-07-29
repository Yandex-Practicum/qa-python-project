from praktikum.database import Database

class TestDatabase:

    def test_available_buns_returns_all_buns(self):
        database = Database()
        buns = database.available_buns()
        bun_names = [bun.get_name() for bun in buns]
        assert bun_names == [
            "black bun",
            "white bun",
            "red bun"
        ]

    def test_available_ingredients_returns_all_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        ingredient_names = [ingredient.get_name()for ingredient in ingredients]
        assert ingredient_names == [
            "hot sauce",
            "sour cream",
            "chili sauce",
            "cutlet",
            "dinosaur",
            "sausage"
        ]