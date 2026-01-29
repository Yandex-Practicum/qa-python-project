from praktikum.bun import Bun


def test_bun_init():
    bun = Bun("black bun", 100)
    assert bun.get_name() == "black bun"
    assert bun.get_price() == 100

def test_bun_get_name():
    bun = Bun("white bun", 200)
    assert bun.get_name() == "white bun"

def test_bun_get_price():
    bun = Bun("red bun", 300)
    assert bun.get_price() == 300

def test_bun_init_with_empty_strings_and_zero_price():
    bun = Bun("", 0)
    assert bun.get_name() == ""
    assert bun.get_price() == 0
