from praktikum.burger import Burger


class TestBurgers:

     def test_set_bun(self, bun_mock):
         bun = Burger()
         bun.set_buns(bun_mock)
         assert bun.bun == bun_mock

     def test_add_ingridient(self):
         ingridient = Burger()
         ingridient.add_ingredient('соус')
         assert ingridient.ingredients == ['соус']

     def test_remove_ingridient(self):
         ingridient = Burger()
         ingridient.add_ingredient('соус')
         ingridient.remove_ingredient(0)
         assert ingridient.ingredients != ['соус']

     def test_move_ingridient(self, ingridient_mock):
         ingridient = Burger()
         ingridient.add_ingredient(ingridient_mock)
         ingridient.add_ingredient(ingridient_mock)
         ingridient.move_ingredient(0, 1)
         assert ingridient.ingredients[1].get_name() == 'Гарнир'

     def test_get_price(self, bun_mock, ingridient_mock):
         bun = Burger()
         bun.set_buns(bun_mock)
         bun.add_ingredient(ingridient_mock)
         assert bun.get_price() == 30

     def test_get_receipt(self, bun_mock, ingridient_mock):
         bun = Burger()
         bun.set_buns(bun_mock)
         bun.add_ingredient(ingridient_mock)
         assert bun.get_receipt() == '(==== Кунжут ====)\n= соус Гарнир =\n(==== Кунжут ====)\n\nPrice: 30'
