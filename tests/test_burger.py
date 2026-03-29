import pytest
from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING


class TestBurgerInit:
    def test_burger_init(self, empty_burger):
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_burger_init_with_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []


class TestBurgerBuns:

    def test_set_buns(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)
        assert empty_burger.bun == test_bun

    def test_set_buns_multiple_times(self, empty_burger):
        bun1 = Bun("first bun", 100)
        bun2 = Bun("second bun", 200)

        empty_burger.set_buns(bun1)
        assert empty_burger.bun == bun1

        empty_burger.set_buns(bun2)
        assert empty_burger.bun == bun2


class TestBurgerIngredients:

    def test_add_ingredient(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == test_sauce_ingredient

    def test_add_multiple_ingredients(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)

        assert len(empty_burger.ingredients) == 2
        assert empty_burger.ingredients[0] == test_sauce_ingredient
        assert empty_burger.ingredients[1] == test_filling

    def test_remove_ingredient(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        empty_burger.remove_ingredient(0)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == test_filling

    def test_remove_ingredient_last(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        empty_burger.remove_ingredient(1)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == test_sauce_ingredient

    def test_move_ingredient_forward(self, empty_burger):
        ingredient1 = Ingredient(IngredientTypes.SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(IngredientTypes.FILLING, "cutlet", 200)
        ingredient3 = Ingredient(IngredientTypes.SAUCE, "sour cream", 150)

        empty_burger.add_ingredient(ingredient1)
        empty_burger.add_ingredient(ingredient2)
        empty_burger.add_ingredient(ingredient3)
        empty_burger.move_ingredient(0, 2)
        assert empty_burger.ingredients[0] == ingredient2
        assert empty_burger.ingredients[1] == ingredient3
        assert empty_burger.ingredients[2] == ingredient1

    def test_move_ingredient_back(self, empty_burger):
        ingredient1 = Ingredient(IngredientTypes.SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(IngredientTypes.FILLING, "cutlet", 200)

        empty_burger.add_ingredient(ingredient1)
        empty_burger.add_ingredient(ingredient2)
        empty_burger.move_ingredient(1, 0)
        assert empty_burger.ingredients[0] == ingredient2
        assert empty_burger.ingredients[1] == ingredient1

    def test_move_ingredient_to_end(self, empty_burger):
        ingredient1 = Ingredient(IngredientTypes.SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(IngredientTypes.FILLING, "cutlet", 200)

        empty_burger.add_ingredient(ingredient1)
        empty_burger.add_ingredient(ingredient2)
        empty_burger.move_ingredient(0, 1)
        assert empty_burger.ingredients[0] == ingredient2
        assert empty_burger.ingredients[1] == ingredient1

class TestBurgerPrice:

    def test_get_price_with_bun_and_ingredients(self, test_burger):
        assert test_burger.get_price() == 400

    def test_get_price_without_bun(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)
        with pytest.raises(AttributeError):
            empty_burger.get_price()

    def test_get_price_without_ingredients(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)
        assert empty_burger.get_price() == 200

    def test_get_price_with_different_bun_prices(self, empty_burger):
        bun1 = Bun("cheap bun", 50)
        bun2 = Bun("rich bun", 300)

        empty_burger.set_buns(bun1)
        assert empty_burger.get_price() == 100

        empty_burger.set_buns(bun2)
        assert empty_burger.get_price() == 600

    def test_get_price_with_multiple_same_ingredients(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)
        ingredient = Ingredient(IngredientTypes.SAUCE, "custom sauce", 10)

        empty_burger.add_ingredient(ingredient)
        empty_burger.add_ingredient(ingredient)
        empty_burger.add_ingredient(ingredient)

        assert empty_burger.get_price() == 200 + 30


class TestBurgerReceipt:

    def test_get_receipt(self, test_burger):
        expected_receipt = """(==== Test Bun (dont eat!) ====)
= sauce Souce emulator =
= filling Velociraptor meat =
(==== Test Bun (dont eat!) ====)

Price: 400"""

        assert test_burger.get_receipt() == expected_receipt

    def test_get_receipt_without_bun(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)

        with pytest.raises(AttributeError):
            empty_burger.get_receipt()

    def test_get_receipt_without_ingredients(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)

        expected_receipt = """(==== Test Bun (dont eat!) ====)
(==== Test Bun (dont eat!) ====)

Price: 200"""

        assert empty_burger.get_receipt() == expected_receipt

    def test_get_receipt_with_one_ingredient(self, empty_burger, test_bun, test_sauce_ingredient):
        empty_burger.set_buns(test_bun)
        empty_burger.add_ingredient(test_sauce_ingredient)

        expected_receipt = """(==== Test Bun (dont eat!) ====)
= sauce Souce emulator =
(==== Test Bun (dont eat!) ====)

Price: 250"""

        assert empty_burger.get_receipt() == expected_receipt


class TestBurgerWithMocks:

    def test_set_buns_with_mock(self, empty_burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = "mock bun"
        mock_bun.price = 150

        empty_burger.set_buns(mock_bun)

        assert empty_burger.bun == mock_bun
        mock_bun.get_name.assert_not_called()
        mock_bun.get_price.assert_not_called()

    def test_get_price_with_mock_bun(self, empty_burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100

        empty_burger.set_buns(mock_bun)

        price = empty_burger.get_price()

        assert price == 200
        mock_bun.get_price.assert_called_once()

    def test_get_price_with_mock_ingredients(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 150

        empty_burger.add_ingredient(mock_ingredient1)
        empty_burger.add_ingredient(mock_ingredient2)

        price = empty_burger.get_price()

        assert price == 400
        mock_ingredient1.get_price.assert_called_once()
        mock_ingredient2.get_price.assert_called_once()

    def test_get_receipt_with_mocks(self, empty_burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "mock bun"

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = IngredientTypes.SAUCE
        mock_ingredient1.get_name.return_value = "mock sauce"

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = IngredientTypes.FILLING
        mock_ingredient2.get_name.return_value = "mock filling"

        empty_burger.set_buns(mock_bun)
        empty_burger.add_ingredient(mock_ingredient1)
        empty_burger.add_ingredient(mock_ingredient2)

        with patch.object(empty_burger, 'get_price', return_value=500):
            receipt = empty_burger.get_receipt()

        expected_receipt = """(==== mock bun ====)
= sauce mock sauce =
= filling mock filling =
(==== mock bun ====)

Price: 500"""

        assert receipt == expected_receipt
        mock_bun.get_name.assert_called()
        mock_ingredient1.get_type.assert_called()
        mock_ingredient1.get_name.assert_called()
        mock_ingredient2.get_type.assert_called()
        mock_ingredient2.get_name.assert_called()

    def test_move_ingredient_with_mocks(self, empty_burger):
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        empty_burger.add_ingredient(mock_ingredient1)
        empty_burger.add_ingredient(mock_ingredient2)
        empty_burger.add_ingredient(mock_ingredient3)

        empty_burger.move_ingredient(0, 2)

        assert empty_burger.ingredients[0] == mock_ingredient2
        assert empty_burger.ingredients[1] == mock_ingredient3
        assert empty_burger.ingredients[2] == mock_ingredient1
