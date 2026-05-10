from praktikum.burger import Burger

class TestBurger:
        
    def test_get_price_burger(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_price = (bun_mock.get_price() * 2) + ingredient_mock.get_price()
        assert burger.get_price() == expected_price
