import pytest
from database import  Database
from data import Data
from helpers import Helpers


class TestDatabase:

    def test_available_buns(self):
        available_names = ["black bun", "white bun","red bun"]
        assert Helpers.list_names == available_names

    def test_available_ingredients(self):
        available_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        assert Helpers.ingr_names == available_names