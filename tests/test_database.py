from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_initialized_with_buns_checks_length(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_database_initialized_with_buns_checks_type(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns[0], Bun)

    def test_database_initialized_with_ingredients_checks_length(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_database_initialized_with_ingredients_checks_type(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients[0], Ingredient)

    def test_buns_content_black_bun(self):
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

    def test_buns_content_white_bun(self):
        db = Database()
        buns = db.available_buns()
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200

    def test_buns_content_red_bun(self):
        db = Database()
        buns = db.available_buns()
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_ingredients_content_hot_sauce(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

    def test_ingredients_content_sour_cream(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200

    def test_ingredients_content_chili_sauce(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300

    def test_ingredients_content_cutlet(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100

    def test_ingredients_content_dinosaur(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200

    def test_ingredients_content_sausage(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300

    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)


