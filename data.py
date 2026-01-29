from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunTestData:
    #Набор тестовых данных для класса Bun
    # Позитивные тесты названий
    NAME_CASES = [
        (("black bun", 100), "black bun"),      # Стандартное название
        (("white bun", 200.50), "white bun"),   # Название с пробелом
        (("red bun", 0), "red bun"),            # Название с нулевой ценой 
        (("", 300), ""),                        # Пустое название
        (("a" * 100, 999.99), "a" * 100)        # Длинное название
    ]
    # Позитивные тесты цен
    PRICE_CASES = [
        (("black bun", 100), 100),              # Целая цена
        (("white bun", 200.50), 200.50),        # Дробная цена
        (("red bun", 0), 0),                    # Нулевая цена
        (("special bun", 999.99), 999.99)       # Высокая цена
    ]
    # Негативные тесты
    INVALID_CASES = [
    (None, 100),                                # None вместо названия булочки
    (123, 100),                                 # Число вместо названия булочки
    ("black bun", "100"),                       # Строка вместо цены (должно быть число)
    ("black bun", None)                         # None вместо цены
    ]


class IngredientTestData:
    #Набор тестовых данных для класса Ingredient
    COMMON_CASES = [
        # Формат:(ingredient_type, name, price)
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),       # базовый случай
        (INGREDIENT_TYPE_FILLING, "cutlet", 200.50),     # дробная цена
        (INGREDIENT_TYPE_SAUCE, "", 0),                  # пустое название
        (INGREDIENT_TYPE_FILLING, "a" * 100, 999.99),    # длинное название
        (INGREDIENT_TYPE_SAUCE, "sour cream", -1),       # отрицательная цена
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 999.99),  # высокая цена
        (INGREDIENT_TYPE_FILLING, "sausage", -5)         # отрицательная цена
    ]
    INVALID_CASES = [
        (None, "hot sauce", 100),                       # None вместо типа ингредиента
        (123, "hot sauce", 100),                        # число вместо типа ингредиента
        (INGREDIENT_TYPE_SAUCE, None, 100),             # None вместо названия
        (INGREDIENT_TYPE_SAUCE, 123, 100),              # число вместо названия
        (INGREDIENT_TYPE_SAUCE, "hot sauce", "100")     # строка вместо цены
    ]


class BurgerTestData:
    """Набор тестовых данных для класса Burger"""
    BURGERS_PRICE_DATA = [
        (100.10, [], 200.20),                               # только булки 
        (250.55, [50.00], 551.10),                          # булки + 1 ингредиент
        (200, [500, 1500, 500, 150, 250], 3300)             # булки + 5 ингредиентов
    ]
    """Набор тестовых данных для проверки обработки None в Burger"""
    NONE_PARAMETERS_CASES = [
        # Формат:(method, args, should_raise, needs_preparation)
        ## Принимают None без ошибок: 
        ("set_buns", [None], False, False),                 # Установка None-булочки
        ("add_ingredient", [None], False, False),           # Добавление None-ингредиента
        ## Вызывают TypeError:
        ("remove_ingredient", [None], True, False),         # Удаление по None-индексу
        ## Требуют ингредиент и вызывают ошибку:
        ("move_ingredient", [None, 0], True, True),         # None как исходный индекс
        ("move_ingredient", [0, None], True, True)          # None как целевой индекс
    ]


class ReceiptData:
    EXP_ONLY_BUN = (
        "(==== White ====)\n"
        "(==== White ====)\n\n"
        "Price: 400"
    )
    EXP_DIFF_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 700"
    )
    EXP_SAME_INGREDS = (
        "(==== White ====)\n"
        "= filling dinosaur =\n"
        "= filling dinosaur =\n"
        "= sauce hot sauce =\n"
        "(==== White ====)\n\n"
        "Price: 900"
    )
    EXP_EMPTY_NAME = (
        "(====  ====)\n"
        "=   =\n"
        "(====  ====)\n\n"
        "Price: 600"  
    )

class DatabaseData:
    DATABASE_BUNS = [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]
    DATABASE_INGREDS = [
        (0, 'SAUCE', "hot sauce", 100),
        (1, 'SAUCE', "sour cream", 200),
        (2, 'SAUCE', "chili sauce", 300),
        (3, 'FILLING', "cutlet", 100),
        (4, 'FILLING', "dinosaur", 200),
        (5, 'FILLING', "sausage", 300)
    ]
