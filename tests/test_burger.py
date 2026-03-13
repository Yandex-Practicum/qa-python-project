import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock(spec=Bun)

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_removes_from_list(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_position(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price_returns_sum_of_bun_and_ingredients(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 50
        burger.set_buns(bun)

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 30
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 20
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        price = burger.get_price()

        assert price == 50 * 2 + 30 + 20

    def test_get_receipt_returns_formatted_string(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = 'black bun'
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = 'hot sauce'
        ingredient.get_price.return_value = 100
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        expected = '(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300'

        assert receipt == expected

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200),
    ])
    def test_get_price_with_different_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)

        result = burger.get_price()

        assert result == price * 2

    def test_get_price_without_bun_raises_error(self):
        burger = Burger()

        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_without_bun_raises_error(self):
        burger = Burger()

        with pytest.raises(AttributeError):
            burger.get_receipt()