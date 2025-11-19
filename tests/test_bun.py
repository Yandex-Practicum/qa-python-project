import pytest
from praktikum.bun import Bun

class TestBun:
    """Тест-кейсы для класса Bun"""
    
    # 1. Тест получения названия булочки
    def test_get_name_when_bun_created_then_returns_correct_name(self):
        """1. При создании булочки get_name() возвращает корректное название"""
        bun = Bun("Краторная булка", 100)
        assert bun.get_name() == "Краторная булка"
    
    # 2. Тест получения цены булочки
    def test_get_price_when_bun_created_then_returns_correct_price(self):
        """2. При создании булочки get_price() возвращает корректную цену"""
        bun = Bun("Белая булка", 200)
        assert bun.get_price() == 200
    
    # 3. Тест строкового представления
    def test_str_when_bun_created_then_returns_name(self):
        """3. При создании булочки str() возвращает её название"""
        bun = Bun("Чёрная булка", 300)
        assert str(bun) == "Чёрная булка"
    
    # 4. Тест создания булочки с нулевой ценой
    def test_create_bun_when_price_is_zero_then_success(self):
        """4. Можно создать булочку с нулевой ценой"""
        bun = Bun("Булка", 0)
        assert bun.get_price() == 0
    
    # 5. Тест создания булочки с максимальной ценой
    def test_create_bun_when_price_is_max_then_success(self):
        """5. Можно создать булочку с максимальной ценой"""
        bun = Bun("Булка", 999999)
        assert bun.get_price() == 999999
    
    # 6. Тест создания булочки с пустым названием
    def test_create_bun_when_name_empty_then_raises_exception(self):
        """6. При создании булочки с пустым названием возникает исключение"""
        with pytest.raises(ValueError):
            Bun("", 100)
    
    # 7. Тест создания булочки с None в названии
    def test_create_bun_when_name_is_none_then_raises_exception(self):
        """7. При создании булочки с None в названии возникает исключение"""
        with pytest.raises(TypeError):
            Bun(None, 100)
    
    # 8. Тест создания булочки с отрицательной ценой
    def test_create_bun_when_price_negative_then_raises_exception(self):
        """8. При создании булочки с отрицательной ценой возникает исключение"""
        with pytest.raises(ValueError):
            Bun("Булка", -100)
    
    # 9. Тест создания булочки с нечисловой ценой
    def test_create_bun_when_price_not_number_then_raises_exception(self):
        """9. При создании булочки с нечисловой ценой возникает исключение"""
        with pytest.raises(TypeError):
            Bun("Булка", "сто")
    
    # 10. Тест mock-булочки
    def test_mock_bun_when_created_then_returns_mock_values(self, mock_bun):
        """10. Mock-булочка возвращает заданные значения"""
        assert mock_bun.get_name() == "Краторная булка"