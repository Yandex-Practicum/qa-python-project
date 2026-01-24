from praktikum.bun import Bun
class TestBun:
    bun = Bun('Краторная булка N-200i', 1255)
    def test_bun_initialization(self):
        assert self.bun.name == 'Краторная булка N-200i' and self.bun.price == 1255
    def test_get_name_retuns_name(self):
        assert self.bun.get_name() == 'Краторная булка N-200i'
    def test_get_price_retuns_price(self):
        assert self.bun.get_price() == 1255





