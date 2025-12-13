"""Модуль с тестовыми данными для всех тестов"""

# Тестовые данные для булочек
TEST_BUNS = [
    {"name": "black bun", "price": 100.0},
    {"name": "white bun", "price": 200.0},
    {"name": "red bun", "price": 300.0},
    {"name": "Special Bun", "price": 150.5},
    {"name": "Test Bun", "price": 100.0},
    {"name": "Another Bun", "price": 0.0},
    {"name": "Expensive Bun", "price": 999.99},
    {"name": "Bun 1", "price": 100.0},
    {"name": "Bun 2", "price": 0.0},
    {"name": "Bun 3", "price": 50.5},
    {"name": "Single Bun", "price": 100.0},
    {"name": "Bun Only", "price": 100.0},
]

# Тестовые данные для ингредиентов
TEST_INGREDIENTS = [
    {"type": "SAUCE", "name": "hot sauce", "price": 100.0},
    {"type": "SAUCE", "name": "sour cream", "price": 200.0},
    {"type": "SAUCE", "name": "chili sauce", "price": 300.0},
    {"type": "SAUCE", "name": "Test Sauce", "price": 50.0},
    {"type": "FILLING", "name": "cutlet", "price": 100.0},
    {"type": "FILLING", "name": "dinosaur", "price": 200.0},
    {"type": "FILLING", "name": "sausage", "price": 300.0},
    {"type": "FILLING", "name": "Test Filling", "price": 80.0},
    {"type": "SAUCE", "name": "Single Sauce", "price": 50.0},
]

# Тестовые данные для проверки цены
TEST_PRICE_CALCULATIONS = [
    {"bun_price": 100.0, "sauce_price": 50.0, "filling_price": 80.0, "expected": 330.0},
    {"bun_price": 0.0, "sauce_price": 0.0, "filling_price": 0.0, "expected": 0.0},
    {"bun_price": 50.5, "sauce_price": 25.25, "filling_price": 75.75, "expected": 202.0},
]

# Тестовые данные для перемещения ингредиентов
TEST_MOVE_INGREDIENT = [
    {"from_index": 0, "to_index": 1, "expected_order": [1, 0]},
    {"from_index": 1, "to_index": 0, "expected_order": [1, 0]},
    {"from_index": 0, "to_index": 0, "expected_order": [0, 1]},
]

# Тестовые данные для удаления ингредиентов
TEST_REMOVE_INGREDIENT = [
    {"index_to_remove": 0, "expected_count": 1},
    {"index_to_remove": 1, "expected_count": 1},
]
