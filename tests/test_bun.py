from data import BunData


class TestBun:

    def test_give_new_name_bun(self, set_data_bun):
        assert set_data_bun.get_name() == BunData.bun_name

    def test_set_new_price_bun(self, set_data_bun):
        assert set_data_bun.get_price() == BunData.bun_price
