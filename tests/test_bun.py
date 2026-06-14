from bun import Bun

class TestBun:
    def test_get_bun_name(self):
        bun = Bun("Метеоритная булка",988)
        assert bun.get_name() == "Метеоритная булка"

    def test_get_bun_price(self):
        bun = Bun("Метеоритная булка",988)
        assert bun.get_price() == 988
