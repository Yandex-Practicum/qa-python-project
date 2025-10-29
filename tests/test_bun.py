from praktikum.bun import Bun
class TestBun:

    """ Тест на получение наименования """
    def test_get_correct_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 777)
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    """ Тест на получение прайса """
    def test_get_correct_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 777)
        assert bun.get_price() == 777