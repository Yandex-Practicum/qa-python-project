from data import MakeBurger as mb 
from bun import Bun

class TestBun:
    
    def test_get_name(self):
        bun = Bun(mb.BUN_NAME, mb.BUN_PRICE) 
        assert bun.get_name() == mb.BUN_NAME
  
    def test_get_price(self):
        bun = Bun(mb.BUN_NAME, mb.BUN_PRICE)
        assert bun.get_price == mb.BUN_PRICE 
        