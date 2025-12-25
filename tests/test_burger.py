
from praktikum.burger import Burger
from constants import Constants

class TestBurger:

    #Тестируем метод init
    def test_init_bun_assigned_bun(self):
        burger = Burger()
        assert burger.bun == None

    def test_init_ingredients_assigned_ingredients(self):
        burger = Burger()
        assert burger.ingredients == []

    #Тестируем методы класса бургер

    def test_set_buns_got_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_got_ingredients(self, burger, burger_ingredients):
        burger.add_ingredient(burger_ingredients)
        assert burger.ingredients[0] == burger_ingredients

    def test_remove_ingredient_got_del_ingredient(self, burger, ingredients):
        burger.ingredients = ingredients
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == Constants.INGREDIENTS_SAUCE2

    def test_move_ingredient_got_ingredient_new_index(self, burger, ingredients):
        burger.ingredients = ingredients
        burger.move_ingredient(0,2)
        assert burger.ingredients[2] == Constants.INGREDIENTS_SAUCE



