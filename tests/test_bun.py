class TestBun:
    def test_correct_name(self, bun):
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_correct_price(self, bun):
        assert bun.get_price() == 988

    
