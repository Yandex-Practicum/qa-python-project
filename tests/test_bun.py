import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bun import Bun

class TestBun:

    bun = Bun("testBun", "99.5")

    def test_bun_init(self):
        assert self.bun.name == "testBun"
        assert self.bun.price == "99.5"

    def test_bun_get_name(self):
        assert self.bun.get_name() == "testBun"

    def test_bun_get_price(self):
        assert self.bun.get_price() == "99.5"