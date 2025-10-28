"""Тестовые данные для бургерной."""

# ----------------------
# Булочки
# ----------------------
WHITE_BUN_NAME = "white bun"
WHITE_BUN_PRICE = 200.0

RED_BUN_NAME = "red bun"
RED_BUN_PRICE = 300.0

BLACK_BUN_NAME = "black bun"
BLACK_BUN_PRICE = 100.0

# ----------------------
# Ингредиенты
# ----------------------
SAUCE_NAME = "hot sauce"
SAUCE_TYPE = "SAUCE"
SAUCE_PRICE = 50.0

FILLING_NAME = "cutlet"
FILLING_TYPE = "FILLING"
FILLING_PRICE = 75.0

# ----------------------
# Чеки / ожидания
# ----------------------
EXPECTED_RECEIPT_PRICE = 325.0
EXPECTED_RECEIPT_LINES = [
    "(==== black bun ====)",
    "= sauce hot sauce =",
    "= filling cutlet =",
    "(==== black bun ====)",
    "",
    "Price: 325.0"
]

# ----------------------
# Альтернативные данные для локалей / других тестов
# ----------------------
TEST_BUN_NAME_RU = "Тестовая булочка"
TEST_SAUCE_NAME_RU = "Острый соус"
TEST_SAUCE_TYPE = "SAUCE"
TEST_BUN_PRICE = 100.0
TEST_SAUCE_PRICE = 50.0
TEST_EXPECTED_TOTAL = 250.0

BUN_NAMES = ["white bun", "black bun", "red bun"]
BUN_VARIANTS = ["white bun", "black bun", "red bun"]
EXPECTED_BUNS_COUNT = 3
EXPECTED_INGREDIENTS_COUNT = 6

# ----------------------
# Цены ингредиентов для тестов базы данных
# ----------------------
INGREDIENT_PRICES = {
    50.0,   # SAUCE_PRICE
    75.0,   # FILLING_PRICE
    100.0,  # BLACK_BUN_PRICE
    200.0,  # WHITE_BUN_PRICE
    300.0,  # RED_BUN_PRICE
}
