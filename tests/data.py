
"""
Тестовые данные для проекта «Бургер».
"""

# Булочки
BUN_NAME_BLACK = "black bun"
BUN_PRICE_DEFAULT = 100

# Ингредиенты
INGREDIENT_TYPE_SAUCE = "SAUCE"
INGREDIENT_NAME_HOT_SAUCE = "hot sauce"
INGREDIENT_PRICE_HOT_SAUCE = 50

# Наборы данных для параметризации цены бургера:
# bun_price, [ingredient_prices], expected_total
PRICE_COMBINATIONS = [
    (100, [], 200),            # только булочки
    (100, [50], 250),          # булочки + 1 ингредиент
    (100, [50, 50], 300),      # булочки + 2 одинаковых ингредиента
    (200, [100], 500),         # другая цена булочки + ингредиент
    (50, [10, 20, 30], 160),   # дешёвая булочка + несколько ингредиентов
]
