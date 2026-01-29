from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        expected_name = "Test BUN_name"
        bun = Bun(expected_name, 100.0)
        assert bun.get_name() == expected_name

    def test_bun_get_price(self):
        expected_price = 100.0
        bun = Bun("Test BUN_name", expected_price)
        assert bun.get_price() == expected_price
