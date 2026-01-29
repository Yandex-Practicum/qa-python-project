from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def compare_bun_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for obj1, obj2 in zip(list1, list2):
        if obj1.name != obj2.name or obj1.price != obj2.price:
            return False
    return True


def compare_ingredients_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for obj1, obj2 in zip(list1, list2):
        if obj1.type != obj2.type or obj1.name != obj2.name or obj1.price != obj2.price:
            return False
    return True

class TestDatabase:
    def test_available_buns(self):
        expected_available_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]

        extracted_available_buns = Database().available_buns()
        assert compare_bun_lists(expected_available_buns, extracted_available_buns)

    def test_available_ingredients(self):
        expected_available_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        extracted_available_ingredients = Database().available_ingredients()
        assert compare_ingredients_lists(expected_available_ingredients, extracted_available_ingredients)