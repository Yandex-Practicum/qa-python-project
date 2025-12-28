from Diplom_1.database import Database
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns(self):
        dt=Database()
        assert len(dt.available_buns()) == 3
        buns = dt.available_buns()
        assert buns[0].name == "black bun"
        assert buns[0].price == 100
        assert buns[1].name == "white bun"
        assert buns[1].price == 200
        assert buns[2].name == "red bun"
        assert buns[2].price == 300
    def test_available_ingredients(self):
        dt = Database()
        ingredients = dt.available_ingredients()
        assert len(dt.available_ingredients()) == 6
        assert ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].name == "hot sauce"
        assert ingredients[0].price == 100
        assert ingredients[1].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].name == "sour cream"
        assert ingredients[1].price == 200
        assert ingredients[2].type == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].name == "chili sauce"
        assert ingredients[2].price == 300
        assert ingredients[3].type == INGREDIENT_TYPE_FILLING
        assert ingredients[3].name == "cutlet"
        assert ingredients[3].price == 100
        assert ingredients[4].type == INGREDIENT_TYPE_FILLING
        assert ingredients[4].name == "dinosaur"
        assert ingredients[4].price == 200
        assert ingredients[5].type == INGREDIENT_TYPE_FILLING
        assert ingredients[5].name == "sausage"
        assert ingredients[5].price == 300


