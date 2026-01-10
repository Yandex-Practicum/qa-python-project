import pytest
from source_code.bun import Bun
from data.data import ORDER_DATA_CORRECT


class TestBun:

     @pytest.mark.parametrize("order_data", ORDER_DATA_CORRECT)
     def test_bun_name(self, order_data):
          bun = Bun(order_data["bun_name"], order_data["bun_price"])
          assert bun.get_name() == order_data["bun_name"] and isinstance(order_data["bun_name"], str)

     @pytest.mark.parametrize("order_data", ORDER_DATA_CORRECT)
     def test_bun_price(self, order_data):
          bun = Bun(order_data["bun_name"], order_data["bun_price"])
          assert bun.get_price() == order_data["bun_price"] and isinstance(order_data["bun_price"], float)
