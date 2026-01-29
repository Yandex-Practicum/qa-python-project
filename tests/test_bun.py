class TestBun:
    #Получить наименование булочки
    def test_getter_return_right_name(self, bun):
        assert bun.get_name() == "Булочка"
    #Получить цену
    def test_getter_return_right_price(self, bun):
        assert bun.get_price() == 10.5