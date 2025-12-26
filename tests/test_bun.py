import generators_data
from praktikum.bun import Bun

class TestBun:

    def test_get_name(self):
        name = generators_data.generate_random_bun_name()
        price = generators_data.generate_random_bun_price()
        bun = Bun(name, price)

        assert bun.get_name() == name

    def test_get_price(self):
        name = generators_data.generate_random_bun_name()
        price = generators_data.generate_random_bun_price()
        bun = Bun(name, price)

        assert bun.get_price() == price