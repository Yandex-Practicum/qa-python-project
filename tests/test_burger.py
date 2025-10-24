import pytest
from unittest.mock import Mock
from tests import data


class TestBurger:

    def test_burger_price(self, burger_with_ingredients, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        expected_price = (mock_bun.get_price() * 2 +
                         mock_ingredient_sauce.get_price() +
                         mock_ingredient_filling.get_price())

        assert burger_with_ingredients.get_price() == expected_price
        assert burger_with_ingredients.get_price() == data.ExpectedPrices.BURGER_WITH_INGREDIENTS

    def test_burger_receipt(self, burger_with_ingredients):
        receipt = burger_with_ingredients.get_receipt()

        expected_receipt_lines = [
            f"(==== {data.BurgerData.TEST_BUN_NAME} ====)",
            f"= {data.BurgerData.TEST_SAUCE_TYPE.lower()} {data.BurgerData.TEST_SAUCE_NAME} =",
            f"= {data.BurgerData.TEST_FILLING_TYPE.lower()} {data.BurgerData.TEST_FILLING_NAME} =",
            f"(==== {data.BurgerData.TEST_BUN_NAME} ====)",
            "",
            f"Price: {data.ExpectedPrices.BURGER_WITH_INGREDIENTS}"
        ]

        expected_receipt = "\n".join(expected_receipt_lines)
        assert receipt == expected_receipt

    def test_burger_receipt_structure(self, burger_with_ingredients):
        receipt = burger_with_ingredients.get_receipt()
        receipt_lines = receipt.split('\n')

        assert len(receipt_lines) == 6
        assert receipt_lines[0] == f"(==== {data.BurgerData.TEST_BUN_NAME} ====)"
        assert receipt_lines[1] == f"= {data.BurgerData.TEST_SAUCE_TYPE.lower()} {data.BurgerData.TEST_SAUCE_NAME} ="
        assert receipt_lines[2] == f"= {data.BurgerData.TEST_FILLING_TYPE.lower()} {data.BurgerData.TEST_FILLING_NAME} ="
        assert receipt_lines[3] == f"(==== {data.BurgerData.TEST_BUN_NAME} ====)"
        assert receipt_lines[4] == ""
        assert receipt_lines[5] == f"Price: {data.ExpectedPrices.BURGER_WITH_INGREDIENTS}"

    def test_empty_burger_receipt(self, empty_burger):
        receipt = empty_burger.get_receipt()

        expected_receipt = "\n".join([
            "(====  ====)",
            "(====  ====)",
            "",
            f"Price: {data.ExpectedPrices.EMPTY_BURGER}"
        ])

        assert receipt == expected_receipt

    def test_burger_with_only_bun_receipt(self, burger_with_bun, mock_bun):
        receipt = burger_with_bun.get_receipt()

        expected_receipt_lines = [
            f"(==== {data.BurgerData.TEST_BUN_NAME} ====)",
            f"(==== {data.BurgerData.TEST_BUN_NAME} ====)",
            "",
            f"Price: {data.ExpectedPrices.BURGER_WITH_BUN_ONLY}"
        ]

        expected_receipt = "\n".join(expected_receipt_lines)
        assert receipt == expected_receipt
