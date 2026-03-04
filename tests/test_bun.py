import pytest
from praktikum.bun import Bun

class TestBun:
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("Very long bun name with many characters", 999.99)
    ])
    def test_bun_initialization(self, name, price):
        #Проверка инициализации булочки с разными параметрами
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
    
    def test_bun_name_getter(self):
        #Проверка получения имени булочки
        bun = Bun("test bun", 150)
        assert bun.get_name() == "test bun"
    
    def test_bun_price_getter(self):
        #Проверка получения цены булочки
        bun = Bun("test bun", 150)
        assert bun.get_price() == 150
    
    @pytest.mark.parametrize("name, price", [
        (None, 100),
        (123, 100),
        ("bun", None),
        ("bun", "100"),
        (None, None),
        (123, "456")
        ])
    def test_bun_accepts_any_types(self, name, price):
        #Проверка, что класс принимает любые типы данных
        bun = Bun(name, price)
    
        assert bun is not None
        assert bun.get_name() == name
        assert bun.get_price() == price