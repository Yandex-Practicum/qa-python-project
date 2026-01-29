from data import expected
from practicum_burgers.burger import Burger
from tests.conftest import *



class TestBurger:

    def test_init_burger_bun_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_init_burger_ingredients_list(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_bun(self, bun_mock):
        burger = Burger()
        bun = bun_mock(burger, price=60, name="Вкусная булочка")
        assert burger.bun is bun

    def test_add_ingredient_successful_addition(self, ingredient_mock):
        burger = Burger()
        ing = ingredient_mock(burger, ingredient_type="SAUCE", price=20, name="Чесночный")
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing

    def test_add_ingredients_multiple_successful_addition(self, ingredient_mock):
        burger = Burger()
        ing1 = ingredient_mock(burger)
        ing2 = ingredient_mock(burger, name="Сыр", ingredient_type="FILLING")
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ing1, ing2]

    def test_remove_ingredient_successful_remove(self, ingredient_mock):
        burger = Burger()
        ing1 = ingredient_mock(burger)
        ing2 = ingredient_mock(burger)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing2
        assert ing1 is not burger.ingredients[0]

    def test_remove_ingredient_invalid_index(self, ingredient_mock):
        burger = Burger()
        ingredient_mock(burger)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_move_ingredient_successful_move(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun_mock(burger)
        ing1 = ingredient_mock(burger)
        ing2 = ingredient_mock(burger)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] is ing2
        assert burger.ingredients[1] is ing1

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (0, [20, 30], 50),
            (50, [10], 110),
            (100, [], 200),
        ]
    )
    def test_get_price_param(self, bun_price, ingredient_prices, expected_total, bun_mock, ingredient_mock):
        burger = Burger()
        bun_mock(burger, price=bun_price)
        for price in ingredient_prices:
            ingredient_mock(burger, price=price)
        result = burger.get_price()
        assert result == expected_total

    def test_get_price_without_bun_raises_attributeerror(self, ingredient_mock):
        burger = Burger()
        ingredient_mock(burger, price=20)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        bun_mock(burger, name='Вкусная булочка')
        ingredient_mock(burger, ingredient_type='SAUCE', name='Чесночный')
        ingredient_mock(burger, ingredient_type='FILLING', name='Сыр')

        burger.get_price = Mock(return_value=100.0)
        receipt = burger.get_receipt()

        assert receipt == expected
