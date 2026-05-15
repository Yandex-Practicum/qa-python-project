def test_bun_get_name(bun):
    assert bun.get_name() == "black bun"


def test_bun_get_price(bun):
    assert bun.get_price() == 100