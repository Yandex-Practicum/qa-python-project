class TestDatabase:
    def test_available_buns(self, database):
        available_buns = database.available_buns()
        expected_names = ["black bun", "white bun", "red bun"]
        assert [bun.get_name() for bun in available_buns] == expected_names

    def test_available_ingredients(self, database):
        available_ingredients = database.available_ingredients()
        expected_names = [
            "hot sauce", "sour cream", "chili sauce",
            "cutlet", "dinosaur", "sausage"
        ]
        assert [ingredient.get_name() for ingredient in available_ingredients] == expected_names




