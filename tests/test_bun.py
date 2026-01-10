from praktikum.bun import Bun


class TestBun:

    def test_get_name_returns_name(self):
        expected_name = "Name"
        bun = Bun(expected_name, 1.0)
        assert bun.get_name() == expected_name

    def test_get_price_returns_price(self):
        expected_price = 1.0
        bun = Bun("Name", expected_price)
        assert bun.get_price() == expected_price

