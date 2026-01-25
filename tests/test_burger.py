import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database

database = Database()

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.configure_mock(name='Hleb', price=2)
        burger.set_buns(bun=mock_bun)
        self.bun = mock_bun
        assert self.bun == mock_bun

    @pytest.mark.parametrize('ingredient', database.available_ingredients())
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(database.available_ingredients()[0])
        burger.remove_ingredient(0)
        assert not burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        [burger.add_ingredient(i) for i in database.available_ingredients()[0:3]]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == database.available_ingredients()[1]

    def test_get_price(self):
        burger = Burger()
        burger.add_ingredient(database.available_ingredients()[0])
        burger.set_buns(database.available_buns()[0])
        assert burger.get_price() == 300

    def test_get_receipt(self):
        burger = Burger()
        [burger.add_ingredient(i) for i in database.available_ingredients()]
        burger.set_buns(database.available_buns()[0])

        assert burger.get_receipt() == (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= sauce sour cream =\n'
            '= sauce chili sauce =\n'
            '= filling cutlet =\n'
            '= filling dinosaur =\n'
            '= filling sausage =\n'
            '(==== black bun ====)\n\n'
            'Price: 1400'
        )
