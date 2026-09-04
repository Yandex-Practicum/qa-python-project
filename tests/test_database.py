from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from tests.data import (
    DATABASE_BUN_NAMES,
    DATABASE_BUN_PRICES,
    DATABASE_FILLING_COUNT,
    DATABASE_INGREDIENT_COUNT,
    DATABASE_SAUCE_COUNT,
)


class TestDatabase:
    def test_available_buns_returns_all_buns(self, database):
        buns = database.available_buns()

        assert len(buns) == len(DATABASE_BUN_NAMES)
        assert tuple(bun.get_name() for bun in buns) == DATABASE_BUN_NAMES
        assert tuple(bun.get_price() for bun in buns) == DATABASE_BUN_PRICES

    def test_available_ingredients_returns_sauces_and_fillings(self, database):
        ingredients = database.available_ingredients()
        types = [ingredient.get_type() for ingredient in ingredients]

        assert len(ingredients) == DATABASE_INGREDIENT_COUNT
        assert types.count(INGREDIENT_TYPE_SAUCE) == DATABASE_SAUCE_COUNT
        assert types.count(INGREDIENT_TYPE_FILLING) == DATABASE_FILLING_COUNT
