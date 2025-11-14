from praktikum.bun import Bun


class TestBun:

        def test_get_names(self):
            bun = Bun('Кунжут', 50)
            assert bun.get_name() == 'Кунжут'

        def test_get_price(self):
            bun = Bun('Кунжут', 50)
            assert bun.get_price() == 50
