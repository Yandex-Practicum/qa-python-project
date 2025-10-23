from data.test_data import BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE


class TestBun:

    def test_get_bun_name(self, bun):
        assert bun.get_name() == BUN_VALID_NAME, f'Имя булочки не соответствует ожидаемому'

    def test_get_bun_price(self, bun):
        assert bun.get_price() == BUN_VALID_FLOAT_PRICE, 'Цена булочки не соответствует ожидаемой'

    def test_get_bun_name_return_str(self, bun):
        assert isinstance(bun.get_name(), str), 'Метод get_name вернул не строку'

    def test_get_bun_price_return_float(self, bun):
        assert isinstance(bun.get_price(), float), 'Метод get_price вернул не число с плавающей точкой'
