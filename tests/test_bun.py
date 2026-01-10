from praktikum.bun import Bun


class TestBun:
    def test_comparison_bun_name(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_name() == "Краторная булка N-200i"

    def test_comparison_bun_price(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_price() == 1255