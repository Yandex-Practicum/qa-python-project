from unittest.mock import patch, Mock
from praktikum.database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE
import pytest

class TestDatabase:
    @pytest.fixture
    def mock_database(self):
        mock_database = Mock()
        return mock_database

    @patch('praktikum.database.Database')
    def test_available_buns_name(self, mock_database_class, mock_database):
        mock_buns = [Mock(name="black bun", price=100)]
        mock_database.available_buns.return_value = mock_buns
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_buns()
        assert result[0].name == "black bun"

    @patch('praktikum.database.Database')
    def test_available_buns_price(self, mock_database_class, mock_database):
        mock_buns = [Mock(name="black bun", price=100)]
        mock_database.available_buns.return_value = mock_buns
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_buns()
        assert result[0].price == 100

    @patch('praktikum.database.Database')
    def test_available_ingredients_type(self, mock_database_class, mock_database):
        mock_ingredients = [Mock(type=INGREDIENT_TYPE_SAUCE, name="hot sauce")]
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_ingredients()
        assert result[0].type == INGREDIENT_TYPE_SAUCE

    @patch('praktikum.database.Database')
    def test_available_ingredients_name(self, mock_database_class, mock_database):
        mock_ingredients = [Mock(type=INGREDIENT_TYPE_SAUCE, name="hot sauce")]
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_database_class.return_value = mock_database
        db = Database()
        result = db.available_ingredients()
        assert result[0].name == "hot sauce"
