class DataAvailable:
    AVAILABLE_BUNS_NAMES = ["black bun", "white bun", "red bun"]
    AVAILABLE_BUNS_PRICES = [100, 200, 300]
    AVAILABLE_INGREDIENTS_NAMES = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
    AVAILABLE_INGREDIENTS_PRICES = [100, 200, 300, 100, 200, 300]

class DataReceipt:
    BURGER_RECEIPT = (
            '(==== fluorescent bun ====)\n'
            '= filling Cheese with asteroid mold =\n'
            '(==== fluorescent bun ====)\n\n'
            'Price: 6118'
        )

class DataBun:
    BUN_FIRST = 'fluorescent bun'
    BUN_SECOND = 'kratornaya bun'
    BUN_FIRST_PRICE = 988
    BUN_SECOND_PRICE = 1255

class DataIngredient:
    INGREDIENT_TYPE_SAUCE = 'SAUCE'
    INGREDIENT_TYPE_FILLING = 'FILLING'
    INGREDIENT_DATA = [
        (INGREDIENT_TYPE_SAUCE, 'Spicy', 90),
        (INGREDIENT_TYPE_FILLING, 'Martian bio-cutlet', 424),
        (INGREDIENT_TYPE_SAUCE, 'Space', 80),
        (INGREDIENT_TYPE_FILLING, 'Crystals of Martian alpha-saccharides', 762),
    ]
