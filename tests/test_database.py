import pytest
from ..database import Database
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_init_buns(self):
        db = Database()
        assert len(db.buns) == 3
        for bun in db.buns:
            assert isinstance(bun, Bun)

    @pytest.mark.parametrize("bun_index,expected_name", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun"),
    ])
    def test_buns_name(self, bun_index, expected_name):
        db = Database()
        bun = db.buns[bun_index]
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("bun_index,expected_price", [
        (0, 100),
        (1, 200),
        (2, 300),
    ])
    def test_buns_price(self, bun_index, expected_price):
        db = Database()
        bun = db.buns[bun_index]
        assert bun.get_price() == expected_price

    def test_init_ingredients(self):
        db = Database()
        assert len(db.ingredients) == 6
        for ingredient in db.ingredients:
            assert isinstance(ingredient, Ingredient)

        sauces = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(sauces) == 3
        assert len(fillings) == 3

    @pytest.mark.parametrize("ingredient_index,expected_name", [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage"),
    ])
    def test_ingredients_name(self, ingredient_index, expected_name):
        db = Database()
        ingredient = db.ingredients[ingredient_index]
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("ingredient_index,expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredients_type(self, ingredient_index, expected_type):
        db = Database()
        ingredient = db.ingredients[ingredient_index]
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("ingredient_index,expected_price", [
        (0, 100),
        (1, 200),
        (2, 300),
        (3, 100),
        (4, 200),
        (5, 300),
    ])
    def test_ingredients_price(self, ingredient_index, expected_price):
        db = Database()
        ingredient = db.ingredients[ingredient_index]
        assert ingredient.get_price() == expected_price

    def test_available_buns_returns_buns(self):
        db = Database()
        assert db.available_buns() is db.buns

    def test_available_ingredients_returns_ingredients(self):
        db = Database()
        assert db.available_ingredients() is db.ingredients
