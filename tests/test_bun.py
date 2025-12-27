from praktikum.bun import Bun

class TestBun:
    def test_get_name_correct_true(self):
        bun = Bun('test bun', 100)
        assert bun.get_name() == 'test bun'

    def test_get_price_correct_true(self):
        bun = Bun('test_bun', 100)
        assert bun.get_price() == 100