import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_name_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_name() == "cutlet"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_get_price_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_price() == 150

    def test_get_type_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_creation_hot_sauce_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_creation_hot_sauce_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_creation_hot_sauce_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_creation_sour_cream_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_creation_sour_cream_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert ingredient.get_name() == "sour cream"

    def test_creation_sour_cream_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        assert ingredient.get_price() == 200

    def test_creation_cutlet_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_creation_cutlet_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_name() == "cutlet"

    def test_creation_cutlet_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_price() == 150

    def test_creation_dinosaur_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 250)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    def test_creation_dinosaur_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 250)
        assert ingredient.get_name() == "dinosaur"

    def test_creation_dinosaur_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 250)
        assert ingredient.get_price() == 250


