from models.bun import Bun
from models.burger import Burger
from models.ingridient import Ingredient
from utils.constants import BUN_BURGER, PRICE_100, PRICE_50, PRICE_75, PRICE_325, INGREDIENT_ONION, TYPE_INGREDIENT, \
    TYPE_SAUCE, SAUCE_MUSTARD, INGREDIENT_BACON


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns(self):
        """Проверяем, что метод set_buns() устанавливает переданную булочку в бургер"""
        burger = Burger()
        bun = Bun(BUN_BURGER, PRICE_100)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        """Проверяем, что метод add_ingredient() добавляет ингредиент в бургер"""
        burger = Burger()
        ingredient = Ingredient(TYPE_INGREDIENT, INGREDIENT_ONION, PRICE_50)
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        """Проверяем, что метод remove_ingredient() удаляет ингредиент из бургера"""
        burger = Burger()
        ingredient1 = Ingredient(TYPE_INGREDIENT, INGREDIENT_ONION, PRICE_50)
        ingredient2 = Ingredient(TYPE_INGREDIENT, INGREDIENT_BACON, PRICE_50)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)

        assert ingredient1 not in burger.ingredients

    def test_move_ingredient(self):
        """Проверяем, что метод move_ingredient() перемещает ингредиент в бургере"""
        burger = Burger()
        ingredient1 = Ingredient(TYPE_INGREDIENT, INGREDIENT_ONION, PRICE_50)
        ingredient2 = Ingredient(TYPE_SAUCE, SAUCE_MUSTARD, PRICE_75)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        """Проверяем, что метод get_price() возвращает правильную цену бургера"""
        burger = Burger()
        bun = Bun(BUN_BURGER, PRICE_100)
        burger.set_buns(bun)
        ingredient1 = Ingredient(TYPE_INGREDIENT, INGREDIENT_ONION, PRICE_50)
        ingredient2 = Ingredient(TYPE_SAUCE, SAUCE_MUSTARD, PRICE_75)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == PRICE_325

    def test_get_receipt(self):
        """Проверяем, что метод get_receipt() возвращает правильный чек бургера"""
        burger = Burger()
        bun = Bun(BUN_BURGER, PRICE_100)
        burger.set_buns(bun)
        ingredient1 = Ingredient(TYPE_INGREDIENT, INGREDIENT_ONION, PRICE_50)
        ingredient2 = Ingredient(TYPE_SAUCE, SAUCE_MUSTARD, PRICE_75)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()

        assert f"(==== {BUN_BURGER} ====)" in receipt
        assert f"= {TYPE_INGREDIENT} {INGREDIENT_ONION} =" in receipt
        assert f"= {TYPE_SAUCE} {SAUCE_MUSTARD} =" in receipt
        assert f"(==== {BUN_BURGER} ====)" in receipt
        assert f"Price: {PRICE_325}" in receipt
