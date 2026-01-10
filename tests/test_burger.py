from conftest import create_ingredient
from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_bun_for_burger(self, create_bun):
        burger = Burger()
        burger.set_buns(create_bun)
        assert burger.bun.get_name() == 'Кунжутная'

    def test_add_ingredient_to_burger(self, create_ingredient):
        burger = Burger()
        burger.add_ingredient(create_ingredient)
        assert len(burger.ingredients) > 0

    def test_remove_ingredient_to_burger(self, create_ingredient):
        burger = Burger()
        burger.add_ingredient(create_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_in_burger(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_1.name = 'Барбекю'
        mock_ingredient_1.price = 20
        mock_ingredient_1.ingredient_type = 'SAUCE'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.name = 'Огурец'
        mock_ingredient_2.price = 12.2
        mock_ingredient_2.ingredient_type = 'FILLING'
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        assert burger.ingredients[0].name == 'Барбекю'
        assert burger.ingredients[1].name == 'Огурец'
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].name == 'Огурец'
        assert burger.ingredients[1].name == 'Барбекю'

    def test_get_price_for_burger(self, create_bun, create_ingredient):
        burger = Burger()
        burger.set_buns(create_bun)
        burger.add_ingredient(create_ingredient)
        assert burger.get_price() == 210.4 or 217.2

    def test_get_receipt_for_burger(self, create_bun, create_ingredient):
        burger = Burger()
        burger.set_buns(create_bun)
        burger.add_ingredient(create_ingredient)
        assert burger.bun.get_name() in burger.get_receipt()
