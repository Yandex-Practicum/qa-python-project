class BunData:

    BUN_VALID_DATA = [
        ("White bun", 2.5, "White bun", 2.5),
        ("Sesame", 3.99, "Sesame", 3.99),
        ("Brioche", 4.0, "Brioche", 4.0),
        ("Gluten-free", 5.75, "Gluten-free", 5.75),
    ]

    BUN_BOUNDARY_PRICES = [0.0, -1.0, 999999.99, 0.001, -0.0]
    BUN_BOUNDARY_NAMES = ["", "   ", "A" * 1000, "Special!@#$%", "Bun\nWith\nNewlines"]