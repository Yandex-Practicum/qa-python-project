from praktikum.bun import Bun
from constsnts import Constants


class TestBun:  # Для проверки методов использовал фикстуру, для проверки атрибутов - явные данные.

    def test_attribute_name_bun_true(self):

        bun = Bun(name="Булка", price=2)
        assert bun.name == "Булка"

    def test_attribute_price_bun_true(self):

        bun = Bun(price=5.7, name="Булка")
        assert bun.price == 5.7

    def test_get_name_bun_successful(self, bun_fix):

        assert bun_fix.get_name() == Constants.BUN

    def test_get_price_bun_successful(self, bun_fix):

        assert bun_fix.get_price() == Constants.BUT_PRICE
