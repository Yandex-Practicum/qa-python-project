from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def test_amount_of_available_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_bun_type_by_a_number_in_the_list_is_bun(self, database):
        for bun in database.available_buns():
            assert isinstance(bun, Bun)

    def test_amount_of_available_ingredients(self, database):
        assert len(database.available_ingredients()) == 6

    def test_ingredients_type_by_a_number_in_the_list_is_ingredient(self, database):
        for ingredient in database.available_ingredients():
            assert isinstance(ingredient, Ingredient)
