import pytest
from praktikum.database import Database


class TestDatabase:
    
    @classmethod
    def setup_class(cls):
        cls.database = Database()
    
    @pytest.mark.parametrize('expected_result', ["black bun", "white bun", "red bun"])
    def test_available_buns(self, expected_result):
        buns = self.database.available_buns()
        buns_list = [bun.get_name() for bun in buns]
        assert expected_result in buns_list, buns_list

    @pytest.mark.parametrize('expected_result', ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"])
    def test_available_ingredients(self, expected_result):
        ingredients = self.database.available_ingredients()
        ingredient_list = [ingredient.get_name() for ingredient in ingredients]
        assert expected_result in ingredient_list, ingredient_list
