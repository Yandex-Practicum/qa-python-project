from praktikum.database import Database
from conftest import database_object


class TestDatabase:

    def test_available_buns_get_full_list(self, database_object):
        assert database_object.available_buns == ['dd']
