from praktikum.burger import Burger
from praktikum.helper import DatabaseMock


class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        mock_database = DatabaseMock()
        mock_database.available_buns()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock_database = DatabaseMock()
        ingredients = mock_database.available_ingredients()
        burger.add_ingredient(ingredients[0])
        assert ingredients[0] in burger.ingredients

    def test_remove_ingredient(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock_database = DatabaseMock()
        ingredients = mock_database.available_ingredients()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)
        assert ingredients[0] not in burger.ingredients

    def test_move_ingredient(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock_database = DatabaseMock()
        ingredients = mock_database.available_ingredients()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        initial_ingredients = burger.ingredients.copy()
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [initial_ingredients[1], initial_ingredients[0]]

    def test_get_price(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock_database = DatabaseMock()
        mock_ingredient = mock_database.available_ingredients()[0]
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        expected_price = bun.get_price.return_value * 2 + mock_ingredient.get_price() * 2
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock_database = DatabaseMock()
        mock_ingredient1 = mock_database.available_ingredients()[0]
        mock_ingredient2 = mock_database.available_ingredients()[1]
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        expected_receipt = [
            f'(==== {bun.get_name.return_value} ====)',
            f'= {str(mock_ingredient1.get_type()).lower()} {mock_ingredient1.get_name()} =',
            f'= {str(mock_ingredient2.get_type()).lower()} {mock_ingredient2.get_name()} =',
            f'(==== {bun.get_name.return_value} ====)\n',
            f'Price: {burger.get_price()}'
        ]
        assert burger.get_receipt() == '\n'.join(expected_receipt)
