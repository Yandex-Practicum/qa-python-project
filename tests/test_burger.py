from praktikum.burger import Burger
from generators_data import generate_random_bun_name, generate_random_bun_price, generate_random_ingredient_name, generate_random_ingredient_price
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock

class TestBurger:
    def test_set_buns_correctly(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_correctly(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_correctly(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index)

        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_to_new_index(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient2 and burger.ingredients[1] == mock_ingredient1

    def test_calculate_price_correctly(self):
        bun_price = generate_random_bun_price()
        ingredient_price = generate_random_ingredient_price()
        mock_ingredient = Mock()
        mock_bun = Mock()
        burger = Burger()

        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)

        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price

        assert burger.get_price() == bun_price * 2 + ingredient_price

    def test_get_receipt_with_bun_name(self):
        bun_name = generate_random_bun_name()
        bun_price = generate_random_bun_price()
        
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        assert bun_name in burger.get_receipt()

    def test_get_receipt_with_ingredient_name(self):
        bun_name = generate_random_bun_name()
        bun_price = generate_random_bun_price()
        ingredient_name = generate_random_ingredient_name()
        ingredient_price = generate_random_ingredient_price()
        
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
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

        assert burger.get_receipt() == receipt