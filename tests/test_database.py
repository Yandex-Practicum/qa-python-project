import pytest
from praktikum.database import Database
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize("bun_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)])
    def test_available_buns(self, bun_name, expected_price):
        mock = Mock()
        mock.available_buns.return_value = [bun_name, expected_price]
        assert mock.available_buns(mock) == [bun_name, expected_price]

    @pytest.mark.parametrize("ing_type, ing_name, ing_price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)])
    def test_available_ingredients_got(self, ing_type, ing_name, ing_price):
        mock = Mock()
        mock.available_ingredients.return_value = [ing_type, ing_name, ing_price]
        assert mock.available_ingredients(mock) == [ing_type, ing_name, ing_price]
