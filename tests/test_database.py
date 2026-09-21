import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_buns_count(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_database_ingredients_count(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    @pytest.mark.parametrize(
        'index, expected_name, expected_price',
        [
            (0, 'black bun', 100),
            (1, 'white bun', 200),
            (2, 'red bun', 300),
        ]
    )
    def test_database_available_buns_data(self, index, expected_name, expected_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize(
        'index, expected_type, expected_name, expected_price',
        [
            (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            (5, INGREDIENT_TYPE_FILLING, 'sausage', 300),
        ]
    )
    def test_database_available_ingredients_data(self, index, expected_type, expected_name, expected_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price
