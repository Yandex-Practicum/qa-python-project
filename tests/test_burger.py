import pytest
from unittest.mock import Mock

from data.burger_data import BurgerData
from data.burger_data import MockData


class TestBurger:
    # в классе TestBurger используются моки для того, чтобы сделать проверки класса Burger
    # независимыми от классов Bun и Ingredient

    @pytest.mark.parametrize(("bun_name", "bun_price"), [BurgerData.BUN_1, BurgerData.BUN_2, BurgerData.BUN_3])
    def test_set_buns(self, burger, bun_name, bun_price):
        bun = Mock()
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    @pytest.mark.parametrize(("i_type", "name", "price"),
                             [BurgerData.SAUCE_1, BurgerData.SAUCE_2, BurgerData.FILLING_1, BurgerData.FILLING_2])
    def test_add_ingredient_one_ingredient(self, burger, i_type, name, price):
        ingredient = Mock()
        ingredient.get_type.return_value = i_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_add_ingredient_several_ingredients(self, burger):
        burger.add_ingredient(MockData.mock_ingredient_1)
        burger.add_ingredient(MockData.mock_ingredient_2)
        assert burger.ingredients == [MockData.mock_ingredient_1, MockData.mock_ingredient_2]

    def test_remove_ingredient(self, burger):
        burger.add_ingredient(MockData.mock_ingredient_1)
        assert burger.ingredients == [MockData.mock_ingredient_1]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_ingredient_by_index_if_several_ingredients(self, burger_with_mock_ingredients):
        burger_with_mock_ingredients.remove_ingredient(1)
        assert burger_with_mock_ingredients.ingredients == [MockData.mock_ingredient_1, MockData.mock_ingredient_2]

    def test_move_ingredient(self, burger_with_mock_ingredients):
        burger_with_mock_ingredients.move_ingredient(2, 0)
        assert burger_with_mock_ingredients.ingredients == [MockData.mock_ingredient_2, MockData.mock_ingredient_1, MockData.mock_ingredient_1]

    def test_get_price(self, burger_with_mock_ingredients):
        ingredients_price = 0
        bun_price = burger_with_mock_ingredients.bun.get_price() * 2
        for item in burger_with_mock_ingredients.ingredients:
            ingredients_price += item.get_price()
        expected_price = bun_price + ingredients_price
        price = burger_with_mock_ingredients.get_price()
        assert price == expected_price

    @pytest.mark.parametrize("ingredient_count", [0, 1, 2, 3, 4])
    def test_get_price_depending_on_ing_count(self, burger, ingredient_count):
        burger.set_buns(MockData.mock_bun)
        for _ in range(ingredient_count):
            burger.add_ingredient(MockData.mock_ingredient_2)
        expected_price = MockData.mock_bun.get_price() * 2 + MockData.mock_ingredient_2.get_price() * ingredient_count
        price = burger.get_price()
        assert price == expected_price

    def test_get_receipt(self, burger_with_mock_ingredients):
        receipt = burger_with_mock_ingredients.get_receipt()
        assert receipt == MockData.MOCK_RECEIPT

