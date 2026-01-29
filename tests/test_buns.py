from praktikum.bun import Bun
from praktikum.database import Database


# В тест-сете присутсвуют тесты на проверку получения данных из базы данных
class TestBuns:

    def test_bun_get_name(self):
        bun = Bun('Флюоресцентная булка', 988)
        assert bun.get_name() == 'Флюоресцентная булка'

    def test_bun_get_price(self):
        bun = Bun('Краторная булка', 1255)
        assert bun.get_price() == 1255

    def test_bun_from_database_get_name(self):
        database = Database()
        buns_list = database.available_buns()
        current_bun = buns_list[0]
        assert current_bun.get_name() == 'black bun'

    def test_bun_from_database_get_price(self):
        database = Database()
        buns_list = database.available_buns()
        current_bun = buns_list[0]
        assert current_bun.get_price() == 100



