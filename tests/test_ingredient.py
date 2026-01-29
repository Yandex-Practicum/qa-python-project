import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Общие тестовые данные
    VALID_CASES = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_SAUCE, "соус барбекю", 150.50),
        (INGREDIENT_TYPE_FILLING, "к", 0.01),
        (INGREDIENT_TYPE_SAUCE, "очень длинное название ингредиента с множеством слов", 999.99)
    ]

    EDGE_CASES = [
        (INGREDIENT_TYPE_SAUCE, "", 100),
        (INGREDIENT_TYPE_FILLING, " ", 200),
        (INGREDIENT_TYPE_SAUCE, "123", 150),
        (INGREDIENT_TYPE_FILLING, "!@#$%^&*()", 200),
        ("UNKNOWN_TYPE", "mystery", 100),
        (None, "null", 100),
        (INGREDIENT_TYPE_SAUCE, "sauce", 0),
        (INGREDIENT_TYPE_FILLING, "filling", 0.001),
        (INGREDIENT_TYPE_SAUCE, "expensive", 999999.99)
    ]

    PRICE_TYPE_CASES = [
        (INGREDIENT_TYPE_SAUCE, "sauce", 100, True),
        (INGREDIENT_TYPE_FILLING, "filling", "100", False),
        (INGREDIENT_TYPE_SAUCE, "sauce", None, False),
        (INGREDIENT_TYPE_FILLING, "filling", [100], False),
        (INGREDIENT_TYPE_SAUCE, "sauce", {"price": 100}, False)
    ]

    NEGATIVE_PRICE_CASES = [
        (INGREDIENT_TYPE_SAUCE, "negative", -1),
        (INGREDIENT_TYPE_FILLING, "negative", -0.01),
        (INGREDIENT_TYPE_SAUCE, "very negative", -1000000)
    ]

    # Тесты для валидных случаев
    @pytest.mark.parametrize("ingredient_type, name, price", VALID_CASES)
    def test_valid_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", VALID_CASES)
    def test_valid_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", VALID_CASES)
    def test_valid_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Тесты для граничных случаев
    @pytest.mark.parametrize("ingredient_type, name, price", EDGE_CASES)
    def test_edge_cases_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", EDGE_CASES)
    def test_edge_cases_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", EDGE_CASES)
    def test_edge_cases_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Тесты типа цены
    @pytest.mark.parametrize("ingredient_type, name, price, expected_valid", PRICE_TYPE_CASES)
    def test_price_type_validation(self, ingredient_type, name, price, expected_valid):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_price(), (int, float)) == expected_valid

    # Тесты отрицательных цен
    @pytest.mark.parametrize("ingredient_type, name, price", NEGATIVE_PRICE_CASES)
    def test_negative_price_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient.get_price(), (int, float))

    @pytest.mark.parametrize("ingredient_type, name, price", NEGATIVE_PRICE_CASES)
    def test_negative_price_value(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
