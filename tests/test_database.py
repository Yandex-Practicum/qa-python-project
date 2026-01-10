import pytest
from database import Database

class TestDatabase:
    def test_init_quantity(self):
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    @pytest.mark.parametrize('bun_index, expected_name, expected_price',
                             [(0, "black bun", 100),
                              (1, "white bun", 200),
                              (2, "red bun", 300)])
    def test_init_database_buns(self, bun_index, expected_name, expected_price):
        database = Database()
        assert database.buns[bun_index].name == expected_name
        assert database.buns[bun_index].price == expected_price

    @pytest.mark.parametrize('ingredients_index, expected_name, expected_price',
                             [(0, "hot sauce", 100),
                              (1, "sour cream", 200),
                              (2, "chili sauce", 300),
                              (3, "cutlet", 100),
                              (4, "dinosaur", 200),
                              (5, "sausage", 300)])
    def test_init_database_ingredients(self, ingredients_index, expected_name, expected_price):
        database = Database()
        assert database.ingredients[ingredients_index].name == expected_name
        assert database.ingredients[ingredients_index].price == expected_price

    @pytest.mark.parametrize('bun_index, expected_name, expected_price',
                             [(0, "black bun", 100),
                              (1, "white bun", 200),
                              (2, "red bun", 300)])
    def test_available_buns(self, bun_index, expected_name, expected_price):
        database = Database()
        list_bons = database.buns

        assert len(list_bons) == 3

        assert list_bons[bun_index].name == expected_name
        assert list_bons[bun_index].price == expected_price

    @pytest.mark.parametrize('ingredients_index, expected_name, expected_price',
                             [(0, "hot sauce", 100),
                              (1, "sour cream", 200),
                              (2, "chili sauce", 300),
                              (3, "cutlet", 100),
                              (4, "dinosaur", 200),
                              (5, "sausage", 300)])
    def test_available_ingredients(self, ingredients_index, expected_name, expected_price):
        database = Database()
        list_ingredients = database.ingredients

        assert len(list_ingredients) == 6

        assert list_ingredients[ingredients_index].name == expected_name
        assert list_ingredients[ingredients_index].price == expected_price

