"""Модуль с тестовыми данными для всех тестов"""


class TestData:
    """Класс с тестовыми данными"""
    
    # Данные для булочек
    BUN_NAME = "test bun"
    BUN_PRICE = 100
    BUN_NAME_BLACK = "black bun"
    BUN_NAME_WHITE = "white bun"
    BUN_NAME_RED = "red bun"
    BUN_PRICE_BLACK = 100
    BUN_PRICE_WHITE = 200
    BUN_PRICE_RED = 300
    
    # Данные для соусов
    SAUCE_NAME = "test sauce"
    SAUCE_NAME_HOT = "hot sauce"
    SAUCE_NAME_SOUR_CREAM = "sour cream"
    SAUCE_NAME_CHILI = "chili sauce"
    SAUCE_PRICE = 50
    SAUCE_PRICE_HOT = 100
    SAUCE_PRICE_SOUR_CREAM = 200
    SAUCE_PRICE_CHILI = 300
    
    # Данные для начинок
    FILLING_NAME = "test filling"
    FILLING_NAME_CUTLET = "cutlet"
    FILLING_NAME_DINOSAUR = "dinosaur"
    FILLING_NAME_SAUSAGE = "sausage"
    FILLING_PRICE = 80
    FILLING_PRICE_CUTLET = 100
    FILLING_PRICE_DINOSAUR = 200
    FILLING_PRICE_SAUSAGE = 300
    
    # Ожидаемые цены для параметризованных тестов
    EXPECTED_PRICES = [
        (100, [50, 30, 20], 300),   # 100*2 + 50+30+20
        (50, [10, 15], 125),        # 50*2 + 10+15
        (80, [], 160),              # Только булочка
        (200, [100, 100, 100], 700) # 200*2 + 100*3
    ]