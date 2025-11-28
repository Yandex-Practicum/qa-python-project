from praktikum.bun import Bun

class TestBun:
    def test_bun_init_is_name(self):
        bun = Bun(name='Test bun', price=10)
        assert bun.name

    def test_bun_init_is_price(self):
        bun = Bun(name='Test bun', price=10)
        assert bun.price

    def test_bun_get_name_correct(self):
        bun = Bun(name='Test bun', price=10)
        assert bun.get_name() == 'Test bun'

    def test_bun_get_price_correct(self):
        bun = Bun(name='Test bun', price=10)
        assert bun.get_price() == 10