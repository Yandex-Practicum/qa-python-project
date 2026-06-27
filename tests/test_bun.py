import data

class TestBun:
    def test_get_name(self, bun):
        result = bun.get_name()
        assert isinstance(result, str) and result == data.BUN_NAME
    
    def test_get_price(self, bun):
        result = bun.get_price()
        assert isinstance(result, float) and result == data.BUN_PRICE
