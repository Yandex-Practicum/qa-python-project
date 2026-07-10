
from bun import Bun



class TestBun:

    def test_get_name(self):
        bun = Bun("Белая булка", 100)
        assert bun.get_name() == "Белая булка"

    def test_get_price(self):
        bun = Bun("Белая булка", 100)
        assert bun.get_price() == 100