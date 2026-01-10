import unittest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import IngredientData


class TestBurgerWithMocks(unittest.TestCase):

    def setUp(self):
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = IngredientData.BUN_NAME
        self.mock_bun.get_price.return_value = IngredientData.BUN_PRICE

        self.mock_ingredient = Mock(spec=Ingredient)
        self.mock_ingredient.get_name.return_value = IngredientData.SAUCE_NAME
        self.mock_ingredient.get_type.return_value = IngredientData.SAUCE_TYPE
        self.mock_ingredient.get_price.return_value = IngredientData.SAUCE_PRICE

        self.mock_ingredient_2 = Mock(spec=Ingredient)
        self.mock_ingredient_2.get_name.return_value = IngredientData.FILLING_NAME
        self.mock_ingredient_2.get_type.return_value = IngredientData.FILLING_TYPE
        self.mock_ingredient_2.get_price.return_value = IngredientData.FILLING_PRICE

        self.burger = Burger()
        self.burger.set_buns(self.mock_bun)

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient)
        self.burger.remove_ingredient(0)

        assert len(self.burger.ingredients) == 0

    def test_move_ingredient(self):
        self.burger.add_ingredient(self.mock_ingredient)
        self.burger.add_ingredient(self.mock_ingredient_2)
        self.burger.move_ingredient(0, 1)

        assert self.burger.ingredients[0] == self.mock_ingredient_2
        assert self.burger.ingredients[1] == self.mock_ingredient

    def test_get_price(self):
        self.burger.add_ingredient(self.mock_ingredient)

        price = self.burger.get_price()
        expected_price = IngredientData.BUN_PRICE * 2 + IngredientData.SAUCE_PRICE

        assert price == expected_price, f"Ожидаемая цена: {expected_price}, получено: {price}"

    def test_get_receipt(self):

        self.burger.add_ingredient(self.mock_ingredient)
        receipt = self.burger.get_receipt()
        expected_price = (IngredientData.BUN_PRICE * 2) + IngredientData.SAUCE_PRICE

        assert f"(==== {IngredientData.BUN_NAME} ====)" in receipt
        assert f"= {IngredientData.SAUCE_TYPE.lower()} {IngredientData.SAUCE_NAME} =" in receipt
        assert f"Price: {expected_price}" in receipt
        assert receipt.startswith(f"(==== {IngredientData.BUN_NAME} ====")
        assert receipt.endswith(f"Price: {expected_price}")

        expected_receipt = "\n".join([
            f"(==== {IngredientData.BUN_NAME} ====)",
            f"= {IngredientData.SAUCE_TYPE.lower()} {IngredientData.SAUCE_NAME} =",
            f"(==== {IngredientData.BUN_NAME} ====)",
            "",
            f"Price: {expected_price}"
        ])
        assert receipt == expected_receipt
