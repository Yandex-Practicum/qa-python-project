# Данные для булок
bun_cases = [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("red bun", 300.0)
]

# Данные для ингредиентов
ingredient_cases = [
    ("SAUCE", "hot sauce", 100.0),
    ("SAUCE", "sour cream", 200.0),
    ("SAUCE", "chili sauce", 300.0),
    ("FILLING", "cutlet", 100.0),
    ("FILLING", "dinosaur", 200.0),
    ("FILLING", "sausage", 300.0),
]

# Пример ожидаемого чека для теста receipt
expected_receipt = (
    "(==== parmesan bun ====)\n"
    "= spicy ketchup =\n"
    "(==== parmesan bun ====)\n"
    "\n"
    "Price: 235.0\n"
)
