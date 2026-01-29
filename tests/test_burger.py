import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        bun = Mock()
        bun.name = 'белая булочка'
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == 'белая булочка'

    def test_add_ingredient(self):
        ingredient = Mock()
        ingredient.type = 'соус'
        ingredient.name = 'карри'
        ingredient.price = 2.00
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        ingredient = Mock()
        ingredient.type = 'соус'
        ingredient.name = 'карри'
        ingredient.price = 2.00
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        ingredient_one = Mock()
        ingredient_one.name = 'карри'
        ingredient_two = Mock()
        ingredient_two.name = 'индейка'
        ingredient_three = Mock()
        ingredient_three.name = 'зелень'
        burger = Burger()
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.add_ingredient(ingredient_three)
        assert len(burger.ingredients) == 3
        assert burger.ingredients[2].name == 'зелень'
        burger.move_ingredient(2, 0)
        assert burger.ingredients[2].name == 'индейка'
        assert burger.ingredients[0].name == 'зелень'

    def test_get_price(self):
        bun = Mock()
        bun.get_price.return_value = 4.00
        burger = Burger()
        burger.set_buns(bun)
        ingredient_one = Mock()
        ingredient_one.get_price.return_value = 2.00
        ingredient_two = Mock()
        ingredient_two.get_price.return_value = 8.00
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)

        assert burger.get_price() == 18.00

    def test_get_receipt(self):
        bun = Mock()
        bun.get_name.return_value = 'белая булочка'
        bun.get_price.return_value = 3.00
        burger = Burger()
        burger.set_buns(bun)
        ingredient_one = Mock()
        ingredient_one.get_name.return_value = 'зелень'
        ingredient_one.get_type.return_value = 'начинка'
        ingredient_one.get_price.return_value = 1.00
        burger.add_ingredient(ingredient_one)
        ingredient_two = Mock()
        ingredient_two.get_name.return_value = 'индейка'
        ingredient_two.get_type.return_value = 'начинка'
        ingredient_two.get_price.return_value = 8.00
        burger.add_ingredient(ingredient_two)
        ingredient_three = Mock()
        ingredient_three.get_name.return_value = 'карри'
        ingredient_three.get_type.return_value = 'соус'
        ingredient_three.get_price.return_value = 2.00
        burger.add_ingredient(ingredient_three)
        receipt = burger.get_receipt()
        words_receipt = receipt.split(' ')
        assert 'зелень' in words_receipt
        assert 'индейка' in words_receipt
        assert 'карри' in words_receipt
        assert 'булочка' in words_receipt
        assert '17.0' in words_receipt


