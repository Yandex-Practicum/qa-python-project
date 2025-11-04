from ..bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    def test_get_bun_name_returns_correct_name(self):
        """Проверяет, что метод get_name возвращает корректное название булочки"""
        bun = Bun("Краторная булка N-200i", 1255)

        assert bun.get_name() == "Краторная булка N-200i"

    def test_get_bun_price_returns_correct_price(self):
        """Проверяет, что метод get_price возвращает корректную цену булочки"""
        bun = Bun("Краторная булка N-200i", 1255)

        assert bun.get_price() == 1255