
from bun import Bun

class TestBunMethods:

    def test_bun_name_true(self):
        bun_name = Bun("black bun", 50)

        assert  bun_name.name == "black bun"

    def test_bun_price_true(self):
        bun_name = Bun("black bun", 100)

        assert bun_name.price == 100

    def test_bun_get_name_true(self):
        bun_name = Bun("black bun", 50)

        assert bun_name.get_name()  == "black bun"

    def test_bun_get_price_true(self):
        bun_name = Bun("black bun", 100)

        assert bun_name.get_price() == 100


