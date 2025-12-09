from praktikum.database import Database


class TestDatabase:

    def test_init_bun_list_true(self):
        database = Database()

        assert database.buns[0].name == "black bun" and database.buns[0].price == 100
        assert database.buns[1].name == "white bun" and database.buns[1].price == 200
        assert database.buns[2].name == "red bun" and database.buns[2].price == 300

    def test_init_ingredients_list_true(self):
        database = Database()

        assert database.ingredients[0].name == "hot sauce" and database.ingredients[0].price == 100
        assert database.ingredients[1].name == "sour cream" and database.ingredients[1].price == 200
        assert database.ingredients[2].name == "chili sauce" and database.ingredients[2].price == 300
        assert database.ingredients[3].name == "cutlet" and database.ingredients[3].price == 100
        assert database.ingredients[4].name == "dinosaur" and database.ingredients[4].price == 200
        assert database.ingredients[5].name == "sausage" and database.ingredients[5].price == 300