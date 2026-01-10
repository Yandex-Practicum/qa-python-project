from bun import Bun
from helpers import *


class TestBun:
    def test_get_name_correct_name_exist(self):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    def test_get_price_correct_price_exist(self):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price