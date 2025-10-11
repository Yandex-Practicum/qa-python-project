import pytest
from unittest.mock import MagicMock


class TestBurger:
    def test_init_is_none(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns_success_assign(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun is not None
        assert burger.bun == bun_mock

    def test_add_ingredient_one_instance_success(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient_mock

    def test_remove_ingredient_success(self, burger, ingredient_mock):
        burger.ingredients.append(ingredient_mock)
        burger.remove_ingredient(index=0)
        assert burger.ingredients == []

    def test_move_ingredient_success(self, burger, ingredient_mock, another_ingredient_mock):
        burger.ingredients.append(ingredient_mock)
        burger.ingredients.append(another_ingredient_mock)
        assert burger.ingredients == [ingredient_mock, another_ingredient_mock]
        burger.move_ingredient(index=0, new_index=1)
        assert burger.ingredients == [another_ingredient_mock, ingredient_mock]

    @pytest.mark.parametrize('ingredient_prices', ([], [100.0], [10.0, 20.0], [5.0, 15.0, 25.0]))
    def test_get_price_success(self, burger, bun_mock, ingredient_prices):
        burger.set_buns(bun_mock)
        price_ingredients = 0
        for price in ingredient_prices:
            ingredient = MagicMock()
            ingredient.get_price.return_value = price
            burger.ingredients.append(ingredient)
            price_ingredients += price
        expected_price = burger.bun.get_price() * 2 + price_ingredients
        assert expected_price == burger.get_price()

    def test_get_receipt_success(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_receipt = f'(==== {bun_mock.get_name()} ====)\n' \
                           f'= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =\n' \
                           f'(==== {bun_mock.get_name()} ====)\n' \
                           '\n' \
                           f'Price: {burger.get_price()}'
        assert burger.get_receipt() == expected_receipt
