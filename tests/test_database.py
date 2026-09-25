import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.constants import (
    BUNS_COUNT,
    INGREDIENTS_COUNT,
    SAUCES_COUNT,
    FILLINGS_COUNT,
    ALL_INGREDIENTS,
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestDatabaseInit:
    def test_buns_count(self, database):
        assert len(database.buns) == BUNS_COUNT

    def test_ingredients_count(self, database):
        assert len(database.ingredients) == INGREDIENTS_COUNT

    def test_all_buns_are_bun_instances(self, database):
        assert all(isinstance(bun, Bun) for bun in database.buns)

    def test_all_ingredients_are_ingredient_instances(self, database):
        assert all(isinstance(ing, Ingredient) for ing in database.ingredients)


class TestAvailableBuns:
    def test_returns_list(self, database):
        assert isinstance(database.available_buns(), list)

    def test_returns_three_buns(self, database):
        assert len(database.available_buns()) == BUNS_COUNT

    def test_returns_same_object_as_attribute(self, database):
        assert database.available_buns() is database.buns


class TestAvailableIngredients:
    def test_returns_list(self, database):
        assert isinstance(database.available_ingredients(), list)

    def test_returns_six_ingredients(self, database):
        assert len(database.available_ingredients()) == INGREDIENTS_COUNT

    def test_returns_same_object_as_attribute(self, database):
        assert database.available_ingredients() is database.ingredients

    def test_three_sauces_and_three_fillings(self, database):
        types = [ing.get_type() for ing in database.available_ingredients()]
        assert types.count(INGREDIENT_TYPE_SAUCE) == SAUCES_COUNT
        assert types.count(INGREDIENT_TYPE_FILLING) == FILLINGS_COUNT

    @pytest.mark.parametrize(
        "name, price, ingredient_type",
        ALL_INGREDIENTS,
    )
    def test_ingredient_present(self, database, name, price, ingredient_type):
        ingredients = database.available_ingredients()
        match = [
            ing for ing in ingredients
            if ing.get_name() == name
            and ing.get_price() == price
            and ing.get_type() == ingredient_type
        ]
        assert len(match) == 1