from practicum.bun import Bun
from practicum.ingredient import Ingredient


class TestDatabase:

    def test_initial_buns(self, db):
        # Проверка наличия начальных булочек в базе данных
        assert len(db.available_buns()) == 3
        assert db.available_buns()[0].name == "black bun"
        assert db.available_buns()[1].name == "white bun"
        assert db.available_buns()[2].name == "red bun"

    def test_initial_ingredients(self, db):
        # Проверка наличия начальных ингредиентов в базе данных
        assert len(db.available_ingredients()) == 6
        assert db.available_ingredients()[0].name == "hot sauce"
        assert db.available_ingredients()[1].name == "sour cream"
        assert db.available_ingredients()[2].name == "chili sauce"
        assert db.available_ingredients()[3].name == "cutlet"
        assert db.available_ingredients()[4].name == "dinosaur"
        assert db.available_ingredients()[5].name == "sausage"

    def test_available_buns_return_type(self, db):
        # Проверка типа возвращаемого значения метода available_buns
        assert isinstance(db.available_buns(), list)
        for bun in db.available_buns():
            assert isinstance(bun, Bun)

    def test_available_ingredients_return_type(self, db):
        # Проверка типа возвращаемого значения метода available_ingredients
        assert isinstance(db.available_ingredients(), list)
        for ingredient in db.available_ingredients():
            assert isinstance(ingredient, Ingredient)

    def test_bun_price(self, db):
        # Проверка цен булочек
        assert db.available_buns()[0].price == 100
        assert db.available_buns()[1].price == 200
        assert db.available_buns()[2].price == 300

    def test_ingredient_price(self, db):
        # Проверка цен ингредиентов
        assert db.available_ingredients()[0].price == 100
        assert db.available_ingredients()[1].price == 200
        assert db.available_ingredients()[2].price == 300
        assert db.available_ingredients()[3].price == 100
        assert db.available_ingredients()[4].price == 200
        assert db.available_ingredients()[5].price == 300
