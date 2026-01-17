from praktikum.bun import Bun


class TestBun:
    def test_get_name_correct_name(self):
        new_bun = Bun('булка "Студенческая"', 10)
        assert new_bun.get_name() == 'булка "Студенческая"'

    def test_get_price_correct_price(self):
        new_bun = Bun('булка "Студенческая"', 10)
        assert new_bun.get_price() == 10