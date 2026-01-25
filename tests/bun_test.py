class TestBun:

    # проверяем имя булки при создании объекта
    def test_bun_name_true(self, bun):
        assert bun.name == 'bun'

    # проверяем цену булки при создании объекта
    def test_bun_price_true(self, bun):
        assert bun.price == 50

    # проверяем метод запроса имени булки
    def test_get_name_success(self, bun):
        assert bun.get_name() == 'bun'

    # проверяем метод запроса цены булки
    def test_get_price_success(self, bun):
        assert bun.get_price() == 50
