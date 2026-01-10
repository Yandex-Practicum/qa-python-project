import practicum.ingredient_types as indegrient_types

BUN_CORRECT_SET = [("Сдобная булочка", 50.0),
                   ("Wheat bun", 30),
                   ("Ржаная булочка_1", 25.0)]

BUN_INCORRECT_SET = [("Неправильный тип", None),
                     ("Неправильный тип", "100"),
                     (None, 25.0),
                     (123, 123),
                     ("Неправильный тип", [1, 2]),
                     ("Неправильный тип", {"1": 1.0, "2": 2})]

INGREDIENT_CORRECT_SET = [(indegrient_types.INGREDIENT_TYPE_SAUCE, "Mayonnaise", 15),
                          (indegrient_types.INGREDIENT_TYPE_FILLING, "Филе курицы", 150.0),
                          (indegrient_types.INGREDIENT_TYPE_SAUCE, "Ketchup_1", 75.5)]

INGREDIENT_INCORRECT_SET = [(indegrient_types.INGREDIENT_TYPE_SAUCE, "Неправильный тип", None),
                            (indegrient_types.INGREDIENT_TYPE_SAUCE, "Неправильный тип", "100"),
                            (indegrient_types.INGREDIENT_TYPE_SAUCE, None, 25.0),
                            (indegrient_types.INGREDIENT_TYPE_SAUCE, 123, 123),
                            (indegrient_types.INGREDIENT_TYPE_SAUCE, "Неправильный тип", [1, 2]),
                            (indegrient_types.INGREDIENT_TYPE_SAUCE, "Неправильный тип",
                             {"1": 1.0, "2": 2}),
                            (None, "Неправильный тип", 100)]
