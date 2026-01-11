from bun import Bun
from burger import Burger
from ingredient import Ingredient
from unittest.mock import patch


class TestBurger:

    def test_init_bun(self):
        burger = Burger()
        assert burger.bun == None

    def test_init_ingredients(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns('Пшеничная')
        assert burger.bun == 'Пшеничная'

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Соус Гуакамоле')
        burger.add_ingredient('Котлета с пюрешкой')
        assert burger.ingredients == ['Соус Гуакамоле', 'Котлета с пюрешкой']


    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Соус Гуакамоле')
        burger.add_ingredient('Котлета с пюрешкой')
        burger.remove_ingredient(0)
        assert burger.ingredients == ['Котлета с пюрешкой']


    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient('Соус Гуакамоле')
        burger.add_ingredient('Котлета с пюрешкой')
        burger.add_ingredient('Чавапчичи')
        burger.move_ingredient(1, 2)
        assert burger.ingredients == ['Соус Гуакамоле', 'Чавапчичи', 'Котлета с пюрешкой']


    @patch('ingredient.Ingredient.get_price', return_value=100)
    @patch('bun.Bun.get_price', return_value=100)
    def test_burger_get_price(self, mock_get_bun_price, mock_get_ingredients_price):
        burger = Burger()
        bun = Bun('сладкий хлеб', 1000000)
        sauce = Ingredient('соус', 'кетчунез', 10425432432)
        meat = Ingredient('мясо', 'котлетос', 20432432420)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(meat)
        burger.get_price()
        assert burger.get_price() == 400


    def test_burger_get_receipt(self):
        burger = Burger()
        bun = Bun('сладкий хлеб', 200)
        meat = Ingredient('meat', 'котлета с пюрешкой', 500)
        burger.set_buns(bun)
        burger.add_ingredient(meat)
        assert burger.get_receipt() == """(==== сладкий хлеб ====)
= meat котлета с пюрешкой =
(==== сладкий хлеб ====)

Price: 900"""








