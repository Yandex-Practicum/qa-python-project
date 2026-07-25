from bun import Bun

def test_bun_get_name():
    bun = Bun("Краторная булка", 100)
    assert bun.get_name() == "Краторная булка"

def test_bun_get_price():
    bun = Bun("Краторная булка", 100)
    assert bun.get_price() == 100
