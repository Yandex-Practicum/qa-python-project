import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestDatabase:
    """Тесты для класса Database."""

    def test_init_no_args_buns_list_not_empty(self):
        database = Database()
        assert len(database.buns) > 0

    def test_init_no_args_ingredients_list_not_empty(self):
        database = Database()
        assert len(database.ingredients) > 0

    def test_init_no_args_buns_contains_three_items(self):
        database = Database()
        assert len(database.buns) == 3

    def test_init_no_args_ingredients_contains_six_items(self):
        database = Database()
        assert len(database.ingredients) == 6

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_init_buns_have_expected_name_and_price(
        self, index, expected_name, expected_price
    ):
        database = Database()
        bun = database.buns[index]
        assert isinstance(bun, Bun)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
    )
    def test_init_ingredients_have_expected_type_name_price(
        self, index, expected_type, expected_name, expected_price
    ):
        database = Database()
        ingredient = database.ingredients[index]
        assert isinstance(ingredient, Ingredient)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

    def test_available_buns_no_args_returns_buns_list(self):
        database = Database()
        assert database.available_buns() is database.buns

    def test_available_buns_no_args_returns_three_items(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_no_args_returns_ingredients_list(self):
        database = Database()
        assert database.available_ingredients() is database.ingredients

    def test_available_ingredients_no_args_returns_six_items(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    def test_two_databases_are_independent(self):
        db1 = Database()
        db2 = Database()
        assert db1.buns is not db2.buns
        assert db1.ingredients is not db2.ingredients

    def test_two_databases_have_equal_content(self):
        db1 = Database()
        db2 = Database()
        assert [b.get_name() for b in db1.buns] == [b.get_name() for b in db2.buns]
        assert [i.get_name() for i in db1.ingredients] == [
            i.get_name() for i in db2.ingredients
        ]
        