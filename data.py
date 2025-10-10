from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:
    buns = [
        ['Флюоресцентная булка R2-D3', 988],
        ['Краторная булка N-200i', 1255]
    ]

    ingredients = [
        [INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90],
        [INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80],
        [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15],
        [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88],
        [INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337],
        [INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000],
        [INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424],
        [INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа', 988]
    ]
