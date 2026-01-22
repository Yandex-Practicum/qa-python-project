from praktikum.bun import Bun


class TestBun:
    def test_get_name_bun_one_bun_successful(self):
        bun = Bun("Флюоресцентная булка", 988)
        assert bun.get_name() == "Флюоресцентная булка", "Неправильное имя булочки"

    def test_get_price_bun_one_bun_successful(self):
        bun = Bun("Флюоресцентная булка", 988)
        assert bun.get_price() == 988, "Неправильная цена булочки"
