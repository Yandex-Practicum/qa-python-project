from unittest.mock import Mock

import pytest

from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDataBase:

    @pytest.mark.parametrize(
        'name, price, index',
        [
            ('black bun', 100, 0),
            ('white bun', 200, 1),
            ('red bun', 300, 2),
        ]
    )
    def test_available_buns(self, name, price, index):
        database = Database()
        bun = Bun(name=name, price=price)
        database_buns = database.available_buns()

        assert database_buns[index].get_price() == bun.get_price()
        assert database_buns[index].get_name() == bun.get_name()

    @pytest.mark.parametrize(
        'ingredient_type, name, price, index',
        [
            (ingredient_types.INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, 0),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, 'sour cream', 200, 1),
            (ingredient_types.INGREDIENT_TYPE_SAUCE, 'chili sauce', 300, 2),
            (ingredient_types.INGREDIENT_TYPE_FILLING, 'cutlet', 100, 3),
            (ingredient_types.INGREDIENT_TYPE_FILLING, 'dinosaur', 200, 4),
            (ingredient_types.INGREDIENT_TYPE_FILLING, 'sausage', 300, 5)
        ]
    )
    def test_available_ingredients(self, ingredient_type, name, price, index):
        database = Database()
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        database_ingredient = database.available_ingredients()

        assert database_ingredient[index].get_price() == ingredient.get_price()
        assert database_ingredient[index].get_name() == ingredient.get_name()
        assert database_ingredient[index].get_type() == ingredient.get_type()

    def test_mock_available_buns(self):
        database = Database()
        mock_database = Mock()
        mock_database.available_buns.return_value = [Bun(name='mock_bun_name', price=100)]
        database.available_buns = mock_database.available_buns

        database_buns = database.available_buns()
        assert len(database_buns) == 1
        assert database_buns[0].get_name() == 'mock_bun_name'
        assert database_buns[0].get_price() == 100

    def test_mock_available_ingredients(self):
        database = Database()
        mock_database = Mock()
        mock_database.available_ingredients.return_value = [
            Ingredient(name='mock_ingredient_name', price=100, ingredient_type=ingredient_types.INGREDIENT_TYPE_SAUCE)
        ]
        database.available_ingredients = mock_database.available_ingredients

        database_ingredients = database.available_ingredients()
        assert len(database_ingredients) == 1
        assert database_ingredients[0].get_name() == 'mock_ingredient_name'
        assert database_ingredients[0].get_price() == 100
        assert database_ingredients[0].get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE




