from praktikum.bun import Bun

class TestBun:

    def test_bun_initialization_price(self):
        bun = Bun('булочка с маком', 200)
        assert bun.get_price() == 200

    def test_bun_initialization_name(self):
        bun = Bun('булочка с маком', 200)
        assert bun.get_name() == 'булочка с маком'
