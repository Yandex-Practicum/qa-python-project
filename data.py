from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


BUNS = [
    ("Флюоресцентная булка R2-D3", 988),
    ("Краторная булка N-200i", 1255)
]


INGREDIENTS_SAUCES = [
    (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
    (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80),
    (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15),
    (INGREDIENT_TYPE_SAUCE, "Соус с шипами Антарианского плоскоходца", 88)
]

INGREDIENTS_FILLING = [
    (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337),
    (INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000),
    (INGREDIENT_TYPE_FILLING, "Биокотлета из марсианской Магнолии", 424),
    (INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988),
    (INGREDIENT_TYPE_FILLING, "Хрустящие минеральные кольца", 300),
    (INGREDIENT_TYPE_FILLING, "Плоды Фалленианского дерева", 874),
    (INGREDIENT_TYPE_FILLING, "Кристаллы марсианских альфа-сахаридов", 762),
    (INGREDIENT_TYPE_FILLING, "Мини-салат Экзо-Плантаго", 4400),
    (INGREDIENT_TYPE_FILLING, "Сыр с астероидной плесенью", 4142)
    ]

ALL_INGREDIENTS = INGREDIENTS_SAUCES + INGREDIENTS_FILLING  