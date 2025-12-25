from praktikum.bun import Bun
from constants import Constants


class TestBun:

    # Тестируем метод _init_ и все его значения
    def test_init_bun_name_assigned_name(self):
        bun = Bun(Constants.NAME_STR, Constants.PRICE_FLT)
        assert bun.name == Constants.NAME_STR

    def test_init_bun_price_assigned_price(self):
        bun = Bun(Constants.NAME_STR, Constants.PRICE_FLT)
        assert bun.price == Constants.PRICE_FLT

    #Тестируем методы
    def test_get_bun_name_got_name(self):
        bun = Bun(Constants.NAME_STR, Constants.PRICE_FLT)
        assert bun.get_name() == Constants.NAME_STR

    def test_get_bun_price_got_price(self):
        bun = Bun(Constants.NAME_STR, Constants.PRICE_FLT)
        assert bun.get_price() == Constants.PRICE_FLT

