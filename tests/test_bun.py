from Diplom_1.bun import Bun


class TestBun:

    def test_bun_name_true(self):
        bun = Bun('bread', 0)
        assert bun.name == 'bread'

    def test_bun_price_true(self):
        bun = Bun('lavash', 150)
        assert bun.price == 150

    def test_bun_get_name_true(self):
        bun = Bun('bagel', 200)
        assert bun.get_name() == 'bagel'

    def test_bun_get_price_true(self):
        bun = Bun('bulka', 100)
        assert bun.get_price() == 100
