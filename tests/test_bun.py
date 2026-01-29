from ..praktikum.bun import Bun


class TestBun:

    """Тестируем получение названия булочки"""
    def test_get_name_positive(self, bun):
        assert bun.get_name() == bun.name

    """Тестируем получение цены булочки"""
    def test_get_price_positive(self, bun):
        assert bun.get_price() == bun.price

    """Тестируем, что цена булочки представлена в виде float"""
    def test_get_price_name_is_float(self):
        bun = Bun('red bun', 200.1)
        assert isinstance(bun.get_price(), float)

    """Тестируем, что название булочки представлено в виде str"""
    def test_get_name_name_is_str(self, bun):
        assert isinstance(bun.get_name(), str)
