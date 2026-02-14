# Общие константы для тестов.
# Содержит все тестовые данные, используемые в различных тестах.

# Константы для типов ингредиентов
INGREDIENT_TYPE_SAUCE = "SAUCE"
INGREDIENT_TYPE_FILLING = "FILLING"

# Константы для названий булочек
BUN_BLACK = "black bun"
BUN_WHITE = "white bun"
BUN_RED = "red bun"
BUN_SESAME = "sesame bun"
BUN_TEST = "test bun"

# Константы для названий ингредиентов
INGREDIENT_HOT_SAUCE = "hot sauce"
INGREDIENT_SOUR_CREAM = "sour cream"
INGREDIENT_CHILI_SAUCE = "chili sauce"
INGREDIENT_CUTLET = "cutlet"
INGREDIENT_DINOSAUR = "dinosaur"
INGREDIENT_SAUSAGE = "sausage"
INGREDIENT_TEST_SAUCE = "test sauce"

# Константы для цен
PRICE_50 = 50
PRICE_100 = 100
PRICE_150 = 150
PRICE_200 = 200
PRICE_300 = 300
PRICE_500 = 500
PRICE_350 = 350
PRICE_400 = 400
PRICE_75 = 75

# Тестовые данные для параметризации булочек
TEST_BUNS = [
    (BUN_BLACK, PRICE_100),
    (BUN_WHITE, PRICE_200),
    (BUN_RED, PRICE_300),
    (BUN_SESAME, PRICE_50),
]

# Тестовые данные для параметризации ингредиентов
TEST_INGREDIENTS = [
    (INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100),
    (INGREDIENT_TYPE_SAUCE, INGREDIENT_SOUR_CREAM, PRICE_200),
    (INGREDIENT_TYPE_FILLING, INGREDIENT_CUTLET, PRICE_100),
    (INGREDIENT_TYPE_FILLING, INGREDIENT_DINOSAUR, PRICE_200),
]

