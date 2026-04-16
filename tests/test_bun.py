import data


class TestBun:
    def test_get_name_success(self, bun):
        assert bun.get_name() == data.bun_name

    def test_get_price_success(self, bun):
        assert bun.get_price() == data.bun_price
