from data import *


class TestBun:

    def test_get_name(self, bun):
        assert bun.get_name() == 'Briosh'

    def test_get_price(self, bun):
        assert bun.get_price() == 100