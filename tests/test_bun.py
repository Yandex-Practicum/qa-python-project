from praktikum.bun import Bun
from data import TestData

class TestBun:
    def test_get_name_bun(self):
        # проверяем, что булочке можно присвоить имя
        bun = Bun(TestData.bun_name, TestData.bun_price)
        assert bun.get_name() == TestData.bun_name, 'Название булки не получено'

    def test_get_price(self):
        # проверяем, что булочке можно присвоить стоимость
        bun = Bun(TestData.bun_name, TestData.bun_price)
        assert bun.get_price() == TestData.bun_price, 'Стоимость булки не получена'