import pytest
from ..database import Database


class TestDatabase:
    @pytest.mark.parametrize('bun', ['black bun'])
    def test_available_buns(self, bun):
        buns_list = lambda: [i.get_name() for i in Database().available_buns()]
        assert bun in buns_list()

    @pytest.mark.parametrize('ingredient', ['hot sauce'])
    def test_available_ingredients(self, ingredient):
        ingredients_list = lambda: [i.get_name() for i in Database().available_ingredients()]
        assert ingredient in ingredients_list()