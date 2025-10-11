from unittest.mock import Mock

from praktikum.database import Database
import data

class Testdatabase():

    def test_available_buns_return_value(self):
        testdatabase = Database()
        mock_buns = Mock()

        available_buns = testdatabase.available_buns()
        lst_buns = []
        for _ in range(len(available_buns)):
            mock_buns.name = data.DEF_BUNS[_][0]
            mock_buns.price = data.DEF_BUNS[_][1]
            lst_buns.append(mock_buns)
            assert lst_buns[_].name == available_buns[_].name and lst_buns[_].price == available_buns[_].price

    def test_available_available_ingredients_return_value(self):
        testdatabase = Database()
        mock_ingredients = Mock()

        available_ingredients = testdatabase.available_ingredients()
        lst_ingredients = []
        for _ in range(len(available_ingredients)):
            mock_ingredients.type = data.DEF_INGREDIENTS[_][0]
            mock_ingredients.name = data.DEF_INGREDIENTS[_][1]
            mock_ingredients.price = data.DEF_INGREDIENTS[_][2]
            lst_ingredients.append(mock_ingredients)

            assert lst_ingredients[_].type == available_ingredients[_].type and lst_ingredients[_].name == available_ingredients[_].name and lst_ingredients[_].price == available_ingredients[_].price
