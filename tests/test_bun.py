class TestBun:

    def test_name_of_bun_true(self, mock_bun_name_price):
        bun = mock_bun_name_price
        assert bun.name == "black bun"

    def test_price_of_bun_true(self, mock_bun_name_price):
        bun = mock_bun_name_price
        assert bun.price == 100

    def test_get_name_get_correct_name(self, mock_bun_name_price):
        bun = mock_bun_name_price
        assert bun.get_name() == "black bun"

    def test_get_price_get_correct_price(self, mock_bun_name_price):
        bun = mock_bun_name_price
        assert bun.get_price() == 100