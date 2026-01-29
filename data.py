# Тестовые данные для Bun
BUN_TEST_DATA = [
    ("Black Bun", 100.0),
    ("White Bun", 50.0),
    ("Red Bun", 75.0),
    ("Long Name Bun" * 10, 100.0),
    ("Zero Price Bun", 0.0),
]

# Тестовые данные для Ingredient
INGREDIENT_TEST_DATA = [
    ("SAUCE", "Ketchup", 20.0),
    ("FILLING", "Cheese", 30.0),
    ("SAUCE", "Long Sauce Name" * 10, 50.0),
    ("FILLING", "Zero Price Filling", 0.0),
]

# Тестовые данные для Burger.get_price
BURGER_PRICE_TEST_DATA = [
    (1, 220.0),  # 1 ингредиент: булочка (100 * 2) + 20
    (2, 240.0),  # 2 ингредиента: булочка (100 * 2) + 40
]

# Ожидаемые данные для Database.available_buns
DATABASE_BUNS_EXPECTED = {
    "count": 3,
    "first_name": "black bun",
    "first_price": 100,
}

# Ожидаемые данные для Database.available_ingredients
DATABASE_INGREDIENTS_EXPECTED = {
    "count": 6,
    "first_name": "hot sauce",
    "first_type": "SAUCE",
}