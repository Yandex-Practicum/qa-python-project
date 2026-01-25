from praktikum.bun import Bun


class TestBunMethods:
    def test_get_name(self):
        bun = Bun('Гослинг', 322)
        assert bun.get_name() == 'Гослинг'

    def test_get_price(self):
        bun = Bun('Гослинг', 322)
        assert bun.get_price() == 322
