
import pytest
from unittest.mock import patch
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_creates_buns(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        assert mock_bun_class.call_count == 3

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_creates_ingredients(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        assert mock_ingredient_class.call_count == 6

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_black_bun(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_bun_class.assert_any_call("black bun", 100)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_white_bun(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_bun_class.assert_any_call("white bun", 200)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_red_bun(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_bun_class.assert_any_call("red bun", 300)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_hot_sauce(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_sour_cream(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_SAUCE, "sour cream", 200)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_cutlet(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_database_initialization_dinosaur(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        mock_ingredient_class.assert_any_call(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_buns_returns_list(self, mock_bun_class, mock_ingredient_class):
        database = Database()
        buns = database.available_buns()

        assert isinstance(buns, list)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_buns_returns_correct_count(self, mock_bun_class, mock_ingredient_class):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_buns_returns_same_instance(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        assert database.available_buns() is database.buns

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_ingredients_returns_list(self, mock_bun_class, mock_ingredient_class):
        database = Database()
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_ingredients_returns_correct_count(self, mock_bun_class, mock_ingredient_class):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    @patch('praktikum.database.Ingredient')
    @patch('praktikum.database.Bun')
    def test_available_ingredients_returns_same_instance(self, mock_bun_class, mock_ingredient_class):
        database = Database()

        assert database.available_ingredients() is database.ingredients
        