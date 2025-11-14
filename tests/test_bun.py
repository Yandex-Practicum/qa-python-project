from praktikum.bun import Bun


class TestBun:

    # Проверить, что присвоено имя булочке
    def test_check_get_name_bun(self):
        bun = Bun('Булочка с кунжутом', 120)
        assert bun.get_name() == 'Булочка с кунжутом'

    # Проверить, что Имя это строка
    def test_bun_name_is_string(self):
        bun = Bun('Сырная булочка', 150)
        assert isinstance(bun.name, str)

    # Проверить, что присвоена цена булочке
    def test_check_get_price_bun(self):
        bun = Bun('Булочка с кунжутом', 120)
        assert bun.get_price() == 120

    # Проверить, что цена это число
    def test_bun_price_is_int(self):
        bun = Bun('Сырная булочка', 150)
        assert isinstance(bun.price, int)