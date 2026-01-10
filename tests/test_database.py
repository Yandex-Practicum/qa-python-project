import unittest
from practikum.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test_initial_bun_count(self):
        qty_buns = 3
        assert len(self.database.available_buns()) == qty_buns

    def test_bun_name_black(self):
        assert self.database.available_buns()[0].name == "black bun"

    def test_bun_name_white(self):
        assert self.database.available_buns()[1].name == "white bun"

    def test_bun_name_red(self):
        assert self.database.available_buns()[2].name == "red bun"

    def test_initial_ingredient_count(self):
        qty_ingredients = 6
        assert len(self.database.available_ingredients()) == qty_ingredients

    def test_ingredient_name_hot_sauce(self):
        assert self.database.available_ingredients()[0].name == "hot sauce"

    def test_ingredient_name_sour_cream(self):
        assert self.database.available_ingredients()[1].name == "sour cream"

    def test_ingredient_name_chili_sauce(self):
        assert self.database.available_ingredients()[2].name == "chili sauce"

    def test_ingredient_name_cutlet(self):
        assert self.database.available_ingredients()[3].name == "cutlet"

    def test_ingredient_name_dinosaur(self):
        assert self.database.available_ingredients()[4].name == "dinosaur"

    def test_ingredient_name_sausage(self):
        assert self.database.available_ingredients()[5].name == "sausage"
