import pytest
from praktikumm.bun import Bun

def test_bun_get_name():
    bun = Bun("white", 200)
    assert bun.get_name() == "white"

def test_bun_get_price():
    bun = Bun("black", 100)
    assert bun.get_price() == 100