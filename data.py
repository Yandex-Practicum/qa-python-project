from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


buns_name_price = [
    ["Краторная булка N-200i", 1255.0],
    ["Флюоресцентная булка R2-D3", 988.0],
    ["Булочка марсианская", 999]
]

# список ингредиентов с типом, названием и ценой для тестов класса Ingredient
ingredients_type_name_price = [
    [INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0],
    [INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80.0],
    [INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15.0],
    [INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337.0],
    [INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000.0],
    [INGREDIENT_TYPE_FILLING, "Биокотлета из марсианской Магнолии", 424.0],
]

# список булок для тестирования базы данных
expected_buns = [
        [0, "black bun", 100],
        [1, "white bun", 200],
        [2, "red bun", 300],
    ]

# список ингредиентов для тестирования базы данных
expected_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]