from data import BUN_PARAMS


class TestBun():

    # проверка получения наименования булки
    def test_get_name(self, bun):
        bun_name = bun.get_name() # получаем наименование булки
        assert bun_name == BUN_PARAMS['name'] and type(bun_name) == str # проверяем соответствие наименования булки

    # проверка получения цены булки
    def test_get_price(self, bun):
        bun_price = bun.get_price()#получаем цену булки
        assert bun_price == BUN_PARAMS['price'] and type(bun_price) == float #проверяем соответствие цены
