from database import Database


class TestDatabase:

    def test_available_buns_success(self):
        test_database = Database()
        buns = test_database.available_buns()
        bun_names = []

        for bun in buns:
            bun_names.append(bun.get_name())

        assert bun_names == ["black bun", "white bun", "red bun"]
        assert len(buns) == 3

    def test_available_ingredients_success(self):
        test_database = Database()
        ingredients = test_database.available_ingredients()

        ingredients_names = []
        for ingredient in ingredients:
            ingredients_names.append(ingredient.get_name())

        assert ingredients_names == ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
