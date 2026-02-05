import pytest
from data import BUNS_NAME_PRICE, INGREDIENTS_TYPE_NAME_PRICE


class TestDatabase:

    @pytest.mark.parametrize(
    "name, price", BUNS_NAME_PRICE)
    def test_available_buns(self, database_fixture, name, price):
        buns = database_fixture.available_buns()
        assert [bun.name == name and bun.price == price for bun in buns] and len(database_fixture.available_buns()) == 3

    @pytest.mark.parametrize(
    "type, name, price", INGREDIENTS_TYPE_NAME_PRICE)
    def test_available_ingredients(self, database_fixture, type, name, price):
        ingredients = database_fixture.available_ingredients()
        assert ([ingredient.type == type and ingredient.name == name and ingredient.price == price for ingredient in ingredients] 
                and len(database_fixture.available_ingredients()) == 6)