from praktikum.database import Database


class TestForDatabase:

    def test_database_available_buns(self):
        database =Database()
        db_names = database.available_buns()
        names = ["black bun", "white bun", "red bun"]
        getting_names = []
        for bun in db_names:
            get_name= bun.get_name()
            getting_names.append(get_name)
        assert names == getting_names


    def test_database_available_ingredients(self):
        database =Database()
        db_names = database.available_ingredients()
        names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        getting_names = []
        for bun in db_names:
            get_name= bun.get_name()
            getting_names.append(get_name)
        assert names == getting_names
