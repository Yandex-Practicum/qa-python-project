import praktikum.ingredient_types as TYPE

BUN_NAME = "Кунжутная"
BUN_PRICE = 20.5

INGR_TYPE = "Начинка"
INGR_NAME = "Котлета"
INGR_PRICE = 150.0

RECEIPT = "(==== Бородинская ====)\n= начинка Сало =\n= начинка Сало =\n= начинка Сало =\n(==== Бородинская ====)\n\nPrice: 100.0"

AVAILABLE_BUNS = [{"name": "black bun", "price": 100, "id": 0},
                  {"name": "white bun", "price": 200, "id": 1},
                  {"name": "red bun", "price": 300, "id": 2}]
AVAILABLE_INGREDIENTS = [{"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100, "id": 0},
                         {"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200, "id": 1},
                         {"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300, "id": 2},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100, "id": 3},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200, "id": 4},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300, "id": 5}]
