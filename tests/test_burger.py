import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from conftest import mock_bun
from conftest import mock_ingredients


class TestBurger:
    @pytest.mark.parametrize('name,price', [['Флюоресцентная булка R2-D3', 988], ['Краторная булка N-200i', 1255]])
    def test_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == name

    def test_add_ingredients(self):
        burger = Burger()
        ingredients = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        burger.add_ingredient(ingredients)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ingredients = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredients1 = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        ingredients2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)
        burger.add_ingredient(ingredients1)
        burger.add_ingredient(ingredients2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredients1

    def test_get_price(self):
        burger = Burger()
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger.set_buns(bun)
        ingredients1 = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        ingredients2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)
        burger.add_ingredient(ingredients1)
        burger.add_ingredient(ingredients2)
        assert burger.get_price() == 4991

    def test_get_receipt(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)
        receipt = burger.get_receipt()
        assert receipt == ("(==== Краторная булка N-200i ====)\n= filling Говяжий метеорит (отбивная) =\n(==== "
                           "Краторная булка N-200i ====)\n\n"f'Price: {burger.get_price()}')