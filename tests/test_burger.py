from unittest.mock import Mock
import pytest
from praktikum.burger import Burger


class TestBurger:

    def setup_method(self):
        self.burger = Burger()

    def test_burger_creation(self):
        assert self.burger.bun is None
        assert len(self.burger.ingredients) == 0

    def test_set_bun(self, mock_bun):
        self.burger.set_buns(mock_bun)

        assert self.burger.bun is not None
        assert self.burger.bun.get_name() == mock_bun.get_name()
        assert self.burger.bun.get_price() == mock_bun.get_price()

    def test_add_ingredient(self, mock_ingredient1, mock_ingredient2):
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0].get_type() == mock_ingredient1.get_type()
        assert self.burger.ingredients[0].get_name() == mock_ingredient1.get_name()
        assert self.burger.ingredients[0].get_price() == mock_ingredient1.get_price()

        assert self.burger.ingredients[1].get_type() == mock_ingredient2.get_type()
        assert self.burger.ingredients[1].get_name() == mock_ingredient2.get_name()
        assert self.burger.ingredients[1].get_price() == mock_ingredient2.get_price()

    def test_remove_ingredient(self, mock_ingredient1, mock_ingredient2):
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        self.burger.remove_ingredient(1)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0].get_name() == mock_ingredient1.get_name()

        self.burger.remove_ingredient(0)

        assert len(self.burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        self.burger.move_ingredient(0, 1)

        assert self.burger.ingredients[0].get_name() == mock_ingredient2.get_name()
        assert self.burger.ingredients[1].get_name() == mock_ingredient1.get_name()

    @pytest.mark.parametrize(
        'bun_price,ingredient1_price,ingredient2_price,total_price',
        [
            (100, 30, 20, 250),
            (0, 30, 10, 40),
            (50, 0, 30, 130),
            (0, 0, 0, 0)
        ]
    )
    def test_get_price(self, bun_price, ingredient1_price, ingredient2_price, total_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = ingredient1_price
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = ingredient2_price

        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        assert self.burger.get_price() == total_price

    def test_get_receipt(self, mock_bun, mock_ingredient1, mock_ingredient2):
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)

        receipt = '''(==== Краторная булка N-200i ====)
= filling Говяжий метеорит (отбивная) =
= sauce Соус Spicy-X =
(==== Краторная булка N-200i ====)

Price: 5600'''

        assert self.burger.get_receipt() == receipt
