from praktikum.bun import Bun
import pytest

class TestBun:

    def test_get_name_bun(self):
        bun = Bun('New bun', 33.33)

        assert bun.get_name() == 'New bun'

    def test_get_price_bun(self):
        bun = Bun('New bun', 100.45)

        assert bun.get_price() == 100.45


    @pytest.mark.parametrize('name, price',
                                 [['Tasty and soft', 99.99],
                                  ['Super bun', 5.05],
                                  ['Small bun', 0.10],
                                  ['Big bun', 100500] ])
    def test_make_bun_correct_data(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name and bun.get_price() == price

    @pytest.mark.parametrize('name, price',
                             [ ['Tasty and soft', -50.50],
                               ['', 10.05],
                               ['Small bun', 0.0] ] )
    def test_make_bun_incorrect_data(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name and bun.get_price() == price