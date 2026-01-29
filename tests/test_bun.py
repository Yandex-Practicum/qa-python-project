from praktikum.bun import Bun

class TestBun:

    def test_get_name_correct_mane(self):       # Проверка названия бургера
        bun = Bun('MyOwnBun', 100.25)
        assert bun.get_name() == "MyOwnBun"

    def test_get_price_correct_price(self):     # Проверка цены бургера
        bun = Bun('MyOwnBun', 100.25)
        assert bun.get_price() == 100.25
