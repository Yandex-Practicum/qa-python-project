import pytest
from database import Database
from parametrize_data import BUNS_DATA, INGREDIENTS_DATA

class TestDatabase:

    @pytest.mark.parametrize("index, expected_name, expected_price", BUNS_DATA)
    def test_init_database_creates_expected_buns_name(self, index, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].name == expected_name

    @pytest.mark.parametrize("index, expected_name, expected_price", BUNS_DATA)
    def test_init_database_creates_expected_buns_price(self, index, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].price == expected_price

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_init_database_creates_expected_ingredients_type(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].type == expected_type

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_init_database_creates_expected_ingredients_name(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].name == expected_name

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_init_database_creates_expected_ingredients_price(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].price == expected_price

    @pytest.mark.parametrize("index,expected_name,expected_price", BUNS_DATA)
    def test_available_buns_returns_expected_buns_name(self, index, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].name == expected_name


    @pytest.mark.parametrize("index,expected_name,expected_price", BUNS_DATA)
    def test_available_buns_returns_expected_buns_price(self, index, expected_name, expected_price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].price == expected_price

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_available_ingredients_returns_expected_ingredients_type(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].type == expected_type

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_available_ingredients_returns_expected_ingredients_name(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].name == expected_name

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", INGREDIENTS_DATA)
    def test_available_ingredients_returns_expected_ingredients(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ingredient = db.available_ingredients()
        assert ingredient[index].price == expected_price