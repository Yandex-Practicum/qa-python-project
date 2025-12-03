import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
import constants


class TestBurgerWithRealData:
    """
    Дополнительные тесты для класса Burger с использованием реальных данных из Stellar Burgers.
    Тестирование граничных случаев и специфических комбинаций ингредиентов.
    """

    def test_get_price_krator_bun_with_expensive_ingredients(self):
        """
        Тест расчета стоимости с Краторной булкой и дорогими ингредиентами.
        Проверяет корректность расчета максимальной стоимости.
        """
        bun_mock = Mock()
        bun_mock.get_price.return_value = 1255  # Краторная булка
        
        filling_mock = Mock()
        filling_mock.get_price.return_value = 4400  # Мини-салат Экзо-Плантаго
        
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = 90  # Соус Spicy-X
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(sauce_mock)
        
        # 1255*2 + 4400 + 90 = 1255*2 + 4490 = 2510 + 4490 = 7000
        assert burger.get_price() == 7000

    def test_get_price_fluorescent_bun_with_cheap_ingredients(self):
        """
        Тест расчета стоимости с Флюоресцентной булкой и бюджетными ингредиентами.
        Проверяет корректность расчета минимальной стоимости.
        """
        bun_mock = Mock()
        bun_mock.get_price.return_value = 988  # Флюоресцентная булка
        
        filling_mock = Mock()
        filling_mock.get_price.return_value = 300  # Хрустящие минеральные кольца
        
        sauce_mock = Mock()
        sauce_mock.get_price.return_value = 15  # Соус традиционный галактический
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(filling_mock)
        burger.add_ingredient(sauce_mock)
        
        # 988*2 + 300 + 15 = 1976 + 315 = 2291
        assert burger.get_price() == 2291

    def test_get_receipt_with_multiple_ingredients(self):
        """
        Тест формирования чека с большим количеством ингредиентов.
        Проверяет корректность отображения всех позиций в чеке.
        """
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Краторная булка N-200i"
        bun_mock.get_price.return_value = 1255
        
        ingredient1_mock = Mock()
        ingredient1_mock.get_name.return_value = "Говяжий метеорит"
        ingredient1_mock.get_price.return_value = 3000
        
        ingredient2_mock = Mock()
        ingredient2_mock.get_name.return_value = "Сыр с астероидной плесенью"
        ingredient2_mock.get_price.return_value = 4142
        
        ingredient3_mock = Mock()
        ingredient3_mock.get_name.return_value = "Соус фирменный Space Sauce"
        ingredient3_mock.get_price.return_value = 80
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient1_mock)
        burger.add_ingredient(ingredient2_mock)
        burger.add_ingredient(ingredient3_mock)
        
        receipt = burger.get_receipt()
        
        # Проверяем что все названия присутствуют в чеке
        assert "Краторная булка N-200i" in receipt
        assert "Говяжий метеорит" in receipt
        assert "Сыр с астероидной плесенью" in receipt
        assert "Соус фирменный Space Sauce" in receipt
        
        # Проверяем общую стоимость
        assert str(1255 * 2 + 3000 + 4142 + 80) in receipt

    def test_get_price_with_only_bun(self):
        """
        Тест расчета стоимости бургера только с булкой.
        Проверяет базовую стоимость без ингредиентов.
        """
        bun_mock = Mock()
        bun_mock.get_price.return_value = 1255  # Краторная булка
        
        burger = Burger()
        burger.set_buns(bun_mock)
        
        # Только булка: 1255 * 2 = 2510
        assert burger.get_price() == 2510

    def test_get_receipt_format_with_real_data(self):
        """
        Тест формата чека с реальными данными.
        Проверяет структуру и читаемость выходных данных.
        """
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Флюоресцентная булка R2-D3"
        bun_mock.get_price.return_value = 988
        
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Биокотлета из марсианской Магнолии"
        ingredient_mock.get_price.return_value = 424
        
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        receipt = burger.get_receipt()
        
        # Проверяем что чек содержит ключевые элементы
        assert isinstance(receipt, str)
        assert len(receipt) > 0
        assert "Флюоресцентная булка R2-D3" in receipt
        assert "Биокотлета из марсианской Магнолии" in receipt
        assert "2400" in receipt  # 988*2 + 424 = 1976 + 424 = 2400