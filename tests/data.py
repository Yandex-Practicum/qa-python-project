from praktikum.ingredient_types import *


class Credentials:
    bun_names = ["black bun", "white bun", "red bun", "чёрная булка", "белая булка", "красная булка"]
    bun_prices = [100, 200, 300, 101, 99, 109, 201, 299, 301]

    ingredient_combination = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)]

    receipt_data = [
        ("black bun",
         [(INGREDIENT_TYPE_SAUCE, "hot sauce")], 
         300,
            "(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300"
        ),
        ("white bun",
         [(INGREDIENT_TYPE_FILLING, "cutlet")],
         400,
            "(==== white bun ====)\n= filling cutlet =\n(==== white bun ====)\n\nPrice: 400"
        ),
       ("red bun",
        [(INGREDIENT_TYPE_SAUCE, "sour cream"), (INGREDIENT_TYPE_FILLING, "dinosaur")], 
        500,
            "(==== red bun ====)\n= sauce sour cream =\n= filling dinosaur =\n(==== red bun ====)\n\nPrice: 500"
        ),
        ("black bun",
         [
            (INGREDIENT_TYPE_SAUCE, "hot sauce"),
            (INGREDIENT_TYPE_FILLING, "cutlet"),
            (INGREDIENT_TYPE_SAUCE, "chili sauce"),
            (INGREDIENT_TYPE_FILLING, "dinosaur")
        ], 
        1000,
            "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n= sauce chili sauce =\n= filling dinosaur =\n(==== black bun ====)\n\nPrice: 1000"
        ),
        (
            "white bun",
            [], 
            200,
            "(==== white bun ====)\n(==== white bun ====)\n\nPrice: 200"
        )
    ]
