from praktikum.bun import Bun


class TestBun:

    def test_get_name_successful(self, bun):
        assert bun.get_name() == 'Bulka'

    def test_get_price_successful(self, bun):
        assert bun.get_price() == 50
