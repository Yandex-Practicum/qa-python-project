import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (IngredientTypes.SAUCE, "hot sauce", 100),
        (IngredientTypes.SAUCE, "sour cream", 200),
        (IngredientTypes.FILLING, "cutlet", 100),
        (IngredientTypes.FILLING, "cheese", 300),
        (IngredientTypes.SAUCE, "chili sauce", 150.5),
        (IngredientTypes.FILLING, "dinosaur", 200),
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type,name,price,expected_type", [
        (IngredientTypes.SAUCE, "hot sauce", 100, IngredientTypes.SAUCE),
        (IngredientTypes.FILLING, "cutlet", 100, IngredientTypes.FILLING),
        (IngredientTypes.SAUCE, "sour cream", 200, IngredientTypes.SAUCE),
        (IngredientTypes.FILLING, "cheese", 300, IngredientTypes.FILLING),
    ])
    def test_get_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("ingredient_type,name,price,expected_name", [
        (IngredientTypes.SAUCE, "hot sauce", 100, "hot sauce"),
        (IngredientTypes.FILLING, "cutlet", 100, "cutlet"),
        (IngredientTypes.SAUCE, "very hot sauce with long name", 150, "very hot sauce with long name"),
        (IngredientTypes.FILLING, "dinosaur", 200, "dinosaur"),
        (IngredientTypes.SAUCE, "", 100, ""),
    ])
    def test_get_name(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("ingredient_type,name,price,expected_price", [
        (IngredientTypes.SAUCE, "hot sauce", 100, 100),
        (IngredientTypes.FILLING, "cutlet", 150.5, 150.5),
        (IngredientTypes.SAUCE, "cheap sauce", 0.99, 0.99),
        (IngredientTypes.FILLING, "expensive", 1000.00, 1000.00),
        (IngredientTypes.SAUCE, "free sauce", 0, 0),
        (IngredientTypes.FILLING, "negative", -50, -50),
    ])
    def test_get_price(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price

    def test_ingredient_with_invalid_type(self):
        ingredient = Ingredient("INVALID_TYPE", "test", 100)
        assert ingredient.get_type() == "INVALID_TYPE"
        assert ingredient.get_name() == "test"
        assert ingredient.get_price() == 100

    def test_ingredient_with_empty_name(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "", 100)
        assert ingredient.get_name() == ""
        assert ingredient.get_type() == IngredientTypes.SAUCE
        assert ingredient.get_price() == 100

    def test_ingredient_with_zero_price(self):
        ingredient = Ingredient(IngredientTypes.FILLING, "free", 0)
        assert ingredient.get_price() == 0
        assert ingredient.get_name() == "free"
        assert ingredient.get_type() == IngredientTypes.FILLING

    def test_ingredient_with_negative_price(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "discount", -50)
        assert ingredient.get_price() == -50
        assert ingredient.get_name() == "discount"
        assert ingredient.get_type() == IngredientTypes.SAUCE

    def test_ingredient_with_float_price(self):
        ingredient = Ingredient(IngredientTypes.FILLING, "premium", 99.99)
        assert ingredient.get_price() == 99.99
        assert ingredient.get_name() == "premium"
        assert ingredient.get_type() == IngredientTypes.FILLING

    def test_ingredient_sauce_type_constant(self):
        assert IngredientTypes.SAUCE == "SAUCE"
        assert INGREDIENT_TYPE_SAUCE == "SAUCE"

    def test_ingredient_filling_type_constant(self):
        assert IngredientTypes.FILLING == "FILLING"
        assert INGREDIENT_TYPE_FILLING == "FILLING"


    def test_ingredient_with_long_name(self):
        long_name = "abcdefghklabcdefghklabcdefghklabcdefghklabcdefghklabcdefghklabcdefghkl"
        ingredient = Ingredient(IngredientTypes.FILLING, long_name, 100)
        assert ingredient.get_name() == long_name
        assert ingredient.get_price() == 100
