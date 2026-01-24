from conftest import *


class TestBun:
    def test_get_name_bun_success(self, mock_for_the_first_bun):

        assert mock_for_the_first_bun.get_name() == Data.BUN_NAME

    def test_get_price_success(self, mock_for_the_second_bun):

        mock_for_the_second_bun.get_price.return_value = Data_1.PRICE_BUNS
        assert mock_for_the_second_bun.get_price() == Data_1.PRICE_BUNS
