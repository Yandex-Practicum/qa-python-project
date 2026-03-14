from bun import Bun

class TestBun:
    def test_set_name_and_price(self):
        bun = Bun('Bun', 100)

        assert bun.name == 'Bun'
        assert bun.price == 100

    def test_get_name(self):
        bun = Bun('Bun', 100)

        assert bun.get_name() == 'Bun'

    def test_get_price(self):
        bun = Bun('Bun', 300)

        assert bun.get_price() == 300