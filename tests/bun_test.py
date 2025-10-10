import sys
import os

# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from praktikum.bun import Bun


class TestBun:

    #Тест создания булочки с валидными параметрами
    def test_init_with_valid_parameters(self):
        name = "Булка с кунжутом"
        price = 25.5
        bun = Bun(name, price)
        
        assert bun.name == name
        assert bun.price == price

    #Тест создания булочки со строковым именем и int ценой
    def test_init_with_string_name_and_int_price(self):
        bun = Bun("Классическая булка", 20)
        
        assert bun.name == "Классическая булка"
        assert bun.price == 20

    #Тест создания булочки с пустым именем
    def test_init_with_empty_string_name(self):    
        bun = Bun("", 15.5)
        
        assert bun.name == ""
        assert bun.price == 15.5

    #Тест создания булочки с очень длинным именем
    def test_init_with_very_long_name(self):       
        long_name = "А" * 1000000
        bun = Bun(long_name, 25.0)
        
        assert bun.name == long_name
        assert bun.price == 25.0

    #Тест создания булочки с нулевой ценой
    def test_init_with_zero_price(self):        
        bun = Bun("Бесплатная булка", 0.0)
        
        assert bun.name == "Бесплатная булка"
        assert bun.price == 0.0

    #Тест создания булочки с отрицательной ценой
    def test_init_with_negative_price(self):   
        bun = Bun("Выгодная булка", -5.0)
        
        assert bun.name == "Выгодная булка"
        assert bun.price == -5.0

    #Тест создания булочки с специальными символами в имени
    def test_init_with_special_characters_in_name(self):      
        special_name = "Булка@#$%^&*()_+-={}[]|\\:;\"'<>?,./"
        bun = Bun(special_name, 18.75)
        
        assert bun.name == special_name
        assert bun.price == 18.75

    #Тест создания булочки с unicode символами в имени
    def test_init_with_unicode_name(self):   
        unicode_name = "Булочка с кунжутом 🍔"
        bun = Bun(unicode_name, 35.0)
        
        assert bun.name == unicode_name
        assert bun.price == 35.0

    #Тест метода get_name возвращает правильное имя
    def test_get_name_returns_correct_name(self):
        name = "Ржаная булка"
        bun = Bun(name, 40.0)
        
        assert bun.get_name() == name

    #Тест метода get_name возвращает строковый тип
    def test_get_name_returns_string_type(self):     
        bun = Bun("Булка из ТЕСТА", 25.0)
        
        assert type(bun.get_name()) == str

    #Тест метода get_name с пустой строкой
    def test_get_name_with_empty_string(self):
        bun = Bun("", 25.0)
        
        assert bun.get_name() == ""

    #Тест метода get_price возвращает правильную цену
    def test_get_price_returns_correct_price(self):
        price = 22.75
        bun = Bun("Булка из ТЕСТА", price)
        
        assert bun.get_price() == price

    #Тест метода get_price возвращает float тип для float входа
    def test_get_price_returns_float_type_for_float_input(self):
        bun = Bun("Булка из ТЕСТА", 25.5)
        
        assert type(bun.get_price()) == float

    #Тест метода get_price возвращает int тип для int входа
    def test_get_price_returns_int_type_for_int_input(self):
        bun = Bun("Булка из ТЕСТА", 25)
        
        assert type(bun.get_price()) == int

    #Тест метода get_price с нулевой ценой
    def test_get_price_with_zero(self):
        bun = Bun("Бесплатная булка", 0)
        
        assert bun.get_price() == 0

    #Тест метода get_price с отрицательной ценой
    def test_get_price_with_negative_value(self):
        bun = Bun("Булка со скидкой", -10.5)
        
        assert bun.get_price() == -10.5

    #Тест метода get_price с очень большой ценой
    def test_get_price_with_enormous_value(self):
        enormous_price = 99999999999.99
        bun = Bun("Лакшери булка", enormous_price)
        
        assert bun.get_price() == enormous_price

    #Тест метода get_price с очень маленьким десятичным значением
    def test_get_price_with_miniscule_decimal(self):
        miniscule_price = 0.0001
        bun = Bun("Эконом булка", miniscule_price)
        
        assert bun.get_price() == miniscule_price

    #Тест независимости нескольких экземпляров
    def test_multiple_instances_independence(self):
        bun1 = Bun("Булка первая", 10.0)
        bun2 = Bun("Булка вторая", 20.0)
        
        assert bun1.get_name() == "Булка первая"
        assert bun1.get_price() == 10.0
        assert bun2.get_name() == "Булка вторая"
        assert bun2.get_price() == 20.0

    #Тест модификации атрибутов после создания
    def test_attribute_modification_after_creation(self):
        bun = Bun("Классическая булка", 15.0)
        
        # Изменяем атрибуты напрямую
        bun.name = "Классическая булка с изюминкой"
        bun.price = 25.0
        
        assert bun.get_name() == "Классическая булка с изюминкой"
        assert bun.get_price() == 25.0

    #Тест согласованности методов с атрибутами
    def test_methods_consistency(self):
        name = "Булка согласованности"
        price = 33.33
        bun = Bun(name, price)
        
        # Проверяем, что методы возвращают те же значения, что и атрибуты
        assert bun.get_name() == bun.name
        assert bun.get_price() == bun.price
