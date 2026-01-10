from unittest import mock
from Diplom_1.practikum.database import Database

class TestDatabaseMethod:
    def test_available_buns(self):
        database = Database()
        mock_buns = [mock.Mock(name='Грязный Джо'), mock.Mock(name='Большой Джо'), mock.Mock(name='детский Джо')]
        database.available_buns = mock.Mock(return_value=mock_buns)
        assert database.available_buns() == mock_buns

    def test_available_ingredients(self):
        database = Database()
        mock_ingredients = [mock.Mock(name="Котлета"), mock.Mock(name="Сыр"), mock.Mock(name="Салат"),
                            mock.Mock(name="кетчунез"), mock.Mock(name="майонез"), mock.Mock(name="кетчуп")]
        database.available_ingredients = mock.Mock(return_value=mock_ingredients)
        assert database.available_ingredients() == mock_ingredients
