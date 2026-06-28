
from bun import Bun

class TestBun:

    def test_get_name_returns_correct_value(self):
        bun = Bun("test_bun", 999.99)
        assert bun.get_name() == "test_bun"

    def test_get_price_returns_correct_value(self):
        bun = Bun("test_bun", 999.99)       
        assert bun.get_price() == 999.99

