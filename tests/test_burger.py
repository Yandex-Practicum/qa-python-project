from data import *
from conftest import cosmo_burger, bun_mock, ingredient_mock, ingredient_mock_remove

class TestBurger:

    def test_set_buns(self, cosmo_burger, bun_mock):
        cosmo_burger.set_buns(bun_mock)
        assert cosmo_burger.bun == bun_mock

    def test_add_ingredient(self, cosmo_burger, ingredient_mock):
        cosmo_burger.add_ingredient(ingredient_mock)
        assert cosmo_burger.ingredients == [ingredient_mock]

    def test_remove_ingredient(self, cosmo_burger, ingredient_mock, ingredient_mock_remove):
        cosmo_burger.add_ingredient(ingredient_mock)
        cosmo_burger.add_ingredient(ingredient_mock_remove)

        cosmo_burger.remove_ingredient(0)
        assert cosmo_burger.ingredients == [ingredient_mock_remove]

    def test_move_ingredient(self, cosmo_burger, ingredient_mock, ingredient_mock_remove):
        cosmo_burger.add_ingredient(ingredient_mock)
        cosmo_burger.add_ingredient(ingredient_mock_remove)

        cosmo_burger.move_ingredient(0, 1)
        assert cosmo_burger.ingredients == [ingredient_mock_remove, ingredient_mock]

        cosmo_burger.move_ingredient(1, 0)
        assert cosmo_burger.ingredients == [ingredient_mock, ingredient_mock_remove]

    def test_get_price(self,cosmo_burger, bun_mock, ingredient_mock, ingredient_mock_remove):
        cosmo_burger.set_buns(bun_mock)
        cosmo_burger.add_ingredient(ingredient_mock)
        cosmo_burger.add_ingredient(ingredient_mock_remove)

        total_price = (BunData.price * 2) + IngredientData.price + RemoveIngredientData.price
        assert cosmo_burger.get_price() == total_price

    def test_get_receipt(self, cosmo_burger, bun_mock, ingredient_mock, ingredient_mock_remove):
        cosmo_burger.set_buns(bun_mock)
        cosmo_burger.add_ingredient(ingredient_mock)
        cosmo_burger.add_ingredient(ingredient_mock_remove)

        expected_receipt = (
            f'(==== {BunData.name} ====)\n'
            f'= {IngredientData.type} {IngredientData.name} =\n'
            f'= {RemoveIngredientData.type} {RemoveIngredientData.name} =\n'
            f'(==== {BunData.name} ====)\n''\n'
            f'Price: {(BunData.price * 2) + IngredientData.price + RemoveIngredientData.price}'
        )

        assert cosmo_burger.get_receipt() == expected_receipt