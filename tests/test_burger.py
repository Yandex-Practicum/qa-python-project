from praktikum.burger import Burger
from unittest.mock import Mock
from data import Data

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = Data.bun_name
        burger.set_buns(mock_bun)

        assert mock_bun.get_name() == burger.bun.get_name()

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = Data.ingredient_type
        mock_ingredient.get_name.return_value = Data.ingredient_name
        mock_ingredient.get_price.return_value = Data.ingredient_price
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = Data.ingredient_type
        mock_ingredient.get_name.return_value = Data.ingredient_name
        mock_ingredient.get_price.return_value = Data.ingredient_price
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient.get_type.return_value = Data.ingredient_type
        mock_ingredient.get_name.return_value = Data.ingredient_name
        mock_ingredient.get_price.return_value = Data.ingredient_price
        mock_ingredient_2.get_type.return_value = Data.ingredient_type_2
        mock_ingredient_2.get_name.return_value = Data.ingredient_name_2
        mock_ingredient_2.get_price.return_value = Data.ingredient_price_2
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients.index(mock_ingredient) == 1


    def test_get_price(self):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = Data.ingredient_type
        mock_ingredient.get_name.return_value = Data.ingredient_name
        mock_ingredient.get_price.return_value = Data.ingredient_price
        mock_bun = Mock()
        mock_bun.get_name.return_value = Data.bun_name
        mock_bun.get_price.return_value = Data.ingredient_price_2
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()

        assert price == 40

    def test_get_recept(self):
        mock_ingredient = Mock()
        type_ingredient = mock_ingredient.get_type.return_value = Data.ingredient_type
        type_ingredient_name = mock_ingredient.get_name.return_value = Data.ingredient_name
        mock_ingredient.get_price.return_value = Data.ingredient_price
        mock_bun = Mock()
        bun_name = mock_bun.get_name.return_value = Data.bun_name
        mock_bun.get_price.return_value = Data.bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()
        recept = burger.get_receipt()

        assert (f'(==== {bun_name} ====)'+'\n'+f'= {type_ingredient.lower()} {type_ingredient_name} ='+'\n'+f'(==== {bun_name} ====)'+'\n'+'\n'+f'Price: {price}') == recept
