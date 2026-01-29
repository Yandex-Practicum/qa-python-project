from praktikum.bun import Bun


class TestBun:
    def test_get_name_correct_name_success(self):
        bun = Bun('TestName', 100)

        assert bun.get_name() == 'TestName'

    def test_get_price_correct_price_success(self):
        bun = Bun('TestName', 100)

        assert bun.get_price() == 100
