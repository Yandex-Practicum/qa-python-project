from Diplom_1.burger import Burger
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient


class TestBurger:

    def test_burger_bun_true(self):
        burger = Burger()
        assert burger.bun == None

    def test_burger_ingredients_true(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_burger_set_buns_true(self):
        bun = Bun('bread', 50)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient_first_true(self):
        ingredient = Ingredient('SAUCE', 'sweet sauce', 20)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_burger_remove_ingredient_second_true(self):
        ingredient_first = Ingredient('SAUCE', 'sweet sauce', 20)
        ingredient_second = Ingredient('FILLING', 'meat', 100)
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        burger.remove_ingredient(1)
        assert burger.ingredients == [ingredient_first]

    def test_burger_move_ingredient_true(self):
        ingredient_first = Ingredient('SAUCE', 'sweet sauce', 20)
        ingredient_second = Ingredient('FILLING', 'meat', 100)
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_second, ingredient_first]

    def test_burger_get_price_true(self):
        ingredient_first = Ingredient('SAUCE', 'sweet sauce', 20)
        ingredient_second = Ingredient('FILLING', 'meat', 100)
        bun = Bun('bread', 50)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        price = burger.get_price()
        assert price == 220

    def test_burger_get_receipt(self):
        ingredient_first = Ingredient('SAUCE', 'sweet sauce', 20)
        ingredient_second = Ingredient('FILLING', 'meat', 100)
        bun = Bun('bread', 50)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        price = burger.get_price()
        receipt = burger.get_receipt()
        assert (bun.name in receipt and str(ingredient_first.type.lower()) in receipt and ingredient_first.name in receipt and
                str(ingredient_second.type.lower()) in receipt and ingredient_second.name in receipt and bun.name in receipt
                and 'Price' in receipt and str(price) in receipt)
