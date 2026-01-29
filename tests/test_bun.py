from data import TEST_BUNS
from praktikum.bun import Bun


class TestBun:
    def test_get_name_returns_name(self):
        bun_data = TEST_BUNS[0]
        bun = Bun(bun_data['name'], bun_data['price'])
        result = bun.get_name()

        assert result == bun_data['name'], f'Ожидалось "{bun_data["name"]}", получили {result}'

    def test_get_price_returns_price(self):
        bun_data = TEST_BUNS[1]
        bun = Bun(bun_data['name'], bun_data['price'])
        result = bun.get_price()

        assert result == bun_data['price'], f'Ожидалось "{bun_data["price"]}", получили {result}'
