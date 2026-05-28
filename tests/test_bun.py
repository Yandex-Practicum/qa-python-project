from data import BUN_NAME, BUN_PRICE

def test_bun_get_name(bun):
    assert bun.get_name() == BUN_NAME


def test_bun_get_price(bun):
    assert bun.get_price() == BUN_PRICE