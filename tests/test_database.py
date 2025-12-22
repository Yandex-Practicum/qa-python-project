import pytest

import data


class TestDatabase:

    @pytest.mark.parametrize('number, name, price', data.BunsDatabase.all_buns)
    def test_available_buns(self, create_database, number, name, price):
        buns = create_database.available_buns()
        assert buns[number].name == name and buns[number].price == price

    @pytest.mark.parametrize('number, name, price', data.IngredientsDatabase.all_ingredients)
    def test_available_ingredients(self, create_database, number, name, price):
        ingredient = create_database.available_ingredients()
        assert ingredient[number].name == name and ingredient[number].price == price
