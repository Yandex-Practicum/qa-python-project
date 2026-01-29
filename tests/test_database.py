import pytest
from data import BurgerData
from ingredient import Ingredient


class TestDatabase:
    @pytest.mark.parametrize('index_list, bun_name_is_available', [
        (0, BurgerData.BUN_NAME),
        (1, BurgerData.BUN_NAME_2)])
    def test_available_buns(self, database, index_list, bun_name_is_available):
        database.available_buns()

        assert database.available_buns()[index_list].name == bun_name_is_available

    def test_available_ingredients(self, database):

        available_ingredients = database.available_ingredients()
        ingredient_list = []
        for ingredient in available_ingredients:
            ingredient_list.append(ingredient.get_name())

        assert (isinstance(available_ingredients, list) and "chili sauce" in ingredient_list
                and isinstance(available_ingredients[0], Ingredient))
