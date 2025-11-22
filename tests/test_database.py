from unittest.mock import patch, Mock

import pytest


from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize(
        "number, name_bun, price_bun",
        [[0, "black bun", 100], [1, "white bun", 200], [2, "red bun", 300]],
    )
    @patch("praktikum.database.Bun")
    def test_database_bun_success(self, mock_bun, number, name_bun, price_bun):
        bun_mock = Mock()
        bun_mock.configure_mock(name=name_bun, price=price_bun)
        mock_bun.return_value = bun_mock
        database = Database()
        assert (
            database.buns[number].name == name_bun
            and database.buns[number].price == price_bun
        )

    @pytest.mark.parametrize(
        "number, type_ingr, name_ingr, price_ingr",
        [
            [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
            [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
            [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
            [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
            [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
            [5, INGREDIENT_TYPE_FILLING, "sausage", 300],
        ],
    )
    @patch("praktikum.database.Ingredient")
    def test_database_ingredient_success(
        self, mock_ingr, number, type_ingr, name_ingr, price_ingr
    ):
        ingr_mock = Mock()
        ingr_mock.configure_mock(type=type_ingr, name=name_ingr, price=price_ingr)
        mock_ingr.return_value = ingr_mock
        database = Database()
        assert (
            database.ingredients[number].name == name_ingr
            and database.ingredients[number].price == price_ingr
            and database.ingredients[number].type == type_ingr
        )

    def test_available_buns_success(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_success(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
