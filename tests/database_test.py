import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


class TestDatabase:
    def test_available_buns_returns_three_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_content(self, database):
        buns = database.available_buns()
        assert [bun.get_name() for bun in buns] == ["black bun", "white bun", "red bun"]
        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients_returns_six(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_content(self, database):
        ingredients = database.available_ingredients()
        names = [ing.get_name() for ing in ingredients]
        types = [ing.get_type() for ing in ingredients]

        assert names == [
            "hot sauce", "sour cream", "chili sauce",
            "cutlet", "dinosaur", "sausage",
        ]
        assert types == [
            INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING,
        ]

    def test_available_ingredients_prices(self, database):
        prices = [ing.get_price() for ing in database.available_ingredients()]
        assert prices == [100, 200, 300, 100, 200, 300]