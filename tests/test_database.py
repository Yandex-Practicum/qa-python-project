from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDataBase:

    # Тест init
    def test_database_initialization(self):
        database = Database()
        assert isinstance(database.buns, list)
        assert len(database.buns) == 3
        assert isinstance(database.ingredients, list)
        assert len(database.ingredients) == 6

    # Тест метода available_buns
    def test_get_available_buns(self):
        database = Database()
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    # Тест метода available_ingredients
    def test_get_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert len(available_ingredients) == 6

    # Проверка содержимого списка булочек(название и стоимость)
    def test_database_buns_content(self):
        database = Database()
        expected_buns = [("black bun", 100), ("white bun", 200), ("red bun", 300)]
        actual_buns = [(b.get_name(), b.get_price()) for b in database.buns]
        assert actual_buns == expected_buns


    # Проверка содержимого списка ингредиентов(название и стоимость)
    def test_database_ingredients_content(self):
        database = Database()
        expected_ingredients = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

        actual_ingredients = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in database.ingredients
        ]

        assert actual_ingredients == expected_ingredients
