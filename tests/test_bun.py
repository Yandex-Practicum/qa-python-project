from bun import Bun


class TestNamePriceBun:
    def test_name_bun_name(self):
        bun = Bun("Whole Wheat", 3.00)
        assert bun.get_name() == "Whole Wheat"


    def test_name_bun_price(self):
        bun = Bun("Whole Wheat", 3.00)
        assert bun.get_price() == 3.00