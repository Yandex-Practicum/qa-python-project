import pytest
from praktikum.burger import Burger
from tests.data import MockBun, MockIngredient, MockIngredient2


class TestBurger:
    def test_set_buns(self, mok_bun):
        burger = Burger()
        burger.set_buns(mok_bun)

        assert burger.bun.get_name() == MockBun.NAME
        assert burger.bun.get_price() == MockBun.PRICE

    @pytest.mark.parametrize('ingred_name, ingred_price, ingred_type', [
        ('Говяжий метеорит', 100, 'начинка'),
        ('Соус из квантовых черных дыр', 50, 'соус'),
        ('Жареные личинки', 75, 'начинка')
    ])
    def test_add_ingredient(self, mok_ingredient, mok_ingredient_2, ingred_name, ingred_price, ingred_type):
        burger = Burger()

        # Добавляем два ингредиента
        burger.add_ingredient(mok_ingredient)
        burger.add_ingredient(mok_ingredient_2)
        assert burger.ingredients == [mok_ingredient, mok_ingredient_2]

    def test_remove_ingredient(self, mok_ingredient, mok_ingredient_2):
        burger = Burger()

        # Добавляем два ингредиента
        burger.add_ingredient(mok_ingredient)
        burger.add_ingredient(mok_ingredient_2)

        # Удаляем первый ингредиент
        burger.remove_ingredient(0)

        assert burger.ingredients == [mok_ingredient_2]

    def test_move_ingredient(self, mok_ingredient, mok_ingredient_2):
        burger = Burger()

        # Добавляем два ингредиента
        burger.add_ingredient(mok_ingredient)
        burger.add_ingredient(mok_ingredient_2)

        # Перемещаем первый ингредиент на вторую позицию
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mok_ingredient_2, mok_ingredient]

    def test_get_price(self, mok_bun, mok_ingredient, mok_ingredient_2):
        burger = Burger()
        burger.set_buns(mok_bun)
        burger.add_ingredient(mok_ingredient)
        burger.add_ingredient(mok_ingredient_2)

        total_price = burger.get_price()

        assert total_price == MockBun.PRICE * 2 + MockIngredient.PRICE + MockIngredient2.PRICE

    def test_get_receipt(self, mok_bun, mok_ingredient, mok_ingredient_2):
        burger = Burger()
        burger.set_buns(mok_bun)
        burger.add_ingredient(mok_ingredient)
        burger.add_ingredient(mok_ingredient_2)
        receipt = ('(==== Крафтовая булка ====)\n'
                   '= начинка Говяжий метеорит =\n'
                   '= соус Говяжий  =\n'
                   '(==== Крафтовая булка ====)\n'
                   '\n'
                   'Price: 900')
        assert burger.get_receipt() == receipt
