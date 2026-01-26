from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('sweet_bun', 88)
        assert bun.get_name() == 'sweet_bun'

    def test_get_price(self):
        bun = Bun('sweet_bun', 88)
        assert bun.get_price() == 88

        


