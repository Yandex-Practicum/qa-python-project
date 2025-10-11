from praktikum.bun import Bun
from test_data import Data

class TestBun():

    # Тест init
    def test_bun_initialization(self):
        name = Data.BUN_NAME
        price = Data.BUN_PRICE
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    # Тест метода get_name
    def test_get_name_return_correct_price(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME

    # Тест метода get_price
    def test_get_price_return_correct_price(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE
