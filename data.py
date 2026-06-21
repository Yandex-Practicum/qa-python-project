import praktikum.ingredient_types as TYPE

BUN_NAME = "Кунжутная"
BUN_PRICE = 20.5

INGR_TYPE = "Начинка"
INGR_NAME = "Котлета"
INGR_PRICE = 150.0

RECEIPT_BUN_NAME = "Бородинская"
RECEIPT_INGR_TYPE = "Начинка"
RECEIPT_INGR_NAME = "Сало"
RECEIPT_GET_PRICE = 100.0
RECEIPT_LIST = []
RECEIPT_LIST.append(f"(==== {RECEIPT_BUN_NAME} ====)")
RECEIPT_LIST.append(f"= {RECEIPT_INGR_TYPE.lower()} {RECEIPT_INGR_NAME} =")
RECEIPT_LIST.append(f"= {RECEIPT_INGR_TYPE.lower()} {RECEIPT_INGR_NAME} =")
RECEIPT_LIST.append(f"= {RECEIPT_INGR_TYPE.lower()} {RECEIPT_INGR_NAME} =")
RECEIPT_LIST.append(f"(==== {RECEIPT_BUN_NAME} ====)\n")
RECEIPT_LIST.append(f"Price: {RECEIPT_GET_PRICE}")
RECEIPT = '\n'.join(RECEIPT_LIST)

AVAILABLE_BUNS = [{"name": "black bun", "price": 100, "id": 0},
                  {"name": "white bun", "price": 200, "id": 1},
                  {"name": "red bun", "price": 300, "id": 2}]
AVAILABLE_INGREDIENTS = [{"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100, "id": 0},
                         {"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200, "id": 1},
                         {"type": TYPE.INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300, "id": 2},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100, "id": 3},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200, "id": 4},
                         {"type": TYPE.INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300, "id": 5}]
