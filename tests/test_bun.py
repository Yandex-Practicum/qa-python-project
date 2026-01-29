from praktikum.bun import Bun


class TestBun:

    def test_get_name_return_bun_name(self):
        bun = Bun('black bun', 100)
        assert bun.get_name() == "black bun", 'Unable to get bun name'

    def test_get_price_return_bun_prise(self):
        bun = Bun('black bun', 100)
        assert bun.get_price() == 100, 'Unable to get bun price'
