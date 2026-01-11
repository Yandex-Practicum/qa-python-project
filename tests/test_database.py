from database import Database
from unittest.mock import patch



class TestDb:

    @patch('database.Database.available_buns', return_value="беспонтовый пирожок")
    def test_db_buns(self, mock_buns):
        database = Database()
        assert database.available_buns() == "беспонтовый пирожок"


    @patch('database.Database.available_ingredients', return_value="подлива")
    def test_db_ingredients(self, mock_ingredients):
        database = Database()
        assert database.available_ingredients() == "подлива"



