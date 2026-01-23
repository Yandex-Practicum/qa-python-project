from unittest.mock import Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns(self):
        mock = Mock()
        mock.buns = [['roll', 250], ['pancake', 200]]
        database = Database()
        database.buns = mock.buns

        assert mock.buns == database.available_buns()

    def test_available_ingredients(self):
        mock = Mock()
        mock.ingredients = [[INGREDIENT_TYPE_SAUCE, 'ketchup', 50], [INGREDIENT_TYPE_FILLING, 'meat', 200]]
        database = Database()
        database.ingredients = mock.ingredients

        assert mock.ingredients == database.available_ingredients()


