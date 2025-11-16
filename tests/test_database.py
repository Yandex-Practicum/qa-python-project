import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:


    @pytest.mark.parametrize('name,price',
                             [("black bun", 100),
                              ("white bun", 200),
                              ("red bun", 300)
                             ])
    def test_database_bun_list_true(self,database,name,price):
        database.buns.append((name, price))
        assert (name, price) in database.buns


    @pytest.mark.parametrize('ingredient_type,name,price',
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                              (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                              (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                              (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                              (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                              (INGREDIENT_TYPE_FILLING, "sausage", 300)
                             ])
    def test_database_ingredient_list_true(self, database, ingredient_type, name, price):
        database.ingredients.append((ingredient_type, name, price))
        assert (ingredient_type, name, price) in database.ingredients


    def test_database_available_buns_check_true(self, database):
        database.buns.append(("white bun", 200))
        assert ("white bun", 200) in database.available_buns()


    def test_database_available_ingredients_check_true(self, database):
        database.ingredients.append((INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        assert (INGREDIENT_TYPE_SAUCE, "hot sauce", 100) in database.available_ingredients()
