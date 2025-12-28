from unittest.mock import patch, Mock
import pytest
from Diplom_1.practicum.ingredient import Ingredient
from Diplom_1.practicum.database import Database


class TestIngredient:

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_price(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_price() == price

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_name(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_name() == name

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_type(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_type() == type