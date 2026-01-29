from praktikum.database import Database


class TestDatabase:

    def test_type_of_list_buns_is_list(self, super_database):
        assert type(super_database.buns) == list


    def test_type_of_list_ingridients_is_list(self, super_database):
        assert type(super_database.ingredients) == list


    def test_available_buns_list_len(self, super_database):
        assert len(super_database.available_buns()) == 3


    def test_available_ingridients_list_len(self, super_database):
        assert len(super_database.available_ingredients()) == 6






