from Diplom_1.database import Database
import pytest

class TestDatabase:

    @pytest.mark.parametrize('i, name, price',[[0, 'black bun', 100], [1, 'white bun', 200], [2, 'red bun', 300]])
    def test_database_creation_buns_true(self, i, name, price):
        database = Database()
        assert database.buns[i].name == name and database.buns[i].price == price

    @pytest.mark.parametrize('i, type, name, price', [[0, 'SAUCE', "hot sauce", 100], [1, 'SAUCE', 'sour cream', 200],
                                                      [2, "SAUCE", 'chili sauce', 300], [3, "FILLING", "cutlet", 100],
                                                      [4, "FILLING", "dinosaur", 200], [5, "FILLING", "sausage", 300]])
    def test_database_creation_ingredients_true(self, i, type, name, price):
        database = Database()
        assert (database.ingredients[i].type == type and database.ingredients[i].name == name and
                database.ingredients[i].price == price)

    @pytest.mark.parametrize('i, name, price', [[0, 'black bun', 100], [1, 'white bun', 200], [2, 'red bun', 300]])
    def test_database_available_buns_true(self, i, name, price):
        database = Database()
        assert len(database.available_buns()) == 3 and database.buns[i].name == name and database.buns[i].price == price

    @pytest.mark.parametrize('i, type, name, price', [[0, 'SAUCE', "hot sauce", 100], [1, 'SAUCE', 'sour cream', 200],
                                                      [2, "SAUCE", 'chili sauce', 300], [3, "FILLING", "cutlet", 100],
                                                      [4, "FILLING", "dinosaur", 200], [5, "FILLING", "sausage", 300]])
    def test_database_available_ingredients_true(self, i, type, name, price):
        database = Database()
        assert (len(database.available_ingredients()) == 6 and database.ingredients[i].type == type and database.ingredients[i].name == name and
                database.ingredients[i].price == price)

