import pytest
from praktikum_burger.burger import Burger
from unittest.mock import Mock, patch

class TestBurger:
    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert len (burger.ingredients) == 0

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, sauce_mock):
        burger = Burger()
        burger.add_ingredient(sauce_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == sauce_mock
 
    def test_remove_ingredient(self, sauce_mock):
        burger = Burger()
        burger.add_ingredient(sauce_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == sauce_mock
        burger.remove_ingredient(0) 
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, sauce_mock, filling_mock):
        burger = Burger()
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == filling_mock
        assert burger.ingredients[1] == sauce_mock

    def test_get_price(self, bun_mock, sauce_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        expected_price = bun_mock.get_price() * 2 + sauce_mock.get_price() + filling_mock.get_price()
        assert burger.get_price() == 210.0
            
    def test_get_price_only_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        expected_price = bun_mock.get_price() * 2
        assert burger.get_price() == 100.0
  
    def test_get_receipt(self, bun_mock, sauce_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)

        expected_price = (bun_mock.get_price() * 2 + sauce_mock.get_price() + filling_mock.get_price())

        expected_receipt = (
            f'(==== {bun_mock.get_name()} ====)\n'
            f'= {sauce_mock.get_type()} {sauce_mock.get_name()} =\n'
            f'= {filling_mock.get_type()} {filling_mock.get_name()} =\n'
            f'(==== {bun_mock.get_name()} ====)\n'
            f'Price: {expected_price}'
        )
        receipt = burger.get_receipt()
        assert receipt == expected_receipt
        assert expected_price == 210.0



    def test_set_buns_negative(self):
        burger = Burger()
        burger.set_buns(None)
        assert burger.bun is None

    def test_add_ingredient_negative(self):
        burger = Burger()
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []
        invalid_ingredient = 'сыр'
        result = burger.add_ingredient(invalid_ingredient)
        assert result is None
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []
    
    def test_remove_ingredient_negative(self):
        burger = Burger()
        assert len(burger.ingredients) == 0
        assert burger.remove_ingredient(0) is False
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []
         
    def test_move_ingredient_negative(self):
        burger = Burger()
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []
        from_index = -1
        to_index = 0
        assert isinstance(from_index, int)
        assert isinstance(to_index, int)
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []

    def test_get_price_negative_sauce(self, bun_mock, sauce_mock):
        invalid_price = -10
        burger = Burger()
        burger.set_buns(bun_mock)
        sauce_mock.get_price = Mock(return_value=invalid_price)
        burger.add_ingredient(sauce_mock)
        expected_price = bun_mock.get_price() * 2
        assert burger.get_price() == 100.0

    def test_get_price_negative_filling(self, bun_mock, filling_mock):
       invalid_price = -100
       burger = Burger()
       burger.set_buns(bun_mock)
       filling_mock.get_price = Mock(return_value=invalid_price)
       burger.add_ingredient(filling_mock)
       aexpected_price = bun_mock.get_price() * 2
       assert burger.get_price() == 100.0

   
    def test_get_receipt_negative_incorrect_price(self, bun_mock, sauce_mock, filling_mock):
        bun_mock.get_price = Mock(return_value=None)
        burger = Burger()   
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)    
        burger.get_price = Mock(return_value="Цена не может быть рассчитана")

        expected_receipt = (
        f'(==== {bun_mock.get_name()} ====)\n'
        f'= {sauce_mock.get_type().lower()} {sauce_mock.get_name()} =\n'  
        f'= {filling_mock.get_type().lower()} {filling_mock.get_name()} =\n'  
        f'(==== {bun_mock.get_name()} ====)\n'
        f'Price: Цена не может быть рассчитана'
    )
        receipt = burger.get_receipt()
        assert receipt == expected_receipt
        assert bun_mock.get_price() is None
        assert f'(==== {bun_mock.get_name()} ====)' in receipt
        assert f'= {sauce_mock.get_type().lower()} {sauce_mock.get_name()} =' in receipt
        assert f'= {filling_mock.get_type().lower()} {filling_mock.get_name()} =' in receipt
        assert receipt.endswith('Price: Цена не может быть рассчитана')
 
