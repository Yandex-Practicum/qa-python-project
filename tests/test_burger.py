from mock import Mock
import random
from praktikum.burger import Burger
from data import TestData

class TestBurger:

    def test_set_buns(self):

        mock_bun = Mock()
        mock_bun.name = random.choice(TestData.bun_names)
        mock_bun.price = random.choice(TestData.prices)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):

        mock_ingredient = Mock()
        mock_ingredient.type = random.choice(TestData.ingredient_types)
        mock_ingredient.name = random.choice(TestData.ingredient_names)
        mock_ingredient.price = random.choice(TestData.prices)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):

        mock_ingredient = Mock()
        mock_ingredient.type = random.choice(TestData.ingredient_types)
        mock_ingredient.name = random.choice(TestData.ingredient_names)
        mock_ingredient.price = random.choice(TestData.prices)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self):

        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = random.choice(TestData.ingredient_types)
        mock_ingredient_1.name = random.choice(TestData.ingredient_names)
        mock_ingredient_1.price = random.choice(TestData.prices)
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = random.choice(TestData.ingredient_types)
        mock_ingredient_2.name = random.choice(TestData.ingredient_names)
        mock_ingredient_2.price = random.choice(TestData.prices)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_burger_price(self):

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        burger = Burger()
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200

        burger.add_ingredient(mock_ingredient)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()

        assert burger.get_price() == expected_price

    def test_get_receipt(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        burger = Burger()
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "sausage"
        mock_ingredient.get_type.return_value = "filling"
        mock_ingredient.get_price.return_value = 300

        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling sausage =\n"
            "(==== black bun ====)\n"
            "\nPrice: 500"
        )
        assert burger.get_receipt() == expected_receipt