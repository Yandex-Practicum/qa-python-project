
def test_burger_set_bun_burger_has_bun(burger, bun_mock):
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock
