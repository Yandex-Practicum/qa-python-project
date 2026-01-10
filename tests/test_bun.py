from praktikum.bun import Bun


class TestBun:

    def test_get_name_positive(self):
        bun = Bun(name='Флюоресцентная булка', price=25.5)
        assert bun.get_name() == 'Флюоресцентная булка'

    def test_get_price_positive(self):
        bun = Bun(name='Флюоресцентная булка', price=25.5)
        assert bun.get_price() == 25.5
