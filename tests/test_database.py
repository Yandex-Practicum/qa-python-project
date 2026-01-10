import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from database import Database

class TestDatabase:
    def test_available_buns(self, mock_database):
        buns = mock_database.available_buns()
        assert len(buns) == 3
        mock_database.available_buns.assert_called_once()

    def test_available_ingredients(self, mock_database):
        ingredients = mock_database.available_ingredients()
        assert len(ingredients) == 6
        mock_database.available_ingredients.assert_called_once()

    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price",
        [
            ("black bun", 100, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            ("white bun", 200, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            ("red bun", 300, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        ],
    )
    def test_database_initialization_mocked_parameterized(
        self, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price
    ):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price

        database = Database()

        database.buns = [mock_bun]
        database.ingredients = [mock_ingredient]

        assert len(database.buns) == 1
        assert len(database.ingredients) == 1

        assert database.buns[0].name == bun_name
        assert database.buns[0].price == bun_price

        assert database.ingredients[0].type == ingredient_type
        assert database.ingredients[0].name == ingredient_name
        assert database.ingredients[0].price == ingredient_price