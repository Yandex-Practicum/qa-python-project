from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDataBase:
    def setup_method(self):
        self.data_base = Database()

    def test_available_buns(self):
        expected_buns_list = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        buns_list = self.data_base.available_buns()
        for expected, actual in zip(expected_buns_list, buns_list):
            assert expected.name == actual.name and expected.price == actual.price

    def test_test_available_ingredients(self):
        expected_ingredients_list = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
        ingredients_list = self.data_base.available_ingredients()
        for expected, actual in zip(expected_ingredients_list, ingredients_list):
            assert expected.name == actual.name and expected.price == actual.price
