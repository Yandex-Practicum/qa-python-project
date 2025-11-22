from praktikum.bun import Bun


class TestBun:

    def test_name_and_price_of_bun_true(self):
        bun = Bun('black bun', 100)
        assert bun.name == 'black bun' and bun.price == 100

    def test_get_name_success(self):
        bun = Bun('black bun', 100)
        assert Bun.get_name(bun) == 'black bun'

    def test_get_price_success(self):
        bun = Bun('black bun', 100)
        assert Bun.get_price(bun) == 100


