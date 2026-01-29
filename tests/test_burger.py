import pytest

class TestBurger:

    def test_set_buns(self, burger):
        burger.set_buns('MindalBan')
        assert burger.bun == 'MindalBan'

    def test_add_ingredient(self, burger):
        burger.add_ingredient('Souce')
        assert 'Souce' in burger.ingredients

    def test_remove_ingredient(self, burger):
        burger.add_ingredient('Onion')
        burger.remove_ingredient(0)
        assert 'Onion' not in burger.ingredients


    def test_move_ingredient(self, burger):
        burger.add_ingredient('Onion')
        burger.add_ingredient('Creame')
        burger.add_ingredient('Pepper')
        burger.move_ingredient(0, 2)
        assert 'Onion' == burger.ingredients[2]


    def test_get_price_one_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        price = burger.get_price()
        assert price == 246

    def test_get_price_one_bun_and_one_ingridient(self, burger, mock_bun, mock_ingridient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingridient)
        price = burger.get_price()
        assert price == 334


    def test_get_receipt_for_bun_with_price(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        lst = burger.get_receipt()
        assert lst == '(==== CherryBun ====)\n(==== CherryBun ====)\n\nPrice: 246'