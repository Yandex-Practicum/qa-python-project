from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def get_ingredient_test_data():
    """Тестовые данные для ингредиентов"""
    return [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "test", 0),
    ]


def get_ingredient_expected_data():
    """Ожидаемые данные ингредиентов из базы"""
    return {
        "sauces": [
            {"name": "hot sauce", "type": INGREDIENT_TYPE_SAUCE, "price": 100},
            {"name": "sour cream", "type": INGREDIENT_TYPE_SAUCE, "price": 200},
            {"name": "chili sauce", "type": INGREDIENT_TYPE_SAUCE, "price": 300},
        ],
        "fillings": [
            {"name": "cutlet", "type": INGREDIENT_TYPE_FILLING, "price": 100},
            {"name": "dinosaur", "type": INGREDIENT_TYPE_FILLING, "price": 200},
            {"name": "sausage", "type": INGREDIENT_TYPE_FILLING, "price": 300},
        ]
    }