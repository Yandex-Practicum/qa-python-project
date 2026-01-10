import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('name, price', [["black bun", 100], ["white bun", 200], ["red bun", 300]])
    def test_available_buns(self, name, price):
        mock_bun = Mock()
        mock_bun.append(Bun(name, price))
        mock_database = Database()
        assert len(mock_database.available_buns()) == 3

    @pytest.mark.parametrize('name_sauce, price_sauce',
                             [["hot sauce", 100], ["sour cream", 200], ["chili sauce", 300]])
    @pytest.mark.parametrize('name_filling, price_filling',
                             [["cutlet", 100], ["dinosaur", 200], ["sausage", 300]])
    def test_available_ingredients(self, name_sauce, name_filling, price_sauce, price_filling):
        mock_ingredients = Mock()
        mock_ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, name_sauce, price_sauce))
        mock_ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, name_filling, price_filling))
        mock_database = Database()
        assert len(mock_database.available_ingredients()) == 6
