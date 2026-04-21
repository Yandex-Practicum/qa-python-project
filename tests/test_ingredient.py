from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_create_ingredient_sets_type(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_create_ingredient_sets_name(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.name == ingredient_name

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_create_ingredient_sets_price(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.price == ingredient_price

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_get_name_returns_correct_name(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_get_price_returns_correct_price(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Хрустящие минеральные кольца", 300), ("Соус", "Традиционный галактический", 15)],
    )
    def test_get_type_returns_correct_type(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type