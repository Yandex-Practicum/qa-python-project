from praktikum.burger import Burger
from unittest.mock import Mock
from unittest.mock import patch
from data import DataTestBurger


class TestBurger:
    def test_set_buns_check_bun_name(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = DataTestBurger.bun_name
        burger.set_buns(mock_bun)
        assert burger.bun.name == DataTestBurger.bun_name

    def test_set_buns_check_bun_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.price = DataTestBurger.bun_price
        burger.set_buns(mock_bun)
        assert burger.bun.price == DataTestBurger.bun_price

    def test_add_ingredient_check_ingredient_name(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.name = DataTestBurger.ingredient_name_1
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == DataTestBurger.ingredient_name_1

    def test_add_ingredient_check_ingredient_type(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.type = DataTestBurger.ingredient_type
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].type == DataTestBurger.ingredient_type

    def test_add_ingredient_check_ingredient_price(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.price = DataTestBurger.ingredient_price
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].price == DataTestBurger.ingredient_price

    def test_remove_ingredient_add_2_delete_1(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_1.name = DataTestBurger.ingredient_name_1
        mock_ingredient_2 = Mock()
        mock_ingredient_2.name = DataTestBurger.ingredient_name_2
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredients_add_2_change_index(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_1.name = DataTestBurger.ingredient_name_1
        mock_ingredient_2 = Mock()
        mock_ingredient_2.name = DataTestBurger.ingredient_name_2
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == DataTestBurger.ingredient_name_2

    def test_get_price_check_sum_bun_and_2_ingredients(self, create_mock_burger_prices):
        mock_bun, mock_ingredient_1, mock_ingredient_2 = create_mock_burger_prices
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == 700

    @patch('praktikum.burger.Burger.get_price', return_value=1000)
    def test_get_receipt_mock_bun_and_2_ingredients(self, mock_get_price, create_mock_burger_names):
        mock_bun, mock_ingredient_1, mock_ingredient_2 = create_mock_burger_names
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        print(burger.get_receipt())
        assert burger.get_receipt() == ("(==== Булочка с маком ====)\n"
                                        "= соус Ранч =\n"
                                        "= начинка Котлета =\n"
                                        "(==== Булочка с маком ====)\n"
                                        "\n"
                                        "Price: 1000")
