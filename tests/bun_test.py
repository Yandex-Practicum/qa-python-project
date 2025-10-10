from praktikum.bun import Bun


class TestBun:

    # тест на получение названия булки
    def test_get_name_true(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    # тест на получение стоимости булки
    def test_get_price_true(self):
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100
