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

    @pytest.mark.parametrize("bun_index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_buns_data(self, bun_index, expected_name, expected_price):
        db = Database()
        bun = db.buns[bun_index]
        assert bun.get_name() == expected_name
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

    @pytest.mark.parametrize("ingredient_index,expected_name,expected_type,expected_price", [
        (0, "hot sauce", INGREDIENT_TYPE_SAUCE, 100),
        (1, "sour cream", INGREDIENT_TYPE_SAUCE, 200),
        (2, "chili sauce", INGREDIENT_TYPE_SAUCE, 300),
        (3, "cutlet", INGREDIENT_TYPE_FILLING, 100),
        (4, "dinosaur", INGREDIENT_TYPE_FILLING, 200),
        (5, "sausage", INGREDIENT_TYPE_FILLING, 300),
    ])
    def test_ingredients_data(self, ingredient_index, expected_name, expected_type, expected_price):
        db = Database()
        ingredient = db.ingredients[ingredient_index]
        assert ingredient.get_name() == expected_name
        assert ingredient.get_type() == expected_type
        assert ingredient.get_price() == expected_price

    def test_available_buns_returns_buns(self):
        db = Database()
        assert db.available_buns() is db.buns

    def test_available_ingredients_returns_ingredients(self):
        db = Database()
        assert db.available_ingredients() is db.ingredients
