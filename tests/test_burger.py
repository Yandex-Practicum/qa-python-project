from ..burger import Burger
from ..tests.mocks import MockData
from ..database import Database


class TestBurger:

    def test_burger_set_buns(self):
        burger = Burger()
        mocked_bun = MockData.mock_bun()
        burger.set_buns(mocked_bun)
        assert burger.bun == mocked_bun

    def test_burger_add_ingredient(self):
        burger = Burger()
        mocked_ingredient = MockData.mock_ingredient()
        burger.add_ingredient(mocked_ingredient)
        assert mocked_ingredient in burger.ingredients

    def test_burger_remove_ingredient(self):
        burger = Burger()
        mocked_ingredient = MockData.mock_ingredient()
        burger.add_ingredient(mocked_ingredient)
        burger.remove_ingredient(0)
        assert mocked_ingredient not in burger.ingredients

    def test_burger_move_ingredient(self):
        burger = Burger()
        database = Database()
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.move_ingredient(0, 1)
        expected_name = database.available_ingredients()[0].name
        assert burger.ingredients[1].name == expected_name

    def test_burger_get_price(self):
        burger = Burger()
        mocked_bun = MockData.mock_bun()
        mocked_ingredient = MockData.mock_ingredient()
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        expected_price = (mocked_bun.get_price() * 2) + mocked_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self):
        burger = Burger()
        mocked_bun = MockData.mock_bun()
        mocked_ingredient = MockData.mock_ingredient()
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        result = burger.get_receipt()
        assert result == MockData.mocked_burger_receipt
