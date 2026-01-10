from praktikum.bun import Bun
from data import Data


class TestBun:
    def test_bun_create_object_successful(self):
        bun = Bun(name=Data.bun.get('name'), price=Data.bun.get('price'))
        assert bun.name == Data.bun.get('name') and bun.price == Data.bun.get('price')

    def test_get_name_successful(self, awesome_bun):
        assert awesome_bun.get_name() == awesome_bun.name

    def test_get_price_name_successful(self, awesome_bun):
        assert awesome_bun.get_price() == awesome_bun.price


