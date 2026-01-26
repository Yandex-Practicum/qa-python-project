class TestBun:

    def test_get_name_success(self,buns):
        result = buns.get_name()
        assert result == "black bun"

    def test_get_price_success(self,buns):
        result = buns.get_price()
        assert result == 100

