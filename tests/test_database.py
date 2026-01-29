import pytest
from praktikum.database import Database


class TestDatabase:

    @pytest.mark.parametrize('number_in_list, name, price', [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_init_data_buns(self, number_in_list, name, price):
        database = Database()
        exempl_bun = getattr(database, 'buns')[number_in_list]
        assert exempl_bun.get_name() == name and exempl_bun.get_price() == price

    @pytest.mark.parametrize('number_in_list, type_ing, name, price', [
        (0, 'SAUCE', "hot sauce", 100),
        (1, 'SAUCE', "sour cream", 200),
        (2, 'SAUCE', "chili sauce", 300),
        (3, 'FILLING', "cutlet", 100),
        (4, 'FILLING', "dinosaur", 200),
        (5, 'FILLING', "sausage", 300)
    ])
    def test_init_data_ingredient(self, number_in_list, type_ing, name, price):
        database = Database()
        exempl_ing = getattr(database, 'ingredients')[number_in_list]
        assert exempl_ing.get_name() == name and exempl_ing.get_price() == price and exempl_ing.get_type()

    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
