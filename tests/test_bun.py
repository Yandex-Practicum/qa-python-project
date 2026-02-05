from data import BUN_DATA


class TestBun:

    def test_get_name(self, bun_fixture):
        bun_name = bun_fixture.get_name()
        assert bun_name == list(BUN_DATA.keys())[0]

    def test_get_price(self, bun_fixture):
        bun_price = bun_fixture.get_price()
        assert bun_price == BUN_DATA[list(BUN_DATA.keys())[0]]