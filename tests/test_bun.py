from praktikum.bun import Bun
from praktikum.database import Database

class TestBun:
    def test_bun_init_is_name(self):
        db = Database()
        bun = Bun(db.buns[0].name, db.buns[0].price)
        assert bun.name, 'У булки не инициализирован атрибут name'

    def test_bun_init_is_price(self):
        db = Database()
        bun = Bun(db.buns[0].name, db.buns[0].price)
        assert bun.price, 'У булки не инициализирован атрибут price'

    def test_bun_get_name_correct(self):
        db = Database()
        bun = Bun(db.buns[0].name, db.buns[0].price)
        bun_name = db.buns[0].name
        assert bun.get_name() == bun_name, 'Вернулось некорректное имя булки'

    def test_bun_get_price_correct(self):
        db = Database()
        bun = Bun(db.buns[0].name, db.buns[0].price)
        bun_price = db.buns[0].price
        assert bun.get_price() == bun_price, 'Вернулась некорректная цена булки'