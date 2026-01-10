from data import Data


# Проверки Bun отдельно, без моков
class TestBun:
    def test_get_name_bun_return_name_bun(self, mock_bun):
        name = mock_bun.get_name()

        assert name == Data.BUN_NAME

    def test_get_price_bun_return_price_bun(self, mock_bun):
        price = mock_bun.get_price()

        assert price == Data.BUN_PRICE
