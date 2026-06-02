from bun import Bun

class TestBun:

    def test_get_name_returns_name(self):
        bun = Bun("Aff", 23)
        assert bun.get_name() == "Aff"

    def test_get_price_return_price(slf):
        bun = Bun("OJH", 100.00)
        assert bun.get_price()==100.00

        