from praktikum.bun import Bun

class TestBun:

    def test_bun_get_name_returns_correct_name(self):
        bun = Bun("Краторная булка Н-200и", 1255)
        assert bun.get_name() == "Краторная булка Н-200и"

    def test_bun_get_price_returns_correct_price(self):
        bun = Bun("Краторная булка Н-200и", 1255)
        assert bun.get_price() == 1255