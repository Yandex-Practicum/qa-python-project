class Data:
    # Словарь с данными булочек
    buns = {
        "black": {"name": "Чёрная булочка", "price": 1.2},
        "red": {"name": "Красная булочка", "price": 1.3},
        "white": {"name": "Белая булочка", "price": 1.0},
    }

    # Словарь с данными ингредиентов
    ingredients = {
        "chili_sauce": {"name": "Chili Sauce", "price": 1.5},
        "ketchup": {"name": "Ketchup", "price": 1.0},
        "mayo": {"name": "Mayonnaise", "price": 1.2},
        "lettuce": {"name": "Lettuce", "price": 0.5},
        "hot_sauce": {"name": "Hot Sauce", "price": 1.3},
        "sour_cream": {"name": "Sour Cream", "price": 1.4},
        "cutlet": {"name": "Cutlet", "price": 2.0},
        "dinosaur": {"name": "Dinosaur", "price": 3.0},
        "sausage": {"name": "Sausage", "price": 2.5}  # Добавлен ключ 'sausage'
    }

    # Константы для различных типов булочек и их цен
    BLACK_BUN = buns["black"]["name"]
    RED_BUN = buns["red"]["name"]
    WHITE_BUN = buns["white"]["name"]
    BLACK_BUN_PRICE = buns["black"]["price"]
    RED_BUN_PRICE = buns["red"]["price"]
    WHITE_BUN_PRICE = buns["white"]["price"]
