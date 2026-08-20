from unittest.mock import patch

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_available_buns_returns_created_buns(self):
        database = Database()

        buns = database.available_buns()

        assert [bun.get_name() for bun in buns] == ['black bun', 'white bun', 'red bun']
        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients_returns_created_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert [ingredient.get_name() for ingredient in ingredients] == [
            'hot sauce',
            'sour cream',
            'chili sauce',
            'cutlet',
            'dinosaur',
            'sausage',
        ]
        assert [ingredient.get_type() for ingredient in ingredients] == [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
            INGREDIENT_TYPE_FILLING,
            INGREDIENT_TYPE_FILLING,
        ]

    def test_database_creates_buns_with_expected_values(self):
        with patch('praktikum.database.Bun') as bun_mock:
            Database()

        assert bun_mock.call_args_list[0].args == ('black bun', 100)
        assert bun_mock.call_args_list[1].args == ('white bun', 200)
        assert bun_mock.call_args_list[2].args == ('red bun', 300)

    def test_database_creates_ingredients_with_expected_values(self):
        with patch('praktikum.database.Ingredient') as ingredient_mock:
            Database()

        assert ingredient_mock.call_args_list[0].args == (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert ingredient_mock.call_args_list[3].args == (INGREDIENT_TYPE_FILLING, 'cutlet', 100)
        assert ingredient_mock.call_args_list[5].args == (INGREDIENT_TYPE_FILLING, 'sausage', 300)
