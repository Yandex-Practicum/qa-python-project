from praktikum.database import Database

class TestDatabase:
    # Тестирование получения списка доступных булок
    def test_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        expected_names = ["black bun", "white bun", "red bun"]
        actual_names = [bun.get_name() for bun in available_buns]
        assert expected_names == actual_names

    # Тестирование получения списка доступных ингредиентов
    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        expected_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur","sausage"]
        actual_names = [ingredient.get_name() for ingredient in available_ingredients]
        assert expected_names == actual_names