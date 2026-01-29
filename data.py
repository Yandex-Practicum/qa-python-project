from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class DataBurgerIngredients:

    data_buns = [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)]

    data_ingredients = [(INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
                            (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88),
                            (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),
                            (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)', 3000)
                        ]


class DataDatabase:

    data_bun_db = [("black bun", 100, 0),
                    ("white bun", 200, 1),
                    ("red bun", 300, 2)
                ]

    data_ingredients_db = [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                           (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                           (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                           (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                           (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                           (INGREDIENT_TYPE_FILLING, "sausage", 300)
                        ]

