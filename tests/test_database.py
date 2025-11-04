import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:

    def test_available_buns_returns_lits_of_buns(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_lits_of_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    @pytest.mark.parametrize('index, expected_name, expected_price', [(0, 'black bun', 100), (1, 'white bun', 200), (2, 'red bun', 300)])
    def test_available_buns_indexes_returns_correts_buns(self, database, index, expected_name, expected_price):
        buns = database.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price     

    @pytest.mark.parametrize('index, expected_type, expected_name, expected_price', [(0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100), (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100), (5, INGREDIENT_TYPE_FILLING, 'sausage', 300)])
    def test_available_ingredients_indexes_returns_correts_ingredients(self, database, index, expected_type, expected_name, expected_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price            
