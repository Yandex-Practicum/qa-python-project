from unittest.mock import patch
from praktikum.database import Database

class TestDatabase:
    def test_available_buns(self, mock_random_choice):
        db = Database()
        mock_bun = db.buns[0]
        mock_random_choice.return_value = mock_bun
        bun = db.available_buns()
        assert bun == mock_bun

    def test_available_ingredients(self, mock_random_choice):
        db = Database()
        mock_ingredient = db.ingredients[0]
        mock_random_choice.return_value = mock_ingredient
        ingredient = db.available_ingredients()
        assert ingredient == mock_ingredient