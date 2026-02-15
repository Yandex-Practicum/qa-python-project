class BurgerTestData:
    BUN_PR = [
        (50, [], 100),
        (50, [10], 110),
        (30, [10, 20], 90),
        (1.5, [0.5, 0.5], 4.0),
    ]

    RECEIPT_DATA = [
        (
            "Black bun",
            50,
            [("SAUCE", "ketchup", 10), ("FILLING", "cutlet", 20)],
            "(==== Black bun ====)\n"
            "= sauce ketchup =\n"
            "= filling cutlet =\n"
            "(==== Black bun ====)\n\n"
            "Price: 130",
        )
    ]
