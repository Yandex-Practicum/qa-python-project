from praktikum.bun import Bun
from data import DataTestBun

class TestBun:
    def test_get_name_create_new_bun_check_name(self):
        new_bun = Bun(*DataTestBun.bun_test_data)
        assert new_bun.get_name() == DataTestBun.bun_test_data[0]

    def test_get_name_create_new_bun_check_price(self):
        new_bun = Bun(*DataTestBun.bun_test_data)
        assert new_bun.get_price() == DataTestBun.bun_test_data[1]
