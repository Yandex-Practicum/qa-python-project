from praktikum.bun import Bun


class TestBun:

    def test_name_true(self):
        bun = Bun(name='Краторная булка N-200i',price=1255)
        assert bun.get_name() == 'Краторная булка N-200i'

    def test_price_true(self):
        bun = Bun(name='Краторная булка N-200i',price=1255)
        
        assert bun.get_price() == 1255