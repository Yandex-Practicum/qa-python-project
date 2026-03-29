from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_init(self):
        db = Database()
        assert db is not None
        assert hasattr(db, 'buns')
        assert hasattr(db, 'ingredients')

    def test_available_buns_list(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_buns_content(self):
        db = Database()
        buns = db.available_buns()

        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]

        for i, (expected_name, expected_price) in enumerate(expected_buns):
            assert buns[i].get_name() == expected_name
            assert buns[i].get_price() == expected_price

    def test_available_buns_returns_correct_types(self):
        db = Database()
        buns = db.available_buns()

        for bun in buns:
            assert isinstance(bun, Bun)
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ing, Ingredient) for ing in ingredients)

    def test_available_ingredients_content(self):
        db = Database()
        ingredients = db.available_ingredients()

        expected_ingredients = [
            (IngredientTypes.SAUCE, "hot sauce", 100),
            (IngredientTypes.SAUCE, "sour cream", 200),
            (IngredientTypes.SAUCE, "chili sauce", 300),
            (IngredientTypes.FILLING, "cutlet", 100),
            (IngredientTypes.FILLING, "dinosaur", 200),
            (IngredientTypes.FILLING, "sausage", 300)
        ]

        for i, (expected_type, expected_name, expected_price) in enumerate(expected_ingredients):
            assert ingredients[i].get_type() == expected_type
            assert ingredients[i].get_name() == expected_name
            assert ingredients[i].get_price() == expected_price

    def test_available_ingredients_sauce_count(self):
        db = Database()
        ingredients = db.available_ingredients()

        sauces = [ing for ing in ingredients if ing.get_type() == IngredientTypes.SAUCE]
        assert len(sauces) == 3

    def test_available_ingredients_filling_count(self):
        db = Database()
        ingredients = db.available_ingredients()

        fillings = [ing for ing in ingredients if ing.get_type() == IngredientTypes.FILLING]
        assert len(fillings) == 3

    def test_database_returns_same_instances(self):
        db = Database()

        buns1 = db.available_buns()
        buns2 = db.available_buns()

        assert buns1 is buns2
        assert buns1[0] is buns2[0]
        assert buns1[0].get_name() == buns2[0].get_name()
        assert buns1[0].get_price() == buns2[0].get_price()

    def test_database_ingredients_are_same_instances(self):
        db = Database()

        ingredients1 = db.available_ingredients()
        ingredients2 = db.available_ingredients()

        assert ingredients1 is ingredients2
        assert ingredients1[0] is ingredients2[0]
        assert ingredients1[0].get_name() == ingredients2[0].get_name()
        assert ingredients1[0].get_price() == ingredients2[0].get_price()

    def test_database_buns_are_mutable(self):
        db = Database()
        buns = db.available_buns()
        original_name = buns[0].get_name()
        original_price = buns[0].get_price()
        buns[0].name = "modified bun"

        assert db.available_buns()[0].get_name() == "modified bun"

        buns[0].name = original_name
        buns[0].price = original_price

    def test_database_ingredients_are_mutable(self):
        db = Database()
        ingredients = db.available_ingredients()
        original_name = ingredients[0].get_name()
        original_price = ingredients[0].get_price()
        ingredients[0].name = "modified ingredient"

        assert db.available_ingredients()[0].get_name() == "modified ingredient"

        ingredients[0].name = original_name
        ingredients[0].price = original_price
