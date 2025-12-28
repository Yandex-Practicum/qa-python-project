from unittest.mock import patch, Mock
import pytest
from Diplom_1.practicum.database import Database

class TestDatabase:

    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_buns(self, index):
        database = Database()
        bun_list = database.available_buns()
        bun_name = database.buns[index].name

        assert bun_name == bun_list[index].name


    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_ingredients(self, index):
        database = Database()
        ingredients_list = database.available_ingredients()
        ingredient_name = database.ingredients[index].name

        assert ingredient_name == ingredients_list[index].name