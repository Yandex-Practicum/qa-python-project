import pytest
from praktikum.database import Database

class TestDataBase:

    @pytest.mark.parametrize('number, name, price', [
        (0, 'bread roll', 10),
        (1, 'rye roll', 5),
        (2, 'oat roll', 3)
    ])
    def test_available_buns(self, number, name, price):
        database = Database()

        assert len(database.available_buns()) == 3

    @pytest.mark.parametrize('number, name, price', [
        (0,  'catchup', 2),
        (1,  'steak', 10)
    ])
    def test_available_ingredients(self,  number, name, price):
        database = Database()

        assert len(database.available_ingredients()) == 6

