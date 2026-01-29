import sys

from Diplom_1.data import Data

sys.path.append('C:\\Cygwin\\home\\user\\Diplom\\Diplom_1')
from Diplom_1.database import Database
from unittest.mock import patch
from Diplom_1.mock_classes import MockBun, MockIngredient



class TestDatabase():
    @patch('Diplom_1.database.Database.available_buns')
    def test_available_buns(self, mock_available_buns):
        expected_buns = [
            MockBun(Data.bun_one, Data.price_one),
            MockBun(Data.bun_two, Data.price_two),
            MockBun(Data.bun_three, Data.price_three)
        ]
        mock_available_buns.return_value = expected_buns
        database = Database()
        buns = database.available_buns()

        assert buns==expected_buns

    @patch('Diplom_1.database.Database.available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        # Создаем список ожидаемых ингредиентов
        expected_ingredients = [
            MockIngredient(Data.one_type, Data.sauce_one, Data.price_one),
            MockIngredient(Data.one_type, Data.sauce_two, Data.price_two),
            MockIngredient(Data.one_type, Data.sauce_three, Data.price_three),
            MockIngredient(Data.two_type, Data.filling_one, Data.price_one),
            MockIngredient(Data.two_type, Data.filling_two, Data.price_two),
            MockIngredient(Data.two_type, Data.filling_three, Data.price_three)
        ]

        mock_available_ingredients.return_value = expected_ingredients
        database = Database()
        assert database.available_ingredients()==expected_ingredients