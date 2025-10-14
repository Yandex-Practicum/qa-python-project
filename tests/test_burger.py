import pytest


class TestBurger:
    
    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger, ingredient_mock):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == initial_count + 1
        assert burger.ingredients[-1] == ingredient_mock

    def test_remove_ingredient(self, burger, ingredient_mock, cutlet_ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == cutlet_ingredient_mock

    def test_move_ingredient(self, burger, ingredient_mock, cutlet_ingredient_mock, cheese_ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        burger.add_ingredient(cheese_ingredient_mock)
        
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[2] == ingredient_mock
        assert burger.ingredients[0] == cutlet_ingredient_mock

    def test_get_price(self, basic_burger_setup, bun_mock, ingredient_mock, cutlet_ingredient_mock):
        burger = basic_burger_setup
        
        expected_price = (
            bun_mock.get_price() * 2 +  
            ingredient_mock.get_price() +
            cutlet_ingredient_mock.get_price()
        )
        
        assert burger.get_price() == expected_price

    def test_get_receipt_format(self, basic_burger_setup, bun_mock, ingredient_mock, cutlet_ingredient_mock):
        burger = basic_burger_setup
        
        receipt = burger.get_receipt()
        
        receipt_lines = receipt.strip().split('\n')
        
        assert receipt_lines[0] == f"(==== {bun_mock.get_name()} ====)"
        assert receipt_lines[1] == f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} ="
        assert receipt_lines[2] == f"= {cutlet_ingredient_mock.get_type().lower()} {cutlet_ingredient_mock.get_name()} ="
        assert receipt_lines[3] == f"(==== {bun_mock.get_name()} ====)"
        assert receipt_lines[4] == ""
        assert receipt_lines[5] == f"Price: {burger.get_price()}"

    def test_get_receipt_only_buns(self, burger, white_bun_mock):
        burger.set_buns(white_bun_mock)
        
        receipt = burger.get_receipt()
        receipt_lines = receipt.strip().split('\n')
        
        assert receipt_lines[0] == f"(==== {white_bun_mock.get_name()} ====)"
        assert receipt_lines[1] == f"(==== {white_bun_mock.get_name()} ====)"
        assert receipt_lines[2] == ""
        assert receipt_lines[3] == f"Price: {burger.get_price()}"
        assert burger.get_price() == white_bun_mock.get_price() * 2

    def test_get_receipt_no_bun_raises_exception(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_ingredient_order_preserved(self, burger, red_bun_mock, ingredient_mock, cutlet_ingredient_mock, cheese_ingredient_mock):
        burger.set_buns(red_bun_mock)
        
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        burger.add_ingredient(cheese_ingredient_mock)
        
        receipt = burger.get_receipt()
        receipt_lines = receipt.strip().split('\n')
        
        assert receipt_lines[1] == f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} ="
        assert receipt_lines[2] == f"= {cutlet_ingredient_mock.get_type().lower()} {cutlet_ingredient_mock.get_name()} ="
        assert receipt_lines[3] == f"= {cheese_ingredient_mock.get_type().lower()} {cheese_ingredient_mock.get_name()} ="

    def test_get_price_empty_burger(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        
        expected_price = bun_mock.get_price() * 2
        assert burger.get_price() == expected_price

    def test_get_price_no_buns_raises_exception(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        
        with pytest.raises(AttributeError):
            burger.get_price()