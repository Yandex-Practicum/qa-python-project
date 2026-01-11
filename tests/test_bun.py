from practikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        bun = Bun('White',100.5)
        actual_name = bun.get_name()

        assert actual_name == 'White'

    def test_bun_get_price(self):
        bun = Bun('White', 100.5)
        actual_price = bun.get_price()

        assert actual_price == 100.5


