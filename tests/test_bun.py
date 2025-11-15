import pytest


class TestBun:

    def test_bun_get_name_return_correct_name(self, mock_bun_data):

        assert mock_bun_data.get_name() == "Ржаная"

    def test_bun_get_price_return_correct_price(self, mock_bun_data):
   
        assert mock_bun_data.get_price() == 150