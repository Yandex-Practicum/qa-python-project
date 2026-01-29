from praktikum.bun import Bun


class TestBun:

    @classmethod
    def setup_class(cls):
        cls.buns = Bun('Флюоресцентная булка R2-D3', 988)


    def test_get_bun_name_success_result(self):
        result = self.buns.get_name()
        assert 'Флюоресцентная булка R2-D3' == result, 'Вернулось неправильное имя'


    def test_get_bun_price_success_result(self):
        result = self.buns.get_price()
        assert 988 == result, 'Вернулась неправильная цена'
