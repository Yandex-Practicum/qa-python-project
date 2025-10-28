import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import (
    BLACK_BUN_NAME, SAUCE_NAME, FILLING_NAME,
    SAUCE_TYPE, FILLING_TYPE,
    EXPECTED_RECEIPT_LINES, EXPECTED_RECEIPT_PRICE,
    TEST_BUN_NAME_RU, TEST_SAUCE_NAME_RU, TEST_SAUCE_TYPE,
    TEST_BUN_PRICE, TEST_SAUCE_PRICE, TEST_EXPECTED_TOTAL
)


class TestBurger:
    """Тестовый класс для бургера."""

    def test_get_receipt_includes_all_components(self, prepared_burger):
        """Тест генерации чека включает все компоненты."""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = BLACK_BUN_NAME
        
        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = SAUCE_TYPE
        mock_sauce.get_name.return_value = SAUCE_NAME
        
        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = FILLING_TYPE
        mock_filling.get_name.return_value = FILLING_NAME
        
        prepared_burger.bun = mock_bun
        prepared_burger.ingredients = [mock_sauce, mock_filling]
        
        with pytest.MonkeyPatch().context() as m:
            m.setattr(prepared_burger, 'get_price', lambda: EXPECTED_RECEIPT_PRICE)
            receipt = prepared_burger.get_receipt()
        
        expected_receipt = "\n".join(EXPECTED_RECEIPT_LINES)
        assert receipt == expected_receipt

    def test_get_receipt_without_bun_includes_price(self):
        """Тест генерации чека с булочкой включает цену."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = TEST_BUN_NAME_RU
        mock_bun.get_price.return_value = TEST_BUN_PRICE
    
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = TEST_SAUCE_TYPE
        mock_ingredient.get_name.return_value = TEST_SAUCE_NAME_RU
        mock_ingredient.get_price.return_value = TEST_SAUCE_PRICE
    
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
    
        receipt = burger.get_receipt()
    
        assert f"Price: {TEST_EXPECTED_TOTAL}" in receipt
