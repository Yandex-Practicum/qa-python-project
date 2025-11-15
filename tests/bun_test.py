from data import test_data

class TestBun:
    def test_get_name(self, bun):
        assert bun.get_name() == test_data.BUN_NAME

    def test_get_price(self, bun):
        assert bun.get_price() == test_data.BUN_PRICE
