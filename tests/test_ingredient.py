import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


class TestIngredient:
    def test_get_name_of_ingredient(self, create_new_ingredient):
        assert create_new_ingredient.get_name() == "hot sauce"

    def test_get_price_of_ingredient(self, create_new_ingredient):
        assert create_new_ingredient.get_price() == 100

    def test_get_type_of_ingredient(self, create_new_ingredient):
        assert create_new_ingredient.get_type() == 'SAUCE'