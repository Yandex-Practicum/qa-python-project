from tests.data import MockBun


class TestBun:
    def test_bun_create(self, mok_bun):
        assert mok_bun.get_name() == MockBun.NAME

    def test_bun_create_price(self, mok_bun):
        assert mok_bun.get_price() == MockBun.PRICE
