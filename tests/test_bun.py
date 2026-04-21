from praktikum.bun import Bun


class TestBun:
    
    def test_get_name_returns_correct_bun_name(self):
        bun = Bun("Краторная булка N-200i", 100.0)
        assert bun.get_name() == "Краторная булка N-200i"
    
    def test_get_price_returns_correct_bun_price(self):
        bun = Bun("Краторная булка N-200i", 200.5)
        assert bun.get_price() == 200.5