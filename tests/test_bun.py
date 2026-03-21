from bun import Bun

class TestBun:
    def test_initialization_sets_name_attribute(self):
        bun = Bun('Black Bun', 100)
        assert bun.name == 'Black Bun'

    def test_initialization_sets_price_attribute(self):
        bun = Bun('White Bun', 200)
        assert bun.price == 200

    def test_get_name_returns_correct_value(self):
        bun = Bun('Red Bun', 150)
        assert bun.get_name() == 'Red Bun'

    def test_get_price_returns_correct_value(self):
        bun = Bun('Golden Bun', 300)
        assert bun.get_price() == 300