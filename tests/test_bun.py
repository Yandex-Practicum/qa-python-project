from Diplom_1.practikum.bun import Bun

class TestBunMethods:
    def test_get_name(self):
        bun = Bun('Неряха', 2.50)
        assert bun.get_name() == 'Неряха'

    def test_get_price(self):
        bun = Bun('Неряха', 2.50)
        assert bun.get_price() == 2.50

