from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        expected_result = ["black bun", "white bun", "red bun"]
        bun_names_list = [bun.get_name() for bun in available_buns]
        assert bun_names_list == expected_result

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        expected_result = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        ingredient_names_list = [ingredient.get_name() for ingredient in available_ingredients]
        assert ingredient_names_list == expected_result
