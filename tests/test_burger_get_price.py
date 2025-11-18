import pytest
from unittest.mock import Mock
from tests.data import TestData


class TestBurgerGetPrice:
    """Тесты для метода get_price класса Burger"""
    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", TestData.EXPECTED_PRICES)
    def test_get_price_calculation(self, sample_burger, bun_price, ingredient_prices, expected_total):
        """Параметризованный тест расчета общей стоимости"""
        # Мок булочки
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        sample_burger.set_buns(bun_mock)
        
        # Моки ингредиентов
        for price in ingredient_prices:
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            sample_burger.add_ingredient(ingredient_mock)
        
        total_price = sample_burger.get_price()
        
        assert total_price == expected_total
        # Проверяем, что метод get_price вызывался у всех объектов
        assert bun_mock.get_price.call_count == 1
        for ingredient in sample_burger.ingredients:
            assert ingredient.get_price.call_count == 1

    def test_get_price_no_bun(self, sample_burger, mock_sauce):
        """Тест расчета цены без булочки (должен упасть с AttributeError)"""
        sample_burger.add_ingredient(mock_sauce)
        
        # Ожидаем AttributeError при попытке получить цену булочки
        with pytest.raises(AttributeError):
            sample_burger.get_price()

    def test_get_price_with_real_objects(self, sample_burger):
        """Тест расчета цены с реальными объектами"""
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
        
        expected_price = TestData.BUN_PRICE_RED * 2 + TestData.SAUCE_PRICE_CHILI + TestData.FILLING_PRICE_DINOSAUR
        assert sample_burger.get_price() == expected_price