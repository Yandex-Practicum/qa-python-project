class TestBun():

    def test_get_name(self, create_bun):
        assert create_bun.get_name() == "Test Bun"

    def test_get_price(self, create_bun):
        assert create_bun.get_price() == 10.5

