import pytest
from praktikum.database import Database


class TestDatabase:
    def setup_method(self):
        self.data = Database()

    def test_available_buns(self):
        assert len(self.data.available_buns()) == 3

    def test_available_ingredients(self):
        assert len(self.data.available_ingredients()) == 6

    @pytest.mark.parametrize("bun, price", [["black bun", 100.0],
                                            ["white bun", 200.0],
                                            ["red bun", 300.0]])
    def test_available_buns_lst(self, bun: str, price: float):
        self.data.buns = (bun, price)

        assert self.data.available_buns() == self.data.buns

    @pytest.mark.parametrize("type_ingredient, ingredient, price", [["filling", "cutlet", 100.0],
                                                                    ["sauce", "hot sauce", 100.0],
                                                                    ["filling", "sausage", 300.0]])
    def test_available_ingredients_lst(self, type_ingredient, ingredient, price):
        self.data.ingredients = (type_ingredient, ingredient, price)

        assert self.data.available_ingredients() == self.data.ingredients
