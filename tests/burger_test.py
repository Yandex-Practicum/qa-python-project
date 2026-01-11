from praktikum.bun import Bun
from praktikum.burger import Burger
from data import TestData
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
import pytest
import mock


class TestBurger:
    def test_set_bun_bun_is_set(self):
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, TestData.BUN_PRICE_VALID)
        burger = Burger()
        burger.set_buns(bun)
        assert TestData.BUN_NAME_VALID_WHITE in burger.get_receipt()

    def test_set_bun_change_bun_by_second_setting_bun_is_changed(self):
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, TestData.BUN_PRICE_VALID)
        bun1 = Bun(TestData.BUN_NAME_VALID_BLACK, TestData.BUN_PRICE_VALID)
        burger = Burger()
        burger.set_buns(bun)
        burger.set_buns(bun1)
        assert TestData.BUN_NAME_VALID_BLACK in burger.get_receipt()

    def test_set_bun_change_bun_by_second_setting_first_bun_is_replaced(self):
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, TestData.BUN_PRICE_VALID)
        bun1 = Bun(TestData.BUN_NAME_VALID_BLACK, TestData.BUN_PRICE_VALID)
        burger = Burger()
        burger.set_buns(bun)
        burger.set_buns(bun1)
        assert TestData.BUN_NAME_VALID_WHITE not in burger.get_receipt()

    @pytest.mark.parametrize('sauce_name',
                             [TestData.SAUCE_NAME_CHILI, TestData.SAUCE_NAME_HOT, TestData.SAUCE_NAME_SOUR])
    def test_add_ingredient_sauce_ingredient_is_added(self, sauce_name):
        burger = Burger()
        bun = mock.BurgerMock.mock_bun()
        burger.set_buns(bun)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, sauce_name,
                                TestData.INGREDIENT_PRICE_VALID)
        burger.add_ingredient(ingredient)
        expected_result = str(ingredient.get_type()).lower() +' '+ ingredient.get_name()
        assert expected_result in burger.get_receipt()

    @pytest.mark.parametrize('filling_name',
                             [TestData.FILLING_NAME_CUTLET, TestData.FILLING_NAME_SAUSAGE,
                              TestData.FILLING_NAME_DINOSAUR])
    def test_add_ingredient_filling_ingredient_is_added(self, filling_name):
        burger = Burger()
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, TestData.BUN_PRICE_VALID)
        burger.set_buns(bun)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, filling_name,
                                TestData.INGREDIENT_PRICE_VALID)
        burger.add_ingredient(ingredient)
        expected_result = str(ingredient.get_type()).lower() + ' ' + ingredient.get_name()
        assert expected_result in burger.get_receipt()

    @pytest.mark.parametrize('number_of_ingredient, ingredient_name_to_delete', [[0, TestData.SAUCE_NAME_HOT],
                             [1, TestData.FILLING_NAME_CUTLET]])
    def test_remove_ingredient_ingredient_is_removed(self, number_of_ingredient, ingredient_name_to_delete):
        burger = Burger()
        bun = mock.BurgerMock.mock_bun()
        burger.set_buns(bun)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_HOT, TestData.INGREDIENT_PRICE_VALID)
        burger.add_ingredient(ingredient)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME_CUTLET, TestData.INGREDIENT_PRICE_VALID)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(number_of_ingredient)
        assert ingredient_name_to_delete not in burger.get_receipt()

    def test_move_ingredient(self):
        burger = Burger()
        bun = mock.BurgerMock.mock_bun()
        ingredient_one = mock.BurgerMock.mock_ingredient_with_parameters(ingredient_types.INGREDIENT_TYPE_SAUCE,TestData.SAUCE_NAME_CHILI, 5)
        ingredient_two = mock.BurgerMock.mock_ingredient_with_parameters(ingredient_types.INGREDIENT_TYPE_FILLING,
                                                                         TestData.FILLING_NAME_CUTLET, 10)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)
        expected = '(==== black bun ====)\n= filling cutlet =\n= sauce chili sauce =\n(==== black bun ====)'
        assert expected in burger.get_receipt()

    def test_get_price(self):
        burger = Burger()
        bun = mock.BurgerMock.mock_bun_with_price(10)
        ingredient = mock.BurgerMock.mock_ingredient_with_price(5)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        ingredient = mock.BurgerMock.mock_ingredient_with_price(6)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 31

    def test_get_receipt(self):
        burger = Burger()
        bun = mock.BurgerMock.mock_bun()
        ingredient = mock.BurgerMock.mock_ingredient()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected = '(==== black bun ====)\n= sauce sour cream =\n(==== black bun ====)'
        assert expected in burger.get_receipt()






