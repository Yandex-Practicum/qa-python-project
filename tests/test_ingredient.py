import pytest
from diplom_1.praktikum.ingredient import Ingredient
from diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.fixture
    def sauce_ingredient(self):
        return Ingredient(INGREDIENT_TYPE_SAUCE, "Острый соус", 50)

    @pytest.fixture
    def filling_ingredient(self):
        return Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 100)

    # Позитивные тесты
    def test_get_type_returns_sauce(self, sauce_ingredient):
        assert sauce_ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_returns_filling(self, filling_ingredient):
        assert filling_ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_name_returns_correct_name(self, sauce_ingredient):
        assert sauce_ingredient.get_name() == "Острый соус"

    def test_get_price_returns_correct_price(self, filling_ingredient):
        assert filling_ingredient.get_price() == 100

    # Негативные тесты
    def test_init_with_invalid_type(self):
        ingredient = Ingredient("INVALID_TYPE", "Странный ингредиент", 50)
        assert ingredient.get_type() == "INVALID_TYPE"

    def test_init_with_empty_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 50)
        assert ingredient.get_name() == ""

    def test_init_with_zero_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 0)
        assert ingredient.get_price() == 0

    def test_init_with_negative_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", -10)
        assert ingredient.get_price() == -10