import pytest

from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


class TestAvailableBuns:
    """Тесты метода available_buns."""

    def test_available_buns_returns_three_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize(
        "index, expected_name",
        [
            (0, "black bun"),
            (1, "white bun"),
            (2, "red bun"),
        ],
    )
    def test_available_buns_returns_bun_with_name(
        self, database, index, expected_name
    ):
        buns = database.available_buns()
        assert buns[index].get_name() == expected_name

    @pytest.mark.parametrize(
        "index, expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
        ],
    )
    def test_available_buns_returns_bun_with_price(
        self, database, index, expected_price
    ):
        buns = database.available_buns()
        assert buns[index].get_price() == expected_price


class TestAvailableIngredients:
    """Тесты метода available_ingredients."""

    def test_available_ingredients_returns_six(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    @pytest.mark.parametrize(
        "index, expected_type",
        [
            (0, INGREDIENT_TYPE_SAUCE),
            (1, INGREDIENT_TYPE_SAUCE),
            (2, INGREDIENT_TYPE_SAUCE),
            (3, INGREDIENT_TYPE_FILLING),
            (4, INGREDIENT_TYPE_FILLING),
            (5, INGREDIENT_TYPE_FILLING),
        ],
    )
    def test_available_ingredients_returns_ingredient_with_type(
        self, database, index, expected_type
    ):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type

    @pytest.mark.parametrize(
        "index, expected_name",
        [
            (0, "hot sauce"),
            (1, "sour cream"),
            (2, "chili sauce"),
            (3, "cutlet"),
            (4, "dinosaur"),
            (5, "sausage"),
        ],
    )
    def test_available_ingredients_returns_ingredient_with_name(
        self, database, index, expected_name
    ):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_name() == expected_name

    @pytest.mark.parametrize(
        "index, expected_price",
        [
            (0, 100),
            (1, 200),
            (2, 300),
            (3, 100),
            (4, 200),
            (5, 300),
        ],
    )
    def test_available_ingredients_returns_ingredient_with_price(
        self, database, index, expected_price
    ):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_price() == expected_price