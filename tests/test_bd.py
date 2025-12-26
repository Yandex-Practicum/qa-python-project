from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        self.db = Database()
        actual_result = [{"name": bun.name, "price": bun.price} for bun in self.db.available_buns()]
        expected_result = [
            {"name": "black bun", "price": 100},
            {"name": "white bun", "price": 200},
            {"name": "red bun", "price": 300}
        ]

        assert actual_result == expected_result

    def test_available_ingredients(self):
        self.db = Database()
        expected_ingredients = [
            {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
            {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
            {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
            {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
            {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
            {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300}
        ]
        actual_ingredients = [{"type": ingredient.type, "name": ingredient.name, "price": ingredient.price} for
                              ingredient in self.db.available_ingredients()]

        assert actual_ingredients == expected_ingredients