from praktikum.burger import Burger
from generators import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_success_new_index_in_ingredient(self, mock_add_ingredients):
        ingredient = mock_add_ingredients.ingredients[0]
        mock_add_ingredients.move_ingredient(1, 0)
        assert mock_add_ingredients.ingredients[1] == ingredient

    def test_get_price_return_correct_calculated_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        assert burger.get_price() == bun_price * 2 + ingredient_price

    def test_get_receipt_return_correct(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price
        receipt = f'(==== {bun_name} ====)\n' \
                  f'= sauce {ingredient_name} =\n' \
                  f'(==== {bun_name} ====)\n' \
                  f'\nPrice: {bun_price * 2 + ingredient_price}'
        print(receipt)
        assert burger.get_receipt() == receipt
