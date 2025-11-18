import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import TestData


class TestBurgerGetReceipt:
    """Тесты для метода get_receipt класса Burger"""
    
    def test_get_receipt_format_with_ingredients(self, sample_burger, mock_bun, mock_sauce, mock_filling):
        """Тест формата чека с ингредиентами"""
        mock_bun.get_name.return_value = TestData.BUN_NAME_BLACK
        mock_bun.get_price.return_value = TestData.BUN_PRICE_BLACK
        
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = TestData.SAUCE_NAME_HOT
        mock_sauce.get_price.return_value = TestData.SAUCE_PRICE_HOT
        
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = TestData.FILLING_NAME_CUTLET
        mock_filling.get_price.return_value = TestData.FILLING_PRICE_CUTLET
        
        sample_burger.set_buns(mock_bun)
        sample_burger.add_ingredient(mock_sauce)
        sample_burger.add_ingredient(mock_filling)
        
        receipt = sample_burger.get_receipt()
        
        # Точная проверка формата чека
        expected_receipt_lines = [
            f"(==== {TestData.BUN_NAME_BLACK} ====)",
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {TestData.SAUCE_NAME_HOT} =",
            f"= {INGREDIENT_TYPE_FILLING.lower()} {TestData.FILLING_NAME_CUTLET} =",
            f"(==== {TestData.BUN_NAME_BLACK} ====)",
            "",
            f"Price: {TestData.BUN_PRICE_BLACK * 2 + TestData.SAUCE_PRICE_HOT + TestData.FILLING_PRICE_CUTLET}"
        ]
        
        actual_lines = receipt.split('\n')
        assert actual_lines == expected_receipt_lines

    def test_get_receipt_format_only_bun(self, sample_burger, mock_bun):
        """Тест формата чека только с булочкой"""
        mock_bun.get_name.return_value = TestData.BUN_NAME_WHITE
        mock_bun.get_price.return_value = TestData.BUN_PRICE_WHITE
        
        sample_burger.set_buns(mock_bun)
        
        receipt = sample_burger.get_receipt()
        
        # Точная проверка формата чека
        expected_receipt_lines = [
            f"(==== {TestData.BUN_NAME_WHITE} ====)",
            f"(==== {TestData.BUN_NAME_WHITE} ====)",
            "",
            f"Price: {TestData.BUN_PRICE_WHITE * 2}"
        ]
        
        actual_lines = receipt.split('\n')
        assert actual_lines == expected_receipt_lines

    def test_get_receipt_no_bun(self, sample_burger):
        """Тест получения чека без булочки (должен упасть с AttributeError)"""
        with pytest.raises(AttributeError):
            sample_burger.get_receipt()

    def test_get_receipt_with_real_objects(self, sample_burger):
        """Тест получения чека с реальными объектами"""
        from praktikum.bun import Bun
        from praktikum.ingredient import Ingredient
        from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
        from tests.data import TestData
        
        bun = Bun(TestData.BUN_NAME_RED, TestData.BUN_PRICE_RED)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_CHILI, TestData.SAUCE_PRICE_CHILI)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME_DINOSAUR, TestData.FILLING_PRICE_DINOSAUR)
        
        sample_burger.set_buns(bun)
        sample_burger.add_ingredient(sauce)
        sample_burger.add_ingredient(filling)
        
        receipt = sample_burger.get_receipt()
        
        # Точная проверка формата чека
        expected_receipt_lines = [
            f"(==== {TestData.BUN_NAME_RED} ====)",
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {TestData.SAUCE_NAME_CHILI} =",
            f"= {INGREDIENT_TYPE_FILLING.lower()} {TestData.FILLING_NAME_DINOSAUR} =",
            f"(==== {TestData.BUN_NAME_RED} ====)",
            "",
            f"Price: {TestData.BUN_PRICE_RED * 2 + TestData.SAUCE_PRICE_CHILI + TestData.FILLING_PRICE_DINOSAUR}"
        ]
        
        actual_lines = receipt.split('\n')
        assert actual_lines == expected_receipt_lines

    def test_get_receipt_exact_match(self, sample_burger, mock_bun, mock_sauce):
        """Тест точного соответствия чека ожидаемому формату"""
        mock_bun.get_name.return_value = TestData.BUN_NAME
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = TestData.SAUCE_NAME
        
        sample_burger.set_buns(mock_bun)
        sample_burger.add_ingredient(mock_sauce)
        
        receipt = sample_burger.get_receipt()
        
        expected_receipt = (
            f"(==== {TestData.BUN_NAME} ====)\n"
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {TestData.SAUCE_NAME} =\n"
            f"(==== {TestData.BUN_NAME} ====)\n"
            f"\n"
            f"Price: {TestData.BUN_PRICE * 2 + TestData.SAUCE_PRICE}"
        )
        
        assert receipt == expected_receipt