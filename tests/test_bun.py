

class TestBun:

    def test_get_name_returns_name(self,mock_bun):#позитивный тест. Возвращает Присвоенное в Bun имя
        bun_name = mock_bun.get_name()
        assert bun_name == 'bun1'

    def test_get_name_returns_price(self,mock_bun):#позитивный тест. Возвращает Присвоенную в Bun цену
        bun_price = mock_bun.get_price()
        assert bun_price == 1000

