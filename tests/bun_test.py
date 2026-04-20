

class TestBun:

    def test_get_name_bun(self, bun):
        bun_obj, name = bun[0], bun[1]
        assert bun_obj.get_name() == name

    def test_get_price_bun(self, bun):
        bun_obj, price = bun[0], bun[2]
        assert bun_obj.get_price() == price
