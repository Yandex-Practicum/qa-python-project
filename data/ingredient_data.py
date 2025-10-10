from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


params_price = [
        (100.5, 100.5),
        (0.01, 0.01),
        (0.0, 0.0)
    ]

params_name = [
        ("Цезарь", "Цезарь"),
        ("", ""),
        ("Цезарь123", "Цезарь123"),
        ("цезарь", "цезарь"),
        ("Cesar", "Cesar"),
        ("!.'-&|\\:", "!.'-&|\\:"),
        ("Ц", "Ц"),
        (" ", " ")
    ]

params_type = [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
        ("", ""),
        ("Соус123", "Соус123"),
        ("котлета", "котлета"),
        ("!.'-&|\\:", "!.'-&|\\:"),
        ("С", "С"),
        (" ", " ")
    ]
