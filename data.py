available_buns = [["black bun", 100], ["white bun", 200], ["red bun", 300]]

available_ingredients = [["SAUCE", "hot sauce", 100], ["SAUCE", "sour cream", 200], ["SAUCE", "chili sauce", 300],
                         ["FILLING", "cutlet", 100], ["FILLING", "dinosaur", 200], ["FILLING", "sausage", 300]]


class MockBun:
    name = "black bun"
    price = 100


class MockIngredients:
    name = "hot sauce"
    price = 100
    ingredient_type = 'SAUCE'
    name_2 = "dinosaur"
    price_2 = 200
    ingredient_type_2 = "FILLING"


expected_receipt = (
        f'(==== black bun ====)\n'
        f'= sauce hot sauce =\n'
        f'= filling dinosaur =\n'
        f'(==== black bun ====)\n\n'
        f'Price: 500'
        )