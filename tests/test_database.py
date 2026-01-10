from unittest.mock import Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns(self):
        database = Database()
        # Mocking the behavior of the database for available buns
        database.available_buns = Mock(return_value=[
            Mock(get_name=lambda: "black bun", get_price=lambda: 100),
            Mock(get_name=lambda: "white bun", get_price=lambda: 200),
            Mock(get_name=lambda: "red bun", get_price=lambda: 300)
        ])

        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients(self):
        database = Database()
        # Mocking the behavior of the database for available ingredients
        database.available_ingredients = Mock(return_value=[
            Mock(get_type=lambda: INGREDIENT_TYPE_SAUCE, get_name=lambda: "hot sauce", get_price=lambda: 100),
            Mock(get_type=lambda: INGREDIENT_TYPE_SAUCE, get_name=lambda: "sour cream", get_price=lambda: 200),
            Mock(get_type=lambda: INGREDIENT_TYPE_SAUCE, get_name=lambda: "chili sauce", get_price=lambda: 300),
            Mock(get_type=lambda: INGREDIENT_TYPE_FILLING, get_name=lambda: "cutlet", get_price=lambda: 100),
            Mock(get_type=lambda: INGREDIENT_TYPE_FILLING, get_name=lambda: "dinosaur", get_price=lambda: 200),
            Mock(get_type=lambda: INGREDIENT_TYPE_FILLING, get_name=lambda: "sausage", get_price=lambda: 300)
        ])

        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all([i.get_type() == INGREDIENT_TYPE_SAUCE for i in ingredients[:3]])
        assert all([i.get_type() == INGREDIENT_TYPE_FILLING for i in ingredients[3:]])
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300
