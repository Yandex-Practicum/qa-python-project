from data import BUN_NAME, BUN_PRICE


class TestBun:

    def test_get_name(self, bun_fixture):
        bun_name = bun_fixture.get_name()
        assert bun_name == BUN_NAME

    def test_get_price(self, bun_fixture):
        bun_price = bun_fixture.get_price()
        assert bun_price == BUN_PRICE