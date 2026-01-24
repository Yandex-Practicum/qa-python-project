from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        assert len(database.available_buns()) == len(expected_buns)

        #Проверить, что все булочки в базе данных совпадают с ожидаемыми
        for bun in range(len(database.available_buns())):
            assert database.available_buns()[bun].get_name() == expected_buns[bun].get_name()
            assert database.available_buns()[bun].get_price() == expected_buns[bun].get_price()

    def test_available_ingredients(self):
        database = Database()
        expected_ingredients = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
        assert len(database.available_ingredients()) == len(expected_ingredients)
        for ingredient in range(len(database.available_ingredients())):
            assert database.available_ingredients()[ingredient].get_name() == expected_ingredients[ingredient].get_name()
            assert database.available_ingredients()[ingredient].get_price() == expected_ingredients[ingredient].get_price()
            assert database.available_ingredients()[ingredient].get_type() == expected_ingredients[ingredient].get_type()
