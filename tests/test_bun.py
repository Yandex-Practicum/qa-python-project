from data import VERIFICATION_NAME, VERIFICATION_PRICE


class TestBun:

    def test_bun_initialization(self, bun):
        # тест корректности инициализации булочки
        assert bun.name == VERIFICATION_NAME
        assert bun.price == VERIFICATION_PRICE

    def test_bun_get_name(self, bun):
        # тест получения названия булочки
        assert bun.get_name() == VERIFICATION_NAME
        assert isinstance(bun.get_name(),str)

    def test_bun_get_price(self, bun):
        # тест получения цены булочки
        assert bun.get_price() == VERIFICATION_PRICE
        assert isinstance(bun.get_price(),float)